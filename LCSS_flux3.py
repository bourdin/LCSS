#!/usr/bin/env python
import sys

def parse(args=None):
    import argparse
    ### Get options from the command line
    parser = argparse.ArgumentParser(description='Compute boundary displacement for a surfing computation')
    parser.add_argument('-i','--inputfile',help='input file',default=None)
    parser.add_argument('-o','--outputfile',help='output file',default=None)
    parser.add_argument("--Wabs",type=float,help="Absorbed flux per unit of surface",default=1.)    
    parser.add_argument("--r0",type=float,default=1.,help='Beam critical radius')
    parser.add_argument("--initialPos",type=float,nargs=3,help="Beam initial postion",default=[0.,0.,0.])
    parser.add_argument("--finalPos",type=float,nargs=3,help="Beam final postion",default=[0.,0.,0.])
    parser.add_argument("--initialTip",type=float,nargs=3,help="Logical crack tip initial position",default=None)
    parser.add_argument("--internalLength",type=float,help="internal length",default=0)
    parser.add_argument("--cs",type=int,nargs='*',help="list of cell sets where the beam is applied",default=[1,])
    parser.add_argument("--force",action="store_true",default=False,help="Overwrite existing files without prompting")
    parser.add_argument("--time_min",type=float,default=0.,help='Start time')
    parser.add_argument("--time_max",type=float,default=1.,help='End time')
    parser.add_argument("--time_numstep",type=int,default=1,help='Number of time steps')
    options = parser.parse_args()
    if options.initialTip == None:
        options.initialTip = options.initialPos
    return options
    
def exoformat(e):
    global_variable_name = ["Elastic Energy","Work","Surface Energy","Total Energy"]
    if e.num_dimensions() == 2: 
        node_variable_name  = ["Temperature","Damage","Displacement_X","Displacement_Y"]
        element_variable_name   = ["Heat_Flux","External_Temperature",
                                   "Stress_XX","Stress_YY","Stress_XY"]
    else:
        node_variable_name  = ["Temperature","Damage","Displacement_X","Displacement_Y","Displacement_Z"]
        element_variable_name   = ["Heat_Flux","External_Temperature",
                                   "Stress_XX","Stress_YY","Stress_ZZ","Stress_YZ","Stress_XZ","Stress_XY"]
    e.set_global_variable_number(0)
    e.set_node_variable_number(len(node_variable_name))
    for i in range(len(node_variable_name)):
        e.put_node_variable_name(node_variable_name[i],i+1)
    e.set_element_variable_number(len(element_variable_name))
    for i in range(len(element_variable_name)):
        e.put_element_variable_name(element_variable_name[i],i+1)
    e.set_element_variable_truth_table([True] * e.numElemBlk.value * len(element_variable_name))
    return(0)

def beamProfile(e,Wabs,r0,beamPos,cs,cellCenters):
    import exodus as exo
    import numpy as np
    
    dim = e.num_dimensions()
    X,Y,Z=e.get_coords()
    numCells = e.elem_blk_info(cs)[1]
    numVertexPerCell = e.elem_blk_info(cs)[2]
    theta = np.zeros(numCells)
    
    def profile(r):
        return 2.*Wabs / np.pi / r0**2 * np.exp(-2.*(r**2/r0)**2)

    r = np.sqrt( (cellCenters[:,0]-beamPos[0])**2 + (cellCenters[:,1]-beamPos[1])**2)
    theta = profile(r)
    return theta

def cellCenter(e,cs):
    import exodus as exo
    import numpy as np
    
    dim              = e.num_dimensions()
    X,Y,Z            = e.get_coords()
    numCells         = e.elem_blk_info(cs)[1]
    numVertexPerCell = e.elem_blk_info(cs)[2]
    cellCenters      = np.empty([numCells,dim])

    cs_info = e.elem_blk_info(cs)
    connect = e.get_elem_connectivity(cs)[0].reshape((cs_info[1],cs_info[2]))
    cellCenters[:,0] = [ np.average(X[cell-1]) for cell in connect ]
    cellCenters[:,1] = [ np.average(Y[cell-1]) for cell in connect ]
    if dim == 3:
        cellCenters[:,2] = [ np.average(Z[cell-1]) for cell in connect ]
    return cellCenters

def damageProfile(e,ell,initialTip):
    import exodus as exo
    import numpy as np
    

    dim = e.num_dimensions()
    X,Y,Z=e.get_coords()
    alpha = np.zeros(e.num_nodes())
    
    for v in range(e.num_nodes()):
        if X[v] <= initialTip[0]:
            d = abs(Y[v]-initialTip[1])
        else:
            d = np.sqrt((X[v]-initialTip[0])**2 + (Y[v]-initialTip[1])**2)
        if d <= 2.*ell:
            alpha[v] = (d/2./ell-1)**2
    return alpha

def main():
    import exodus as exo
    import numpy as np
    import os
    import pymef90
    options = parse()
    
    if  os.path.exists(options.outputfile):
        if options.force:
            os.remove(options.outputfile)
        else:
            if pymef90.confirm("ExodusII file {0} already exists. Overwrite?".format(options.outputfile)):
                os.remove(options.outputfile)
            else:
                print ('\n\t{0} was NOT generated.\n'.format(options.outputfile))
                return -1
    exoin  = exo.exodus(options.inputfile,array_type='numpy')

    exoout = exoin.copy(options.outputfile)
    exoformat(exoout)
    exoin.close()
    exoout.close()
    exoout  = exo.exodus(options.outputfile,mode='a',array_type='numpy')
    
    #T = np.linspace(options.time_min,options.time_max,options.time_numstep)
    x0 = np.linspace(options.initialPos[0],options.finalPos[0],options.time_numstep)
    y0 = np.linspace(options.initialPos[1],options.finalPos[2],options.time_numstep)
    z0 = np.linspace(options.initialPos[2],options.finalPos[2],options.time_numstep)

    cellCenters = {}
    for cs in options.cs:
        print("Computing cell center coordinates for set {0}".format(cs))
        cellCenters[cs] = cellCenter(exoout,cs)
    for step in range(options.time_numstep):
        print("Processing time step {0} (x0=[{1},{2},{3})".format(step,x0[step],y0[step],z0[step]))
        exoout.put_time(step+1,x0[step])
        for cs in options.cs:
            theta = beamProfile(exoout,options.Wabs,options.r0,[x0[step],y0[step],z0[step]],cs,cellCenters[cs])
            exoout.put_element_variable_values(cs,"Heat_Flux",step+1,theta)
    exoout.close()
    
if __name__ == "__main__":
        sys.exit(main())

