from visit import *
def parse(args=None):
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--output',default=None)
    parser.add_argument('--force',default=False,action='store_true')
    parser.add_argument('inputfile',help='input file')
    return parser.parse_args()

if __name__ == "__main__":
    import sys  
    import os.path

    options = parse()

    prefix = os.path.splitext(options.inputfile)[0]
    if options.output == None:
        options.output='{0:s}-crackLength.txt'.format(prefix)

    if os.path.exists(options.inputfile) and (not os.path.exists(options.output)  or options.force):
        prefix,ext = os.path.splitext(options.inputfile)
        MyDatabase = options.inputfile
        status = OpenDatabase(options.inputfile)       
        if not status:
            print ("unable to open database {0}".format(options.inputfile))
            sys.exit(-1)

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
    
        f = open(options.output,'w')
        f.write('# lc, a\n')

        for state in range(TimeSliderGetNStates()):
            Query("SpatialExtents", use_actual_data=1)
            SetTimeSliderState(state)
            crackBB = GetQueryOutputValue()
            print(state,crackBB)
            f.write('{0[0]:.4e} {0[1]:.4e}\n'.format(crackBB))
        f.close()
        DeleteAllPlots()
        CloseDatabase(MyDatabase)

        sys.exit(0)
    else:
        print('output file exists, or input file does not exist. Exiting...')
        sys.exit(-1)

