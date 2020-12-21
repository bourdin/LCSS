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
    # Begin spontaneous state
    View3DAtts = View3DAttributes()
    View3DAtts.viewNormal = (-0.5807712759861402, -0.6171360034225121, 0.5308934716768702)
    View3DAtts.focus = (0, 0, -0.175)
    View3DAtts.viewUp = (0.08848834059742759, 0.6004278743402324, 0.7947680046992227)
    View3DAtts.viewAngle = 30
    View3DAtts.parallelScale = 58.3098
    View3DAtts.nearPlane = -116.62
    View3DAtts.farPlane = 116.62
    View3DAtts.imagePan = (0.2294172242755754, 0.191482960420443)
    View3DAtts.imageZoom = 3.7975
    View3DAtts.perspective = 1
    View3DAtts.eyeAngle = 2
    View3DAtts.centerOfRotationSet = 0
    View3DAtts.centerOfRotation = (0, 0, -0.175)
    View3DAtts.axis3DScaleFlag = 0
    View3DAtts.axis3DScales = (1, 1, 1)
    View3DAtts.shear = (0, 0, 1)
    View3DAtts.windowValid = 1
    SetView3D(View3DAtts)
    # End spontaneous state

    ViewCurveAtts = ViewCurveAttributes()
    ViewCurveAtts.domainCoords = (0, 1)
    ViewCurveAtts.rangeCoords = (0, 1)
    ViewCurveAtts.viewportCoords = (0.2, 0.95, 0.15, 0.95)
    ViewCurveAtts.domainScale = ViewCurveAtts.LINEAR  # LINEAR, LOG
    ViewCurveAtts.rangeScale = ViewCurveAtts.LINEAR  # LINEAR, LOG
    SetViewCurve(ViewCurveAtts)


    # Logging for SetAnnotationObjectOptions is not implemented yet.
    AnnotationAtts = AnnotationAttributes()
    AnnotationAtts.axes3D.visible = 1
    AnnotationAtts.axes3D.autoSetTicks = 1
    AnnotationAtts.axes3D.autoSetScaling = 1
    AnnotationAtts.axes3D.lineWidth = 0
    AnnotationAtts.axes3D.tickLocation = AnnotationAtts.axes3D.Inside  # Inside, Outside, Both
    AnnotationAtts.axes3D.axesType = AnnotationAtts.axes3D.ClosestTriad  # ClosestTriad, FurthestTriad, OutsideEdges, StaticTriad, StaticEdges
    AnnotationAtts.axes3D.triadFlag = 1
    AnnotationAtts.axes3D.bboxFlag = 1
    AnnotationAtts.axes3D.xAxis.title.visible = 0
    AnnotationAtts.axes3D.xAxis.title.font.font = AnnotationAtts.axes3D.xAxis.title.font.Arial  # Arial, Courier, Times
    AnnotationAtts.axes3D.xAxis.title.font.scale = 1
    AnnotationAtts.axes3D.xAxis.title.font.useForegroundColor = 1
    AnnotationAtts.axes3D.xAxis.title.font.color = (0, 0, 0, 255)
    AnnotationAtts.axes3D.xAxis.title.font.bold = 0
    AnnotationAtts.axes3D.xAxis.title.font.italic = 0
    AnnotationAtts.axes3D.xAxis.title.userTitle = 0
    AnnotationAtts.axes3D.xAxis.title.userUnits = 0
    AnnotationAtts.axes3D.xAxis.title.title = "X-Axis"
    AnnotationAtts.axes3D.xAxis.title.units = ""
    AnnotationAtts.axes3D.xAxis.label.visible = 1
    AnnotationAtts.axes3D.xAxis.label.font.font = AnnotationAtts.axes3D.xAxis.label.font.Arial  # Arial, Courier, Times
    AnnotationAtts.axes3D.xAxis.label.font.scale = 1
    AnnotationAtts.axes3D.xAxis.label.font.useForegroundColor = 1
    AnnotationAtts.axes3D.xAxis.label.font.color = (0, 0, 0, 255)
    AnnotationAtts.axes3D.xAxis.label.font.bold = 0
    AnnotationAtts.axes3D.xAxis.label.font.italic = 0
    AnnotationAtts.axes3D.xAxis.label.scaling = 0
    AnnotationAtts.axes3D.xAxis.tickMarks.visible = 1
    AnnotationAtts.axes3D.xAxis.tickMarks.majorMinimum = 0
    AnnotationAtts.axes3D.xAxis.tickMarks.majorMaximum = 1
    AnnotationAtts.axes3D.xAxis.tickMarks.minorSpacing = 0.02
    AnnotationAtts.axes3D.xAxis.tickMarks.majorSpacing = 0.2
    AnnotationAtts.axes3D.xAxis.grid = 0
    AnnotationAtts.axes3D.yAxis.title.visible = 0
    AnnotationAtts.axes3D.yAxis.title.font.font = AnnotationAtts.axes3D.yAxis.title.font.Arial  # Arial, Courier, Times
    AnnotationAtts.axes3D.yAxis.title.font.scale = 1
    AnnotationAtts.axes3D.yAxis.title.font.useForegroundColor = 1
    AnnotationAtts.axes3D.yAxis.title.font.color = (0, 0, 0, 255)
    AnnotationAtts.axes3D.yAxis.title.font.bold = 0
    AnnotationAtts.axes3D.yAxis.title.font.italic = 0
    AnnotationAtts.axes3D.yAxis.title.userTitle = 0
    AnnotationAtts.axes3D.yAxis.title.userUnits = 0
    AnnotationAtts.axes3D.yAxis.title.title = "Y-Axis"
    AnnotationAtts.axes3D.yAxis.title.units = ""
    AnnotationAtts.axes3D.yAxis.label.visible = 1
    AnnotationAtts.axes3D.yAxis.label.font.font = AnnotationAtts.axes3D.yAxis.label.font.Arial  # Arial, Courier, Times
    AnnotationAtts.axes3D.yAxis.label.font.scale = 1
    AnnotationAtts.axes3D.yAxis.label.font.useForegroundColor = 1
    AnnotationAtts.axes3D.yAxis.label.font.color = (0, 0, 0, 255)
    AnnotationAtts.axes3D.yAxis.label.font.bold = 0
    AnnotationAtts.axes3D.yAxis.label.font.italic = 0
    AnnotationAtts.axes3D.yAxis.label.scaling = 0
    AnnotationAtts.axes3D.yAxis.tickMarks.visible = 1
    AnnotationAtts.axes3D.yAxis.tickMarks.majorMinimum = 0
    AnnotationAtts.axes3D.yAxis.tickMarks.majorMaximum = 1
    AnnotationAtts.axes3D.yAxis.tickMarks.minorSpacing = 0.02
    AnnotationAtts.axes3D.yAxis.tickMarks.majorSpacing = 0.2
    AnnotationAtts.axes3D.yAxis.grid = 0
    AnnotationAtts.axes3D.zAxis.title.visible = 0
    AnnotationAtts.axes3D.zAxis.title.font.font = AnnotationAtts.axes3D.zAxis.title.font.Arial  # Arial, Courier, Times
    AnnotationAtts.axes3D.zAxis.title.font.scale = 1
    AnnotationAtts.axes3D.zAxis.title.font.useForegroundColor = 1
    AnnotationAtts.axes3D.zAxis.title.font.color = (0, 0, 0, 255)
    AnnotationAtts.axes3D.zAxis.title.font.bold = 0
    AnnotationAtts.axes3D.zAxis.title.font.italic = 0
    AnnotationAtts.axes3D.zAxis.title.userTitle = 0
    AnnotationAtts.axes3D.zAxis.title.userUnits = 0
    AnnotationAtts.axes3D.zAxis.title.title = "Z-Axis"
    AnnotationAtts.axes3D.zAxis.title.units = ""
    AnnotationAtts.axes3D.zAxis.label.visible = 1
    AnnotationAtts.axes3D.zAxis.label.font.font = AnnotationAtts.axes3D.zAxis.label.font.Arial  # Arial, Courier, Times
    AnnotationAtts.axes3D.zAxis.label.font.scale = 1
    AnnotationAtts.axes3D.zAxis.label.font.useForegroundColor = 1
    AnnotationAtts.axes3D.zAxis.label.font.color = (0, 0, 0, 255)
    AnnotationAtts.axes3D.zAxis.label.font.bold = 0
    AnnotationAtts.axes3D.zAxis.label.font.italic = 0
    AnnotationAtts.axes3D.zAxis.label.scaling = 0
    AnnotationAtts.axes3D.zAxis.tickMarks.visible = 1
    AnnotationAtts.axes3D.zAxis.tickMarks.majorMinimum = 0
    AnnotationAtts.axes3D.zAxis.tickMarks.majorMaximum = 1
    AnnotationAtts.axes3D.zAxis.tickMarks.minorSpacing = 0.02
    AnnotationAtts.axes3D.zAxis.tickMarks.majorSpacing = 0.2
    AnnotationAtts.axes3D.zAxis.grid = 0
    AnnotationAtts.axes3D.setBBoxLocation = 0
    AnnotationAtts.axes3D.bboxLocation = (0, 1, 0, 1, 0, 1)
    AnnotationAtts.axes3D.triadColor = (0, 0, 0)
    AnnotationAtts.axes3D.triadLineWidth = 0
    AnnotationAtts.axes3D.triadFont = 0
    AnnotationAtts.axes3D.triadBold = 1
    AnnotationAtts.axes3D.triadItalic = 1
    AnnotationAtts.axes3D.triadSetManually = 0
    AnnotationAtts.userInfoFlag = 0
    AnnotationAtts.userInfoFont.font = AnnotationAtts.userInfoFont.Arial  # Arial, Courier, Times
    AnnotationAtts.userInfoFont.scale = 1
    AnnotationAtts.userInfoFont.useForegroundColor = 1
    AnnotationAtts.userInfoFont.color = (0, 0, 0, 255)
    AnnotationAtts.userInfoFont.bold = 0
    AnnotationAtts.userInfoFont.italic = 0
    AnnotationAtts.databaseInfoFlag = 1
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
    AnnotationAtts.legendInfoFlag = 1
    AnnotationAtts.backgroundColor = (255, 255, 255, 255)
    AnnotationAtts.foregroundColor = (0, 0, 0, 255)
    AnnotationAtts.gradientBackgroundStyle = AnnotationAtts.Radial  # TopToBottom, BottomToTop, LeftToRight, RightToLeft, Radial
    AnnotationAtts.gradientColor1 = (0, 0, 255, 255)
    AnnotationAtts.gradientColor2 = (0, 0, 0, 255)
    AnnotationAtts.backgroundMode = AnnotationAtts.Solid  # Solid, Gradient, Image, ImageSphere
    AnnotationAtts.backgroundImage = ""
    AnnotationAtts.imageRepeatX = 1
    AnnotationAtts.imageRepeatY = 1
    AnnotationAtts.axesArray.visible = 1
    AnnotationAtts.axesArray.ticksVisible = 1
    AnnotationAtts.axesArray.autoSetTicks = 1
    AnnotationAtts.axesArray.autoSetScaling = 1
    AnnotationAtts.axesArray.lineWidth = 0
    AnnotationAtts.axesArray.axes.title.visible = 1
    AnnotationAtts.axesArray.axes.title.font.font = AnnotationAtts.axesArray.axes.title.font.Arial  # Arial, Courier, Times
    AnnotationAtts.axesArray.axes.title.font.scale = 1
    AnnotationAtts.axesArray.axes.title.font.useForegroundColor = 1
    AnnotationAtts.axesArray.axes.title.font.color = (0, 0, 0, 255)
    AnnotationAtts.axesArray.axes.title.font.bold = 0
    AnnotationAtts.axesArray.axes.title.font.italic = 0
    AnnotationAtts.axesArray.axes.title.userTitle = 0
    AnnotationAtts.axesArray.axes.title.userUnits = 0
    AnnotationAtts.axesArray.axes.title.title = ""
    AnnotationAtts.axesArray.axes.title.units = ""
    AnnotationAtts.axesArray.axes.label.visible = 1
    AnnotationAtts.axesArray.axes.label.font.font = AnnotationAtts.axesArray.axes.label.font.Arial  # Arial, Courier, Times
    AnnotationAtts.axesArray.axes.label.font.scale = 1
    AnnotationAtts.axesArray.axes.label.font.useForegroundColor = 1
    AnnotationAtts.axesArray.axes.label.font.color = (0, 0, 0, 255)
    AnnotationAtts.axesArray.axes.label.font.bold = 0
    AnnotationAtts.axesArray.axes.label.font.italic = 0
    AnnotationAtts.axesArray.axes.label.scaling = 0
    AnnotationAtts.axesArray.axes.tickMarks.visible = 1
    AnnotationAtts.axesArray.axes.tickMarks.majorMinimum = 0
    AnnotationAtts.axesArray.axes.tickMarks.majorMaximum = 1
    AnnotationAtts.axesArray.axes.tickMarks.minorSpacing = 0.02
    AnnotationAtts.axesArray.axes.tickMarks.majorSpacing = 0.2
    AnnotationAtts.axesArray.axes.grid = 0
    SetAnnotationAttributes(AnnotationAtts)
    return 0

def getlaststep(fname):
  ### open file
  f=open(fname)
  ### Read last line in a string
  lastline = f.readlines()[-1]
  laststep = lastline.rsplit()[0] 
  return(int(laststep))


def draw():
    AddPlot("Pseudocolor", "Damage", 1, 1)
    AddOperator("Isovolume", 1)
    SetActivePlots(0)
    SetActivePlots(0)
    IsovolumeAtts = IsovolumeAttributes()
    IsovolumeAtts.lbound = 0.95
    IsovolumeAtts.ubound = 1e+37
    IsovolumeAtts.variable = "Damage"
    SetOperatorOptions(IsovolumeAtts, 0, 1)

    AddOperator("Smooth", 0)
    SmoothOperatorAtts = SmoothOperatorAttributes()
    SmoothOperatorAtts.numIterations = 40
    SmoothOperatorAtts.relaxationFactor = 0.1
    SmoothOperatorAtts.convergence = 0
    SmoothOperatorAtts.maintainFeatures = 0
    SmoothOperatorAtts.featureAngle = 45
    SmoothOperatorAtts.edgeAngle = 15
    SmoothOperatorAtts.smoothBoundaries = 0
    SetOperatorOptions(SmoothOperatorAtts, 1, 0)

    AddPlot("Contour", "Temperature", 1, 0)
    SetActivePlots(1)
    SetActivePlots(1)
    ContourAtts = ContourAttributes()
    ContourAtts.defaultPalette.GetControlPoints(0).colors = (255, 0, 0, 255)
    ContourAtts.defaultPalette.GetControlPoints(0).position = 0
    ContourAtts.defaultPalette.GetControlPoints(1).colors = (0, 255, 0, 255)
    ContourAtts.defaultPalette.GetControlPoints(1).position = 0.034
    ContourAtts.defaultPalette.GetControlPoints(2).colors = (0, 0, 255, 255)
    ContourAtts.defaultPalette.GetControlPoints(2).position = 0.069
    ContourAtts.defaultPalette.GetControlPoints(3).colors = (0, 255, 255, 255)
    ContourAtts.defaultPalette.GetControlPoints(3).position = 0.103
    ContourAtts.defaultPalette.GetControlPoints(4).colors = (255, 0, 255, 255)
    ContourAtts.defaultPalette.GetControlPoints(4).position = 0.138
    ContourAtts.defaultPalette.GetControlPoints(5).colors = (255, 255, 0, 255)
    ContourAtts.defaultPalette.GetControlPoints(5).position = 0.172
    ContourAtts.defaultPalette.GetControlPoints(6).colors = (255, 135, 0, 255)
    ContourAtts.defaultPalette.GetControlPoints(6).position = 0.207
    ContourAtts.defaultPalette.GetControlPoints(7).colors = (255, 0, 135, 255)
    ContourAtts.defaultPalette.GetControlPoints(7).position = 0.241
    ContourAtts.defaultPalette.GetControlPoints(8).colors = (168, 168, 168, 255)
    ContourAtts.defaultPalette.GetControlPoints(8).position = 0.276
    ContourAtts.defaultPalette.GetControlPoints(9).colors = (255, 68, 68, 255)
    ContourAtts.defaultPalette.GetControlPoints(9).position = 0.31
    ContourAtts.defaultPalette.GetControlPoints(10).colors = (99, 255, 99, 255)
    ContourAtts.defaultPalette.GetControlPoints(10).position = 0.345
    ContourAtts.defaultPalette.GetControlPoints(11).colors = (99, 99, 255, 255)
    ContourAtts.defaultPalette.GetControlPoints(11).position = 0.379
    ContourAtts.defaultPalette.GetControlPoints(12).colors = (40, 165, 165, 255)
    ContourAtts.defaultPalette.GetControlPoints(12).position = 0.414
    ContourAtts.defaultPalette.GetControlPoints(13).colors = (255, 99, 255, 255)
    ContourAtts.defaultPalette.GetControlPoints(13).position = 0.448
    ContourAtts.defaultPalette.GetControlPoints(14).colors = (255, 255, 99, 255)
    ContourAtts.defaultPalette.GetControlPoints(14).position = 0.483
    ContourAtts.defaultPalette.GetControlPoints(15).colors = (255, 170, 99, 255)
    ContourAtts.defaultPalette.GetControlPoints(15).position = 0.517
    ContourAtts.defaultPalette.GetControlPoints(16).colors = (170, 79, 255, 255)
    ContourAtts.defaultPalette.GetControlPoints(16).position = 0.552
    ContourAtts.defaultPalette.GetControlPoints(17).colors = (150, 0, 0, 255)
    ContourAtts.defaultPalette.GetControlPoints(17).position = 0.586
    ContourAtts.defaultPalette.GetControlPoints(18).colors = (0, 150, 0, 255)
    ContourAtts.defaultPalette.GetControlPoints(18).position = 0.621
    ContourAtts.defaultPalette.GetControlPoints(19).colors = (0, 0, 150, 255)
    ContourAtts.defaultPalette.GetControlPoints(19).position = 0.655
    ContourAtts.defaultPalette.GetControlPoints(20).colors = (0, 109, 109, 255)
    ContourAtts.defaultPalette.GetControlPoints(20).position = 0.69
    ContourAtts.defaultPalette.GetControlPoints(21).colors = (150, 0, 150, 255)
    ContourAtts.defaultPalette.GetControlPoints(21).position = 0.724
    ContourAtts.defaultPalette.GetControlPoints(22).colors = (150, 150, 0, 255)
    ContourAtts.defaultPalette.GetControlPoints(22).position = 0.759
    ContourAtts.defaultPalette.GetControlPoints(23).colors = (150, 84, 0, 255)
    ContourAtts.defaultPalette.GetControlPoints(23).position = 0.793
    ContourAtts.defaultPalette.GetControlPoints(24).colors = (160, 0, 79, 255)
    ContourAtts.defaultPalette.GetControlPoints(24).position = 0.828
    ContourAtts.defaultPalette.GetControlPoints(25).colors = (255, 104, 28, 255)
    ContourAtts.defaultPalette.GetControlPoints(25).position = 0.862
    ContourAtts.defaultPalette.GetControlPoints(26).colors = (0, 170, 81, 255)
    ContourAtts.defaultPalette.GetControlPoints(26).position = 0.897
    ContourAtts.defaultPalette.GetControlPoints(27).colors = (68, 255, 124, 255)
    ContourAtts.defaultPalette.GetControlPoints(27).position = 0.931
    ContourAtts.defaultPalette.GetControlPoints(28).colors = (0, 130, 255, 255)
    ContourAtts.defaultPalette.GetControlPoints(28).position = 0.966
    ContourAtts.defaultPalette.GetControlPoints(29).colors = (130, 0, 255, 255)
    ContourAtts.defaultPalette.GetControlPoints(29).position = 1
    ContourAtts.defaultPalette.smoothing = ContourAtts.defaultPalette.None  # None, Linear, CubicSpline
    ContourAtts.defaultPalette.equalSpacingFlag = 1
    ContourAtts.defaultPalette.discreteFlag = 1
    ContourAtts.defaultPalette.categoryName = "Standard"
    ContourAtts.changedColors = ()
    ContourAtts.colorType = ContourAtts.ColorByColorTable  # ColorBySingleColor, ColorByMultipleColors, ColorByColorTable
    ContourAtts.colorTableName = "hot_and_cold"
    ContourAtts.invertColorTable = 0
    ContourAtts.legendFlag = 0
    ContourAtts.lineWidth = 0
    ContourAtts.singleColor = (255, 0, 0, 255)
    ContourAtts.SetMultiColor(0, (255, 0, 0, 255))
    ContourAtts.SetMultiColor(1, (0, 255, 0, 255))
    ContourAtts.SetMultiColor(2, (0, 0, 255, 255))
    ContourAtts.SetMultiColor(3, (0, 255, 255, 255))
    ContourAtts.SetMultiColor(4, (255, 0, 255, 255))
    ContourAtts.SetMultiColor(5, (255, 255, 0, 255))
    ContourAtts.SetMultiColor(6, (255, 135, 0, 255))
    ContourAtts.SetMultiColor(7, (255, 0, 135, 255))
    ContourAtts.SetMultiColor(8, (168, 168, 168, 255))
    ContourAtts.SetMultiColor(9, (255, 68, 68, 255))
    ContourAtts.contourNLevels = 10
    ContourAtts.contourValue = ()
    ContourAtts.contourPercent = ()
    ContourAtts.contourMethod = ContourAtts.Level  # Level, Value, Percent
    ContourAtts.minFlag = 0
    ContourAtts.maxFlag = 1
    ContourAtts.min = 0
    ContourAtts.max = 0.1
    ContourAtts.scaling = ContourAtts.Linear  # Linear, Log
    ContourAtts.wireframe = 0
    SetPlotOptions(ContourAtts)
    AddOperator("Slice", 0)
    SliceAtts = SliceAttributes()
    SliceAtts.originType = SliceAtts.Intercept  # Point, Intercept, Percent, Zone, Node
    SliceAtts.originPoint = (0, 0, 0)
    SliceAtts.originIntercept = 0
    SliceAtts.originPercent = 0
    SliceAtts.originZone = 0
    SliceAtts.originNode = 0
    SliceAtts.normal = (0, 0, 1)
    SliceAtts.axisType = SliceAtts.ZAxis  # XAxis, YAxis, ZAxis, Arbitrary, ThetaPhi
    SliceAtts.upAxis = (0, 1, 0)
    SliceAtts.project2d = 0
    SliceAtts.interactive = 0
    SliceAtts.flip = 0
    SliceAtts.originZoneDomain = 0
    SliceAtts.originNodeDomain = 0
    SliceAtts.meshName = "Mesh"
    SliceAtts.theta = 0
    SliceAtts.phi = 90
    SetOperatorOptions(SliceAtts, 0, 0)

    SetView()

    RenderingAtts = RenderingAttributes()
    RenderingAtts.antialiasing = 1
    RenderingAtts.orderComposite = 1
    RenderingAtts.depthCompositeThreads = 2
    RenderingAtts.depthCompositeBlocking = 65536
    RenderingAtts.alphaCompositeThreads = 2
    RenderingAtts.alphaCompositeBlocking = 65536
    RenderingAtts.depthPeeling = 0
    RenderingAtts.occlusionRatio = 0
    RenderingAtts.numberOfPeels = 16
    RenderingAtts.multiresolutionMode = 0
    RenderingAtts.multiresolutionCellSize = 0.002
    RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
    RenderingAtts.stereoRendering = 0
    RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
    RenderingAtts.notifyForEachRender = 0
    RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
    RenderingAtts.scalableAutoThreshold = 2000000
    RenderingAtts.specularFlag = 0
    RenderingAtts.specularCoeff = 0.6
    RenderingAtts.specularPower = 10
    RenderingAtts.specularColor = (255, 255, 255, 255)
    RenderingAtts.doShadowing = 0
    RenderingAtts.shadowStrength = 0.5
    RenderingAtts.doDepthCueing = 0
    RenderingAtts.depthCueingAutomatic = 1
    RenderingAtts.startCuePoint = (-10, 0, 0)
    RenderingAtts.endCuePoint = (10, 0, 0)
    RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
    RenderingAtts.colorTexturingFlag = 1
    RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
    RenderingAtts.compactDomainsAutoThreshold = 256
    RenderingAtts.osprayRendering = 0
    RenderingAtts.ospraySPP = 1
    RenderingAtts.osprayAO = 0
    RenderingAtts.osprayShadows = 0
    SetRenderingAttributes(RenderingAtts)

    DrawPlots()
    return 0
    
def SetView():
    View3DAtts = View3DAttributes()
    View3DAtts.viewNormal = (-0.711164, -0.407435, 0.572924)
    View3DAtts.focus = (0, 0, 0)
    View3DAtts.viewUp = (0.382339, 0.459737, 0.801535)
    View3DAtts.viewAngle = 30
    View3DAtts.parallelScale = 35.3571
    View3DAtts.nearPlane = -70.7141
    View3DAtts.farPlane = 70.7141
    View3DAtts.imagePan = (0.194787, 0.123699)
    View3DAtts.imageZoom = 6.54872
    View3DAtts.perspective = 1
    View3DAtts.eyeAngle = 2
    View3DAtts.centerOfRotationSet = 0
    View3DAtts.centerOfRotation = (0, 0, 0)
    View3DAtts.axis3DScaleFlag = 0
    View3DAtts.axis3DScales = (1, 1, 1)
    View3DAtts.shear = (0, 0, 1)
    View3DAtts.windowValid = 1
    SetView3D(View3DAtts)

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
    movName    = os.path.join(rootdir,'{0}.mp4'.format(prefix))

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

    draw()

    SetAnnotations()
    DrawPlots()


    geometry = (4096,4096)

    if options.bg == 'white':
        setBGWhite()
    else:
        setBGBlack()

    for step in range(stepmin-1,stepmax):
        SetTimeSliderState(step)
        filename = '{basename}-{step:04d}'.format(basename = os.path.join(rootdir,'Frames',prefix),step=step,**options.__dict__)
        status = savePNG(filename,geometry)

    DeleteAllPlots()
    CloseDatabase(MyDatabase)

    cmd_exists = lambda x: any(os.access(os.path.join(path, x), os.X_OK) for path in os.environ["PATH"].split(os.pathsep))    
    #cmd = 'ffmpeg -y -i Frames/{prefix}-%04d.png -vcodec mjpeg -qscale 1  {prefix}.avi'.format(prefix=prefix)
    cmd = 'ffmpeg -y -i {framesDir}/{prefix}-%04d.png -f mp4 -vcodec h264 -pix_fmt yuv420p  {movName}'.format(framesDir=framesDir,prefix=prefix,movName=movName,**options.__dict__)
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
    parser.add_argument('--step_min',type=int,default=1)
    parser.add_argument('--step_max',type=int,default=0)
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

