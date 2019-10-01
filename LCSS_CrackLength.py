from visit import *
def getlaststep(fname):
  ### open file
  f=open(fname)
  ### Read last line in a string
  lastline = f.readlines()[-1]
  laststep = lastline.rsplit()[0] 
  return(int(laststep))


def getCrackLength(options):
    import json
    import os
    import os.path
    import shutil
    import math
    
    prefix,ext = os.path.splitext(options.inputfile)


    ##  
    ## Open the database
    ##
    MyDatabase = options.inputfile
    status = OpenDatabase(options.inputfile, options.step-1)       
    if not status:
        print ("unable to open database {0}".format(options.inputfile))
        return -1

    AddPlot('Pseudocolor', 'Damage')
    PseudocolorAtts = PseudocolorAttributes()
    PseudocolorAtts.scaling = PseudocolorAtts.Linear  # Linear, Log, Skew
    PseudocolorAtts.skewFactor = 1
    PseudocolorAtts.limitsMode = PseudocolorAtts.OriginalData  # OriginalData, CurrentPlot
    PseudocolorAtts.centering = PseudocolorAtts.Natural  # Natural, Nodal, Zonal
    PseudocolorAtts.colorTableName = "hot"
    PseudocolorAtts.invertColorTable = 0
    PseudocolorAtts.opacityType = PseudocolorAtts.FullyOpaque  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange
    PseudocolorAtts.renderSurfaces = 1
    PseudocolorAtts.renderWireframe = 0
    PseudocolorAtts.renderPoints = 0
    PseudocolorAtts.smoothingLevel = 0
    PseudocolorAtts.legendFlag = 1
    PseudocolorAtts.lightingFlag = 0
    SetPlotOptions(PseudocolorAtts)
    AddOperator("Isovolume", 1)
    SetActivePlots(0)
    IsovolumeAtts = IsovolumeAttributes()
    IsovolumeAtts.lbound = 0.95
    IsovolumeAtts.ubound = 1e+37
    IsovolumeAtts.variable = "Damage"
    SetOperatorOptions(IsovolumeAtts, 0, 1)
    DrawPlots()
    SetQueryFloatFormat("%g")
    Query("SpatialExtents", use_actual_data=1)
    crackBB = GetQueryOutputValue()

    DeleteAllPlots()
    CloseDatabase(MyDatabase)
    return crackBB[0],crackBB[1]

def parse(args=None):
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--step',type=int,default=0)
    parser.add_argument('--output',default=None)
    parser.add_argument('--force',default=False,action='store_true')
    parser.add_argument('inputfile',help='input file')
    return parser.parse_args()

if __name__ == "__main__":
    import sys  
    import os.path

    options = parse()

    prefix = os.path.splitext(options.inputfile)[0]
    laststep = 1000000
    if options.step == 0:
        enerfile = prefix+'.ener'
        if os.path.exists(enerfile):
            laststep = getlaststep(enerfile)
        else:
            enerfile = prefix.split('_out')[0]+'.ener'
            if os.path.exists(enerfile):
                laststep = getlaststep(enerfile)
            else:
                print "unable to find step to plot."
                sys.exit(-1)
        options.step = laststep

    if options.output == None:
        options.output='{0}-{1:04d}-crackLength.txt'.format(prefix,options.step)

    if os.path.exists(options.inputfile) and (not os.path.exists(options.output)  or options.force):
        amin,amax = getCrackLength(options)   
        f = open(options.output,'w')
        f.write('# lc, a\n')
        f.write('{0:.4e} {1:.4e}\n'.format(amin,amax))
        f.close()

        sys.exit(0)
    else:
        print('output file exists, or input file does not exist. Exiting...')
        sys.exit(-1)

