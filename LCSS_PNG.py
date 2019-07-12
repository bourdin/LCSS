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
    AnnotationAtts.axes2D.xAxis.label.visible = 0
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
    AnnotationAtts.axes2D.xAxis.grid = 0
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
    AnnotationAtts.axes2D.yAxis.label.visible = 0
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
    AnnotationAtts.axes2D.yAxis.grid = 0
    AnnotationAtts.userInfoFlag = 0
    AnnotationAtts.userInfoFont.font = AnnotationAtts.userInfoFont.Arial  # Arial, Courier, Times
    AnnotationAtts.userInfoFont.scale = 1
    AnnotationAtts.userInfoFont.useForegroundColor = 1
    AnnotationAtts.userInfoFont.color = (0, 0, 0, 255)
    AnnotationAtts.userInfoFont.bold = 0
    AnnotationAtts.userInfoFont.italic = 0
    AnnotationAtts.databaseInfoFlag = 0
    AnnotationAtts.timeInfoFlag = 1
    AnnotationAtts.databaseInfoFont.font = AnnotationAtts.databaseInfoFont.Arial  # Arial, Courier, Times
    AnnotationAtts.databaseInfoFont.scale = 1
    AnnotationAtts.databaseInfoFont.useForegroundColor = 1
    AnnotationAtts.databaseInfoFont.color = (0, 0, 0, 255)
    AnnotationAtts.databaseInfoFont.bold = 0
    AnnotationAtts.databaseInfoFont.italic = 0
    AnnotationAtts.databaseInfoExpansionMode = AnnotationAtts.File  # File, Directory, Full, Smart, SmartDirectory
    AnnotationAtts.databaseInfoTimeScale = 1
    AnnotationAtts.databaseInfoTimeOffset = 0
    AnnotationAtts.legendInfoFlag = 0

    visit.SetAnnotationAttributes(AnnotationAtts)
    return 0

def getlaststep(fname):
  ### open file
  f=open(fname)
  ### Read last line in a string
  lastline = f.readlines()[-1]
  laststep = lastline.rsplit()[0] 
  return(int(laststep))

def drawCrack(displacementScaling=.1,damageThreshold=.99,BB=None):
    ##
    ## Add pseudocolor plot of fracture field
    ##

    AddPlot('Pseudocolor', 'Temperature')
    PseudocolorAtts = PseudocolorAttributes()
    PseudocolorAtts.scaling = PseudocolorAtts.Linear  # Linear, Log, Skew
    PseudocolorAtts.skewFactor = 1
    PseudocolorAtts.limitsMode = PseudocolorAtts.OriginalData  # OriginalData, CurrentPlot
    PseudocolorAtts.minFlag = 0
    PseudocolorAtts.maxFlag = 0
    PseudocolorAtts.centering = PseudocolorAtts.Natural  # Natural, Nodal, Zonal
    PseudocolorAtts.colorTableName = "hot"
    PseudocolorAtts.invertColorTable = 0
    PseudocolorAtts.opacityType = PseudocolorAtts.FullyOpaque  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange
    PseudocolorAtts.renderSurfaces = 1
    PseudocolorAtts.renderWireframe = 0
    PseudocolorAtts.renderPoints = 0
    PseudocolorAtts.smoothingLevel = 0
    PseudocolorAtts.legendFlag = 0
    PseudocolorAtts.lightingFlag = 0
    SetPlotOptions(PseudocolorAtts)

    AddOperator("Displace", 1)
    SetActivePlots(0)
    DisplaceAtts = DisplaceAttributes()
    DisplaceAtts.factor = displacementScaling
    DisplaceAtts.variable = "Displacement"
    SetOperatorOptions(DisplaceAtts, 1)

    DrawPlots()
    if BB == None:
        Query("SpatialExtents", use_actual_data=1)
        BB = GetQueryOutputValue() 
    SetView(BB)

    AddPlot("Subset", "ElementBlock", 1, 1)
    SetActivePlots(1)
    SetActivePlots(1)
    SubsetAtts = SubsetAttributes()
    SubsetAtts.colorType = SubsetAtts.ColorBySingleColor  # ColorBySingleColor, ColorByMultipleColors, ColorByColorTable
    SubsetAtts.colorTableName = "Default"
    SubsetAtts.invertColorTable = 0
    SubsetAtts.legendFlag = 0
    SubsetAtts.lineStyle = SubsetAtts.SOLID  # SOLID, DASH, DOT, DOTDASH
    SubsetAtts.lineWidth = 1
    SubsetAtts.singleColor = (255, 255, 255, 255)
    SubsetAtts.SetMultiColor(0, (255, 0, 0, 255))
    SubsetAtts.SetMultiColor(1, (0, 255, 0, 255))
    SubsetAtts.SetMultiColor(2, (0, 0, 255, 255))
    SubsetAtts.SetMultiColor(3, (0, 255, 255, 255))
    SubsetAtts.SetMultiColor(4, (255, 0, 255, 255))
    SubsetAtts.SetMultiColor(5, (255, 255, 0, 255))
    SubsetAtts.subsetNames = ("1", "10", "11", "12", "20", "21")
    SubsetAtts.opacity = 1
    SubsetAtts.wireframe = 0
    SubsetAtts.drawInternal = 0
    SubsetAtts.smoothingLevel = 0
    SubsetAtts.pointSize = 0.05
    SubsetAtts.pointType = SubsetAtts.Point  # Box, Axis, Icosahedron, Octahedron, Tetrahedron, SphereGeometry, Point, Sphere
    SubsetAtts.pointSizeVarEnabled = 0
    SubsetAtts.pointSizeVar = "default"
    SubsetAtts.pointSizePixels = 2
    SetPlotOptions(SubsetAtts)
    silr = SILRestriction()
    silr.SuspendCorrectnessChecking()
    silr.TurnOnAll()
    for silSet in (2,3,4,5):
        silr.TurnOffSet(silSet)
    silr.EnableCorrectnessChecking()
    SetPlotSILRestriction(silr ,0)
    DrawPlots()
    return BB    

def drawCrack2(displacementScaling=.1,damageThreshold=.99,BB=None):
    ##
    ## Add pseudocolor plot of fracture field
    ##

    AddPlot('Pseudocolor', 'Temperature')
    PseudocolorAtts = PseudocolorAttributes()
    PseudocolorAtts.scaling = PseudocolorAtts.Linear  # Linear, Log, Skew
    PseudocolorAtts.skewFactor = 1
    PseudocolorAtts.limitsMode = PseudocolorAtts.OriginalData  # OriginalData, CurrentPlot
    # PseudocolorAtts.minFlag = 1
    # PseudocolorAtts.min = 0
    # PseudocolorAtts.maxFlag = 1
    # PseudocolorAtts.max = 1
    PseudocolorAtts.centering = PseudocolorAtts.Natural  # Natural, Nodal, Zonal
    PseudocolorAtts.colorTableName = "hot"
    PseudocolorAtts.invertColorTable = 0
    PseudocolorAtts.opacityType = PseudocolorAtts.FullyOpaque  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange
    PseudocolorAtts.renderSurfaces = 1
    PseudocolorAtts.renderWireframe = 0
    PseudocolorAtts.renderPoints = 0
    PseudocolorAtts.smoothingLevel = 0
    PseudocolorAtts.legendFlag = 0
    PseudocolorAtts.lightingFlag = 0
    SetPlotOptions(PseudocolorAtts)

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

    # AddPlot("Contour", "Temperature", 1, 1)
    # SetActivePlots(1)
    # ContourAtts = ContourAttributes()
    # ContourAtts.defaultPalette.equalSpacingFlag = 1
    # ContourAtts.defaultPalette.discreteFlag = 1
    # ContourAtts.defaultPalette.categoryName = "Standard"
    # ContourAtts.changedColors = ()
    # ContourAtts.colorType = ContourAtts.ColorByColorTable  # ColorBySingleColor, ColorByMultipleColors, ColorByColorTable
    # ContourAtts.colorTableName = "hot_and_cold"
    # ContourAtts.invertColorTable = 0
    # ContourAtts.legendFlag = 0
    # ContourAtts.lineWidth = 1
    # ContourAtts.contourNLevels = 10
    # ContourAtts.contourValue = ()
    # ContourAtts.contourPercent = ()
    # ContourAtts.contourMethod = ContourAtts.Level  # Level, Value, Percent
    # ContourAtts.minFlag = 0
    # ContourAtts.maxFlag = 0
    # ContourAtts.min = 0
    # ContourAtts.max = 1
    # ContourAtts.scaling = ContourAtts.Linear  # Linear, Log
    # ContourAtts.wireframe = 0
    # SetPlotOptions(ContourAtts)
    DrawPlots()
    if BB == None:
        Query("SpatialExtents", use_actual_data=1)
        newBB = GetQueryOutputValue() 
    else:
        newBB = tuple(BB)    
    SetView(newBB)

    AddPlot("Subset", "ElementBlock", 1, 1)
    SetActivePlots(2)
    SubsetAtts = SubsetAttributes()
    SubsetAtts.colorType = SubsetAtts.ColorBySingleColor  # ColorBySingleColor, ColorByMultipleColors, ColorByColorTable
    SubsetAtts.colorTableName = "Default"
    SubsetAtts.invertColorTable = 0
    SubsetAtts.legendFlag = 0
    SubsetAtts.lineStyle = SubsetAtts.SOLID  # SOLID, DASH, DOT, DOTDASH
    SubsetAtts.lineWidth = 2
    SubsetAtts.singleColor = (255, 0, 0, 255)
    #SubsetAtts.SetMultiColor(0, (255, 0, 0, 255))
    #SubsetAtts.SetMultiColor(1, (0, 255, 0, 255))
    #SubsetAtts.SetMultiColor(2, (0, 0, 255, 255))
    #SubsetAtts.SetMultiColor(3, (0, 255, 255, 255))
    #SubsetAtts.SetMultiColor(4, (255, 0, 255, 255))
    #SubsetAtts.SetMultiColor(5, (255, 255, 0, 255))
    #SubsetAtts.subsetNames = ("1", "10", "11", "12", "20", "21")
    SubsetAtts.opacity = 1
    SubsetAtts.wireframe = 0
    SubsetAtts.drawInternal = 0
    SubsetAtts.smoothingLevel = 0
    SubsetAtts.pointSize = 0.05
    SubsetAtts.pointType = SubsetAtts.Point  # Box, Axis, Icosahedron, Octahedron, Tetrahedron, SphereGeometry, Point, Sphere
    SubsetAtts.pointSizeVarEnabled = 0
    SubsetAtts.pointSizeVar = "default"
    SubsetAtts.pointSizePixels = 2
    SetPlotOptions(SubsetAtts)
    silr = SILRestriction()
    silr.SuspendCorrectnessChecking()
    silr.TurnOnAll()
    for silSet in silr.SetsInCategory('ElementBlock')[:-2]:
       silr.TurnOffSet(silSet)
    silr.EnableCorrectnessChecking()
    SetPlotSILRestriction(silr ,0)
    DrawPlots()
    return newBB
    
def SetView(BB):
    View2DAtts = View2DAttributes()
    View2DAtts.viewportCoords = (0.05, 0.95, 0.05, 0.95)
    View2DAtts.windowCoords = BB
    View2DAtts.fullFrameActivationMode = View2DAtts.Auto  # On, Off, Auto
    View2DAtts.fullFrameAutoThreshold = 100
    View2DAtts.xScale = View2DAtts.LINEAR  # LINEAR, LOG
    View2DAtts.yScale = View2DAtts.LINEAR  # LINEAR, LOG
    View2DAtts.windowValid = 1
    SetView2D(View2DAtts)
    RecenterView()

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
    
    prefix,ext = os.path.splitext(options.inputfile)

    laststep = 1000000
    enerfile = prefix+'.ener'
    if os.path.exists(enerfile):
        laststep = getlaststep(enerfile)
    else:
        enerfile = prefix.split('_out')[0]+'.ener'
        if os.path.exists(enerfile):
            laststep = getlaststep(enerfile)
        else:
            print "unable to find step to plot."
            return -1
    if options.step == 0:
        step = laststep
    else:
        step = min(options.step,laststep)

    ##  
    ## Open the database
    ##
    MyDatabase = options.inputfile
      
    print ('Trying to load {0}'.format(options.inputfile))
    status = OpenDatabase(options.inputfile, step-1)       
    if not status:
        print ("unable to open database {0}".format(options.inputfile))
        return -1

    BB = drawCrack2(options.displacementScaling,options.damageThreshold,options.BB)
    SetAnnotations()
    DrawPlots()


    W = BB[1]-BB[0]
    H = BB[3]-BB[2]
    if W > H:
        geometry = (2048,int(2048.*H/W))
    else:
        geometry = (int(2048.*W/H),2048)

    if options.output != None:
        filename=os.path.splitext(options.output)[0]
    else:
        filename = '{basename}-{step:04d}'.format(basename = prefix,step=step)
    if options.bg == 'white':
        setBGWhite()
    else:
        setBGBlack()
    status = savePNG(filename,geometry)

    DeleteAllPlots()
    CloseDatabase(MyDatabase)
    return 0

def parse(args=None):
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--step',type=int,default=0)
    parser.add_argument('--bg',choices=['white','black'],default='white')
    parser.add_argument('--displacementScaling',type=float,default=0)
    parser.add_argument('--BB',type=float,nargs=4,default=None)
    parser.add_argument('--damageThreshold',type=float,default=.99)
    parser.add_argument('--output',default=None)
    parser.add_argument('--force',default=False,action='store_true')
    parser.add_argument('inputfile',help='input file')
    return parser.parse_args()

if __name__ == "__main__":
    import sys  
    import os.path

    options = parse()
    if os.path.exists(options.inputfile) and (not os.path.exists(options.output)  or options.force):
        print('processing {0}'.format(options.inputfile)) 
        plot(options)   
        sys.exit(0)
    else:
        sys.exit(-1)

