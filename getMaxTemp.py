#!/usr/bin/env python

def parse(args=None):
    import argparse
    r0 = 1.0e-4
    rho = 2.48e3
    cp = 1.5e3
    k = 1.
    d = 0.7e-3

    t0 = rho * cp * r0**2/k
    theta0 = 1./k/d

    ### Get options from the command line
    parser = argparse.ArgumentParser(description='Compute boundary displacement for a surfing computation')
    parser.add_argument('-i','--inputfile',help='input file',default=None)
    parser.add_argument("--step",type=int,default=None,help='time step (leave empty for all steps)')
    parser.add_argument("--t0",type=float,default=t0,help='Time scaling factor in numerical simulation [s]. default {0:.4e}'.format(t0))
    parser.add_argument("--theta0",type=float,default=theta0,help='Temperature scaling factor in numerical simulation [K]. default {0:.4e}'.format(theta0))
    options = parser.parse_args()
    return options
    

def main():
    import numpy as np
    import os
    import pymef90
    import sys
    if sys.version_info.major == 3:
        import exodus3 as exo
    else:
        import exodus2 as exo

    options = parse()
    exoin = exo.exodus(options.inputfile,mode='r',array_type='numpy')
    if options.step == None:
        steps = range(exoin.num_times())
        times = exoin.get_times()
    else:
        steps = (options.step-1,)
        times = (exoin.get_times()[options.step-1],)
    for s,t in zip(steps,times):
        thetaMax = max(exoin.get_node_variable_values('Temperature',s))*options.theta0
        print('step {0} time (real) {1:.4e} max temp (real): {2:.4e}'.format(s+1,t,thetaMax))
    exoin.close()
if __name__ == "__main__":
    import sys
    sys.exit(main())
