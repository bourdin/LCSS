import pymef90

def createParser():
    import argparse
    import sys
    parser = argparse.ArgumentParser()
    #parser.add_argument('--rescale', default=False, action='store_true',help='Convert to non-dimensional form')
    geom = parser.add_argument_group('Geometry')
    geom.add_argument('--width',type=float,default=50,help='Domain width [m]')
    geom.add_argument('--height',type=float,default=50,help='Domain height m]')
    geom.add_argument('--thickness',type=float,default=1,help='Domain thickness [m]')
    geom.add_argument('--lc',type=float,default=10,help='Initial crack length [m]')
    geom.add_argument('--order',type=float,default=1,choices = [1,2],help='finite element discretization order')

    mesh = parser.add_argument_group('Mesh')
    mesh.add_argument('--hf',type=float,default=1.e-1,help='Fine mesh size [m]')
    mesh.add_argument('--hc',type=float,default=1.e-1,help='Coarse mesh size [m]')
    mesh.add_argument('--r',type=float,default=2,help='Mesh transition width [m]')

    beam = parser.add_argument_group('Beam')
    beam.add_argument('--intensity','--I',type=float,default=1,help='Intensity (50 - 200) [W]')
    beam.add_argument('--criticalRadius','--r0',type=float,default=1,help='Critical radius (1e-4 - 1e-3)[m]')
    beam.add_argument('--scanningSpeed','--V',type=float,default=1,help='Beam scanning speed (~ 2.5e-3) [m/s]')
    beam.add_argument('--position','--x0',type=float,default=0,help='Beam position in relation to the center of the plate(0) [m]')

    material = parser.add_argument_group('Material')
    material.add_argument('--YoungsModulus', '--E', type=float, default=1, help="Young's modulus (~ 74e9) [Pa]")
    material.add_argument('--PoissonRatio', '--nu', type=float, default=0.23, help="Poisson ratio (~ 0.23)")
    material.add_argument('--fractureToughness', '--gc', type=float, default=1, help="Fracture toughness [J/m^2]")
    material.add_argument('--linearThermalExpansion','--beta', type=float, default=1., help='Linear thermal expansion coefficient [1/K]')
    material.add_argument('--lightAbsorpsionCoefficient','--alphaL', type=float, default=9., help='Light absorbtion coefficient at beam frequency (~ 9) [1/m]')
    material.add_argument('--density', '--rho', type=float, default=1,help='Density (~ 2.48e3)[kg/m^3]')
    material.add_argument('--specificHeat', '--cp', type=float, default=1,help='Specific heat (0.35e3 - 1e3 [J/K/kg]')
    material.add_argument('--thermalConductivity', '--k', type=float, default=1.,help='Thermal conductivity (0.82 - 1.37) [J/s/K/m]')
    material.add_argument('--internalLength', type=float, default=4e-1,help='Internal Length [m]')
    material.add_argument('--residualStiffness', type=float, default=1e-8,help='residual stiffness')

    vf = parser.add_argument_group('vDef parameters')
    vf.add_argument('--meshdir',help='Folder where meshes are stored',default='Meshes')
    vf.add_argument('--workdir',help='Folder where the computation will be ran (default is Job ID)',default=None)
    vf.add_argument('--prefix',help='Name files after prefix + geometry instead of job ID',default=None)
    vf.add_argument('--dontmesh',help='Do not try to generate mesh if not found in meshdir',default=False,action='store_true')
    vf.add_argument('--yamlfile',help='Name of the yaml options file',default='LCSS.yaml')
    vf.add_argument('--geofile',help='Name of the gmsh geo file',default='LCSS.geo')
    vf.add_argument('--atnum',help='Regularization type',type=int,default=1)
    vf.add_argument('--irrevtol',help='Irreversibility tolerance',type=float,default=1.)
    vf.add_argument('--extraopts',help='Additional options to pass to vDef',default=None)
    vf.add_argument('--gceff',help='Correct fracture toughnesses for h/epsilon effect',default=False,action='store_true')
    vf.add_argument('--unilateralcontact',help='Unilateral contact handling',choices=['none','hydrostaticdeviatoric'],default='none')
    vf.add_argument('--hypre',help='Use hypre as a preconditioner for the displacement field',default=False,action='store_true')
    vf.add_argument('--ml',help='Use ML as a preconditioner for the displacement field',default=False,action='store_true')
    vf.add_argument('--sor',help='SOR multiplier for alternate minimizations',type=float,default=1.)

    misc = parser.add_argument_group('Miscellaneous')
    misc.add_argument('--mpiexec',help='mpi job launcher',default='mpiexec')
    misc.add_argument('--meshonly',help='meshonly, do not run',default=False,action='store_true')
    misc.add_argument('--forcemesh',help='re-generate mesh even if it exists',default=False,action='store_true')
    misc.add_argument('--postprocess',help='Automatically run visit to generate .png file',default=False,action='store_true')
    args = parser.parse_args()

    parser.add_argument('configfile',nargs='?',type=argparse.FileType(mode='r'),default=None,help='YAML configuration file (overrides all other options)')
    return parser

