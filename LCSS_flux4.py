#!/usr/bin/env python
import sys

def parse(args=None):
    import argparse
    alpha_L = 9
    beta = 90e-6
    d = 7e-4
    r0 = 1.0e-4
    rho = 2.48e3
    cp = 1.5e3
    V = 2.5e-3
    k = 1.

    t0 = rho * cp * r0**2/k
    x0 = r0

    ### Get options from the command line
    parser = argparse.ArgumentParser(description='Compute boundary displacement for a surfing computation')
    parser.add_argument('-i','--inputfile',help='input file',default=None)
    parser.add_argument('-o','--outputfile',help='output file',default=None)
    parser.add_argument('--pathfile',help='File describing the beam path',default=None)
    parser.add_argument("--d",type=float,help="Plate thickness [m]",default=7.e-4)
    parser.add_argument("--alpha",type=float,help="Glass absorbtion coefficient [m^-1]",default=9.)    
    parser.add_argument("--r0",type=float,default=1.e-4,help='Beam critical radius [m]')
    parser.add_argument("--dt",type=float,default=1,help='Time step size [s]')

    parser.add_argument("--x0",type=float,default=r0,help='Space rescaling factor for numerical simulations [1]')
    parser.add_argument("--t0",type=float,default=t0,help='Time scaling factor for numerical simulation [m]')

    parser.add_argument("--cs",type=int,nargs='*',help="list of cell sets where the beam is applied",default=[1,])
    parser.add_argument("--force",action="store_true",default=False,help="Overwrite existing files without prompting")
    options = parser.parse_args()
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
        return 2.*Wabs / np.pi / r0**2 * np.exp(-2.*(r/r0)**2)

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
    exoin  = exo.exodus(options.inputfile,mode='r')
    exoout = exoin.copy(options.outputfile)
    exoout.close()
    exoout  = exo.exodus(options.outputfile,mode='a',array_type='numpy')
    ### Adding a QA record, needed until visit fixes its exodus reader
    import datetime
    import os.path
    import sys
    QA_rec_len = 32
    QA = [os.path.basename(sys.argv[0]),os.path.basename(__file__),datetime.date.today().strftime('%Y%m%d'),datetime.datetime.now().strftime("%H:%M:%S")]
    exoout.put_qa_records([[ q[0:31] for q in QA],])

    exoformat(exoout)
    
    cellCenters = {}
    for cs in options.cs:
        print("Computing cell center coordinates for set {0}".format(cs))
        cellCenters[cs] = cellCenter(exoout,cs)

    beamPath = np.loadtxt(options.pathfile)
    substep = 0
    for step in range(beamPath.shape[0]-1):
        print("Processing path line {0}  (t={1:.2e}-{2:.2e}, x0={3:.2e}-{4:.2e}, y0={5:.2e}-{6:.2e}, W={7:.2e}-{8:.2e})".format(step,beamPath[step][0],beamPath[step+1][0],beamPath[step][1],beamPath[step+1][1],beamPath[step][2],beamPath[step+1][2],beamPath[step][3],beamPath[step+1][3]))
        nstep = int((beamPath[step+1][0] - beamPath[step][0]) / options.dt) + 1
        print("nstep", nstep, beamPath[step+1][0] - beamPath[step][0])
        T  = np.linspace(beamPath[step][0]/options.t0,beamPath[step+1][0]/options.t0,nstep)
        X0 = np.linspace(beamPath[step][1]/options.x0,beamPath[step+1][1]/options.x0,nstep)
        Y0 = np.linspace(beamPath[step][2]/options.x0,beamPath[step+1][2]/options.x0,nstep)
        W  = np.linspace(beamPath[step][3] * (1.- np.exp(-options.alpha * options.d)),beamPath[step+1][3] * (1.- np.exp(-options.alpha * options.d)),nstep)
        for t,x0,y0,w in zip(T,X0,Y0,W):
            substep += 1
            print("   time step {4}: t={0:.2e}, x0={1:.2e}, y0={2:.2e}, W={3:.2e}])".format(t,x0,y0,w,substep))
            exoout.put_time(substep,t)
            for cs in options.cs:
                theta = beamProfile(exoout,w,options.r0 / options.x0,[x0,y0,0],cs,cellCenters[cs])
                exoout.put_element_variable_values(cs,"Heat_Flux",substep,theta)
    exoout.close()
    
if __name__ == "__main__":
        sys.exit(main())

