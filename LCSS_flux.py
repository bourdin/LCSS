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
    parser.add_argument("--initialPos",type=float,nargs=3,help="initial crack tip postion",default=[0.,0.,0.])
    parser.add_argument("--cs",type=int,nargs='*',help="list of cell sets where the beam is applied",default=[])
    parser.add_argument("--force",action="store_true",default=False,help="Overwrite existing files without prompting")
    parser.add_argument("--time_min",type=float,default=1.,help='Start time')
    parser.add_argument("--time_max",type=float,default=1.,help='End time')
    parser.add_argument("--time_numstep",type=int,default=1,help='Number of time steps')
    return parser.parse_args()
    
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

def beamProfile(e,Wabs,r0,initialPos,cs):
    import exodus as exo
    import numpy as np
    

    dim = e.num_dimensions()
    X,Y,Z=e.get_coords()
    theta = np.zeros(e.elem_blk_info(cs)[1],dtype=exo.c_double)
    
    connect = e.get_elem_connectivity(cs)
    for cid in range(connect[1]):
        vertices = [connect[0][cid*connect[2]+c]-1 for c in range(connect[2])]
        x = np.average([X[v] for v in vertices])
        y = np.average([Y[v] for v in vertices])
        r = np.sqrt((x-initialPos[0])**2+(y-initialPos[1])**2)
        theta[cid] = 2.*Wabs / np.pi / r0**2 * np.exp(-2.*(r/r0)**2)
    return theta

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
    exoin.close()
    exoformat(exoout)
    
    T = np.linspace(options.time_min,options.time_max,options.time_numstep)
    for step in range(options.time_numstep):
        exoout.put_time(step+1,T[step])
    for cs in options.cs:
        theta = beamProfile(exoout,options.Wabs,options.r0,options.initialPos,cs)
        step = 0
        for step in range(options.time_numstep):
            exoout.put_element_variable_values(cs,"Heat_Flux",step+1,theta)
            step += 1
    exoout.close()
    
if __name__ == "__main__":
        sys.exit(main())

