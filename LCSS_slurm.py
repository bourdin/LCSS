#!/usr/bin/env python
#SBATCH -J LCSS
import LCSS
import hashlib
import pymef90
    
    

def main():
    import os
    import os.path
    import numpy as np
    import pymef90
    import shutil
    

    parser = LCSS.createParser()
    options = pymef90.parse(parser,key='configfile')
    Geometry = pymef90.parseGroup(parser,options,'Geometry')
    str = repr(Geometry).encode("utf-8")
    options.hash = hashlib.sha1(str).hexdigest()
    options.__dict__ = pymef90.PrepareJob(Geometry,options.__dict__)
    scriptpath = os.path.dirname(os.path.abspath(__file__))

    ###
    ### Search for the mesh file, and generate it if it is missing
    ###
    archmeshprefix = os.path.join(options.meshdir,options.hash)
    if not os.path.isfile(archmeshprefix+'.gen') or options.forcemesh:
        if options.dontmesh:
            print('Cannot find mesh, exiting')
            return -1
        else:
            print('{0}.gen not found: generating new mesh'.format(archmeshprefix))
            if not os.path.exists(options.meshdir):
                os.makedirs(options.meshdir)
            pymef90.argsWrite(options.geofile,
                      os.path.join(options.meshdir,options.hash+'.geo'),
                      options.__dict__)
            os.chdir(options.meshdir)
            os.system('gmsh -2 -format msh2 -order {order} {hash}.geo'.format(**options.__dict__))
            os.system('gmsh2exo.py --force {hash}.msh {hash}.gen'.format(**options.__dict__))            
            #pymef90.Dictwritetxt(Geometry.__dict__,archmeshprefix+'.txt')
            pymef90.DictwriteJSON(Geometry.__dict__,archmeshprefix+'.json')


    else:
        print("Found matching mesh at {0}".format(archmeshprefix))

    ###
    ### Create computation directory
    ###
    if options.meshonly:
        return 0
    ###
    ### Write 00_INFO.txt and 00_INFO.json
    ###
    if not os.path.exists(options.workdir):
        os.makedirs(options.workdir)
    os.chdir(options.workdir)


    #pymef90.Dictwritetxt(options.__dict__,'00_INFO.txt',overwrite=False)
    pymef90.DictwriteJSON(options.__dict__,'00_INFO.json',overwrite=True)
    shutil.copyfile(archmeshprefix+'.gen',os.path.join(options.workdir,options.prefix+'.gen'))

    ###
    ### Prepare vDef yaml options file
    ####
    pymef90.argsWrite(options.yamlfile,
              os.path.join(options.workdir,options.prefix+'.yaml'),
              options.__dict__)

    ### Generate heat flux in output file
    # find the flux script within the path and pythonpath
    for binpath in sys.path+os.getenv('PATH').split(':'):
        if os.path.exists(os.path.join(binpath,"LCSS_flux2.py")):
            break
    cmd = '{0} -i {prefix}.gen -o {prefix}_out.gen --cs 1 2 --force --initialPos {initialPos[0]}  {initialPos[1]} {initialPos[2]} --finalPos {finalPos[0]} {finalPos[1]} {finalPos[2]} --r0 {criticalRadius} --Wabs {intensity} --time_min {time_min} --time_max {time_max} --time_numstep {time_numstep}'.format(os.path.join(binpath,'LCSS_flux2.py'),**options.__dict__)
    print('Now running: {0}'.format(cmd))
    os.system(cmd)

    ### Run the computation
    if os.path.isfile(os.path.join(os.getenv("MEF90_DIR"),"bin",os.getenv("PETSC_ARCH"),"vDef")):
        bin = os.path.join(os.getenv("MEF90_DIR"),"bin",os.getenv("PETSC_ARCH"),"vDef")
    else:
        print('Cannot find binary for vDef')
        sys.exit(-1)

    if options.mpiexec == 'mpirun':
        options.mpiexec += ' -machinefile {0}'.format(os.getenv("PBS_NODEFILE"))
    cmd1 = options.mpiexec + ' {0:s} -prefix {prefix:s} -options_file_yaml {prefix:s}.yaml '.format(bin,**options.__dict__)
    if options.extraopts:
        cmd1+= options.extraopts
    if options.hypre:
        cmd1 += ' -disp_pc_type hypre -disp_pc_hypre_type boomeramg -disp_pc_hypre_boomeramg_strong_threshold 0.9 '
    if options.ml:
        cmd1 += ' -disp_pc_type ml'
    #if options.unilateralcontact == 'none':
    #    cmd1 += ' -disp_snes_type ksponly'
        
    #cmd1 += ' -temp_ksp_monitor_true_residual -temp_ksp_converged_reason'
    cmd1 += ' -disp_snes_monitor'


    print("Now running: {0}".format(cmd1))
    os.system(cmd1)

    if options.postprocess:
        cmd = 'ml visit; visit -cli -nowin -s {0} --output {1}.png {1}_out.gen;'.format(os.path.join(binpath,"LCSS_PNG.py"),options.prefix)
        print('now running: {0}'.format(cmd))
        os.system(cmd)
        cmd = 'ml visit; visit -cli -nowin -s {0} --output {1}_disp.png --displacementScaling 1 {1}_out.gen;'.format(os.path.join(binpath,"LCSS_PNG.py"),options.prefix)
        print('now running: {0}'.format(cmd))
        os.system(cmd)

import sys  
if __name__ == "__main__":
    sys.exit(main())

