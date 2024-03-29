from visit import *
def savePNG(filename,geometry=[4096,4096]):
    SaveWindowAtts = SaveWindowAttributes()
    SaveWindowAtts.outputToCurrentDirectory = 1
    SaveWindowAtts.fileName = filename
    SaveWindowAtts.family = 0
    SaveWindowAtts.format = SaveWindowAtts.PNG
    SaveWindowAtts.width = geometry[0]
    SaveWindowAtts.height = geometry[1]
    SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint
    SaveWindowAtts.forceMerge = 1
    SetSaveWindowAttributes(SaveWindowAtts)
    return SaveWindow()

def SetAnnotations():
    import visit
    AnnotationAtts = AnnotationAttributes()
    AnnotationAtts.axes2D.visible = 1
    AnnotationAtts.axes2D.autoSetTicks = 1
    AnnotationAtts.axes2D.autoSetScaling = 1
    AnnotationAtts.axes2D.lineWidth = 0
    AnnotationAtts.axes2D.tickLocation = AnnotationAtts.axes2D.Outside  # Inside, Outside, Both
    AnnotationAtts.axes2D.tickAxes = AnnotationAtts.axes2D.BottomLeft  # Off, Bottom, Left, BottomLeft, All
    AnnotationAtts.axes2D.xAxis.title.visible = 0
    AnnotationAtts.axes2D.xAxis.title.font.font = AnnotationAtts.axes2D.xAxis.title.font.Arial  # Arial, Courier, Times
    AnnotationAtts.axes2D.xAxis.title.font.scale = 1
    AnnotationAtts.axes2D.xAxis.title.font.useForegroundColor = 1
    AnnotationAtts.axes2D.xAxis.title.font.color = (0, 0, 0, 255)
    AnnotationAtts.axes2D.xAxis.title.font.bold = 0
    AnnotationAtts.axes2D.xAxis.title.font.italic = 1
    AnnotationAtts.axes2D.xAxis.title.userTitle = 0
    AnnotationAtts.axes2D.xAxis.title.userUnits = 0
    AnnotationAtts.axes2D.xAxis.title.title = "X-Axis"
    AnnotationAtts.axes2D.xAxis.title.units = ""
    AnnotationAtts.axes2D.xAxis.label.visible = 1
    AnnotationAtts.axes2D.xAxis.label.font.font = AnnotationAtts.axes2D.xAxis.label.font.Arial  # Arial, Courier, Times
    AnnotationAtts.axes2D.xAxis.label.font.scale = 1
    AnnotationAtts.axes2D.xAxis.label.font.useForegroundColor = 1
    AnnotationAtts.axes2D.xAxis.label.font.color = (0, 0, 0, 255)
    AnnotationAtts.axes2D.xAxis.label.font.bold = 0
    AnnotationAtts.axes2D.xAxis.label.font.italic = 1
    AnnotationAtts.axes2D.xAxis.label.scaling = 0
    AnnotationAtts.axes2D.xAxis.tickMarks.visible = 1
    AnnotationAtts.axes2D.xAxis.tickMarks.majorMinimum = 0
    AnnotationAtts.axes2D.xAxis.tickMarks.majorMaximum = 1
    AnnotationAtts.axes2D.xAxis.tickMarks.minorSpacing = 0.02
    AnnotationAtts.axes2D.xAxis.tickMarks.majorSpacing = 0.2
    AnnotationAtts.axes2D.xAxis.grid = 1
    AnnotationAtts.axes2D.yAxis.title.visible = 0
    AnnotationAtts.axes2D.yAxis.title.font.font = AnnotationAtts.axes2D.yAxis.title.font.Arial  # Arial, Courier, Times
    AnnotationAtts.axes2D.yAxis.title.font.scale = 1
    AnnotationAtts.axes2D.yAxis.title.font.useForegroundColor = 1
    AnnotationAtts.axes2D.yAxis.title.font.color = (0, 0, 0, 255)
    AnnotationAtts.axes2D.yAxis.title.font.bold = 0
    AnnotationAtts.axes2D.yAxis.title.font.italic = 1
    AnnotationAtts.axes2D.yAxis.title.userTitle = 0
    AnnotationAtts.axes2D.yAxis.title.userUnits = 0
    AnnotationAtts.axes2D.yAxis.title.title = "Y-Axis"
    AnnotationAtts.axes2D.yAxis.title.units = ""
    AnnotationAtts.axes2D.yAxis.label.visible = 1
    AnnotationAtts.axes2D.yAxis.label.font.font = AnnotationAtts.axes2D.yAxis.label.font.Arial  # Arial, Courier, Times
    AnnotationAtts.axes2D.yAxis.label.font.scale = 1
    AnnotationAtts.axes2D.yAxis.label.font.useForegroundColor = 1
    AnnotationAtts.axes2D.yAxis.label.font.color = (0, 0, 0, 255)
    AnnotationAtts.axes2D.yAxis.label.font.bold = 0
    AnnotationAtts.axes2D.yAxis.label.font.italic = 1
    AnnotationAtts.axes2D.yAxis.label.scaling = 0
    AnnotationAtts.axes2D.yAxis.tickMarks.visible = 1
    AnnotationAtts.axes2D.yAxis.tickMarks.majorMinimum = 0
    AnnotationAtts.axes2D.yAxis.tickMarks.majorMaximum = 1
    AnnotationAtts.axes2D.yAxis.tickMarks.minorSpacing = 0.02
    AnnotationAtts.axes2D.yAxis.tickMarks.majorSpacing = 0.2
    AnnotationAtts.axes2D.yAxis.grid = 1
    AnnotationAtts.userInfoFlag = 0
    AnnotationAtts.userInfoFont.font = AnnotationAtts.userInfoFont.Arial  # Arial, Courier, Times
    AnnotationAtts.userInfoFont.scale = 1
    AnnotationAtts.userInfoFont.useForegroundColor = 1
    AnnotationAtts.userInfoFont.color = (0, 0, 0, 255)
    AnnotationAtts.userInfoFont.bold = 0
    AnnotationAtts.userInfoFont.italic = 0
    AnnotationAtts.databaseInfoFlag = 1
    AnnotationAtts.timeInfoFlag = 0
    AnnotationAtts.databaseInfoFont.font = AnnotationAtts.databaseInfoFont.Arial  # Arial, Courier, Times
    AnnotationAtts.databaseInfoFont.scale = 1
    AnnotationAtts.databaseInfoFont.useForegroundColor = 1
    AnnotationAtts.databaseInfoFont.color = (0, 0, 0, 255)
    AnnotationAtts.databaseInfoFont.bold = 0
    AnnotationAtts.databaseInfoFont.italic = 0
    AnnotationAtts.databaseInfoExpansionMode = AnnotationAtts.File  # File, Directory, Full, Smart, SmartDirectory
    AnnotationAtts.databaseInfoTimeScale = 0
    AnnotationAtts.databaseInfoTimeOffset = 0
    AnnotationAtts.legendInfoFlag = 1

    visit.SetAnnotationAttributes(AnnotationAtts)
    return 0

def getlaststep(fname):
  ### open file
  f=open(fname)
  ### Read last line in a string
  lastline = f.readlines()[-1]
  laststep = lastline.rsplit()[0] 
  return(int(laststep))


def draw(displacementScaling=.1,damageThreshold=.99,tempMax=None,BB=None):
    ##
    ## Add pseudocolor plot of fracture field
    ##

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
    DrawPlots()

    AddOperator("Displace", 1)
    SetActivePlots(0)
    DisplaceAtts = DisplaceAttributes()
    DisplaceAtts.factor = displacementScaling
    DisplaceAtts.variable = "Displacement"
    SetOperatorOptions(DisplaceAtts, 1)
    AddOperator("Isovolume", 1)
    IsovolumeAtts = IsovolumeAttributes()
    IsovolumeAtts.lbound = -1e+37
    IsovolumeAtts.ubound = damageThreshold
    IsovolumeAtts.variable = "Damage"
    SetOperatorOptions(IsovolumeAtts, 1)
    DrawPlots()

    AddPlot("Contour", "Temperature", 1, 1)
    SetActivePlots(1)
    ContourAtts = ContourAttributes()
    ContourAtts.defaultPalette.equalSpacingFlag = 1
    ContourAtts.defaultPalette.discreteFlag = 1
    ContourAtts.defaultPalette.categoryName = "Standard"
    ContourAtts.changedColors = ()
    ContourAtts.colorType = ContourAtts.ColorByColorTable  # ColorBySingleColor, ColorByMultipleColors, ColorByColorTable
    ContourAtts.colorTableName = "hot_and_cold"
    ContourAtts.invertColorTable = 0
    ContourAtts.legendFlag = 1
    ContourAtts.lineWidth = 1
    ContourAtts.contourNLevels = 11
    ContourAtts.contourValue = ()
    ContourAtts.contourPercent = ()
    ContourAtts.contourMethod = ContourAtts.Level  # Level, Value, Percent
    ContourAtts.minFlag = 1
    ContourAtts.min = 0
    if tempMax:
        ContourAtts.maxFlag = 1
        ContourAtts.max = tempMax
    else:
        ContourAtts.maxFlag = 0
    ContourAtts.scaling = ContourAtts.Linear  # Linear, Log
    ContourAtts.wireframe = 0
    SetPlotOptions(ContourAtts)
    DrawPlots()
    if BB == None:
        Query("SpatialExtents", use_actual_data=1)
        newBB = GetQueryOutputValue() 
    else:
        newBB = tuple(BB)    
    SetView(newBB)

    # AddPlot("Subset", "ElementBlock", 1, 1)
    # SetActivePlots(2)
    # SubsetAtts = SubsetAttributes()
    # SubsetAtts.colorType = SubsetAtts.ColorBySingleColor  # ColorBySingleColor, ColorByMultipleColors, ColorByColorTable
    # SubsetAtts.colorTableName = "Default"
    # SubsetAtts.invertColorTable = 0
    # SubsetAtts.legendFlag = 0
    # SubsetAtts.lineStyle = SubsetAtts.SOLID  # SOLID, DASH, DOT, DOTDASH
    # SubsetAtts.lineWidth = 3
    # SubsetAtts.singleColor = (0, 0, 0, 255)
    # SubsetAtts.opacity = 1
    # SubsetAtts.wireframe = 0
    # SubsetAtts.drawInternal = 0
    # SubsetAtts.smoothingLevel = 0
    # SubsetAtts.pointSize = 0.05
    # SubsetAtts.pointType = SubsetAtts.Point  # Box, Axis, Icosahedron, Octahedron, Tetrahedron, SphereGeometry, Point, Sphere
    # SubsetAtts.pointSizeVarEnabled = 0
    # SubsetAtts.pointSizeVar = "default"
    # SubsetAtts.pointSizePixels = 1
    # SetPlotOptions(SubsetAtts)
    # silr = SILRestriction()
    # silr.SuspendCorrectnessChecking()
    # silr.TurnOnAll()
    # for silSet in silr.SetsInCategory('ElementBlock')[:-2]:
    #    silr.TurnOffSet(silSet)
    # silr.EnableCorrectnessChecking()
    # SetPlotSILRestriction(silr ,0)
    DrawPlots()
    return newBB
    
def SetView(BB):
    View2DAtts = View2DAttributes()
    View2DAtts.viewportCoords = (0.2, 0.95, 0.05, 0.95)
    View2DAtts.windowCoords = BB
    View2DAtts.fullFrameActivationMode = View2DAtts.Auto  # On, Off, Auto
    View2DAtts.fullFrameAutoThreshold = 100
    View2DAtts.xScale = View2DAtts.LINEAR  # LINEAR, LOG
    View2DAtts.yScale = View2DAtts.LINEAR  # LINEAR, LOG
    View2DAtts.windowValid = 1
    SetView2D(View2DAtts)

def setBGBlack():
    AnnotationAtts = GetAnnotationAttributes()
    AnnotationAtts.backgroundColor = (0, 0, 0, 255)
    AnnotationAtts.foregroundColor = (255, 255, 255, 255)
    SetAnnotationAttributes(AnnotationAtts)
    return 0

def setBGWhite():
    AnnotationAtts = GetAnnotationAttributes()
    AnnotationAtts.backgroundColor = (255, 255, 255, 255)
    AnnotationAtts.foregroundColor = (0, 0, 0, 255)
    SetAnnotationAttributes(AnnotationAtts)
    return 0

def plot(options):
    import json
    import os
    import os.path
    import shutil
    import math
    
    prefix,ext = os.path.splitext(os.path.basename(options.inputfile))
    rootdir    = os.path.dirname(options.inputfile)
    framesDir  = os.path.join(rootdir,'Frames')
    movName    = os.path.join(rootdir,'{0}-disp{1:.2f}.mp4'.format(prefix,options.displacementScaling))

    if not os.path.exists(framesDir):
        os.makedirs(framesDir)


    laststep = 1000000
    if options.step_max == 0:
        enerfile = os.path.join(rootdir,prefix+'.ener')
        if os.path.exists(enerfile):
            laststep = getlaststep(enerfile)
        else:
            enerfile = os.path.join(rootdir,prefix.split('_out')[0]+'.ener')
            if os.path.exists(enerfile):
                laststep = getlaststep(enerfile)
            else:
                print "unable to find step to plot."
                return -1
        stepmax = laststep
    else:
        stepmax = options.step_max
    stepmin = options.step_min


    ### Open the database
    
    MyDatabase = options.inputfile
      
    print ('Trying to load {0}'.format(options.inputfile))
    status = OpenDatabase(options.inputfile, stepmin-1)       
    if not status:
        print ("unable to open database {0}".format(options.inputfile))
        return -1

    BB = draw(options.displacementScaling,options.damageThreshold,options.BB)

    SetAnnotations()
    DrawPlots()


    W = BB[1]-BB[0]
    H = BB[3]-BB[2]
    if W > H:
        geometry = (2048,2*int(2048.*H/W/2.))
    else:
        geometry = (2*int(2048.*W/H/2.),2048)

    if options.bg == 'white':
        setBGWhite()
    else:
        setBGBlack()

    for step in range(stepmin-1,stepmax):
        SetTimeSliderState(step)
        filename = '{basename}-{step:04d}-disp{displacementScaling:.2f}'.format(basename = os.path.join(rootdir,'Frames',prefix),step=step,**options.__dict__)
        status = savePNG(filename,geometry)

    DeleteAllPlots()
    CloseDatabase(MyDatabase)

    cmd_exists = lambda x: any(os.access(os.path.join(path, x), os.X_OK) for path in os.environ["PATH"].split(os.pathsep))    
    #cmd = 'ffmpeg -y -i Frames/{prefix}-%04d.png -vcodec mjpeg -qscale 1  {prefix}.avi'.format(prefix=prefix)
    cmd = 'ffmpeg -y -i {framesDir}/{prefix}-%04d-disp{displacementScaling:.2f}.png -f mp4 -vcodec h264 -pix_fmt yuv420p  {movName}'.format(framesDir=framesDir,prefix=prefix,movName=movName,**options.__dict__)
    if cmd_exists('ffmpeg'):
        print('\n\t running {0}\n'.format(cmd))
        os.system(cmd)
    else:
        print('\t{0}'.format(cmd))

    return 0

def parse(args=None):
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--bg',choices=['white','black'],default='white')
    parser.add_argument('--displacementScaling',type=float,default=0)
    parser.add_argument('--BB',type=float,nargs=4,default=None)
    parser.add_argument('--damageThreshold',type=float,default=.99)
    parser.add_argument('--YoungsModulus',type=float,default=1)
    parser.add_argument('--PoissonRatio',type=float,default=.23)
    parser.add_argument('--step_min',type=int,default=1)
    parser.add_argument('--step_max',type=int,default=0)
    parser.add_argument('--temp_max',type=float,default=0.15)
    parser.add_argument('--force',default=False,action='store_true')
    parser.add_argument('inputfile',help='input file')
    return parser.parse_args()

if __name__ == "__main__":
    import sys  
    import os.path

    options = parse()
    if os.path.exists(options.inputfile):
        print('processing {0}'.format(options.inputfile)) 
        plot(options)   
        sys.exit(0)
    else:
        print('output file exists, or input file does not exist. Exiting...')
        sys.exit(-1)

