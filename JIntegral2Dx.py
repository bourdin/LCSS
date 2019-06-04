from visit import *

def mytrapz(xy):
    trapz = 0
    for i in range(len(xy)/2-1):
        trapz += (xy[2*i+2]-xy[2*i])*(xy[2*i+1]+xy[2*i+3])
    trapz = trapz*.5
    return trapz



def computeJ(rootdir,nint=[100,100]):
    import json
    import os
    import os.path
    import shutil
    import math

    ##  
    ## Open the database
    ##
    with open(os.path.join(rootdir,'00_INFO.json')) as fp:
        options = json.load(fp)

        MyDatabase = os.path.join(rootdir,'{prefix:s}_out.gen'.format(**options))
        OpenDatabase(MyDatabase)
    
        DefineVectorExpression("dUx","gradient(<Displacement_X>)")
        DefineVectorExpression("dUy","gradient(<Displacement_Y>)")
        DefineScalarExpression("EnergyDensity","(<Stress_XX> * dUx[0] + <Stress_YY> * dUy[1] + <Stress_XY> * (dUx[1]+dUy[0])) * .5 ")
        DefineScalarExpression("C11","EnergyDensity - <Stress_XX> * dUx[0] - <Stress_XY> * dUy[0]")
        DefineScalarExpression("C21","              - <Stress_XY> * dUx[0] - <Stress_YY> * dUy[0]")

        AddPlot("Pseudocolor","Damage")
        DrawPlots()
        SuppressQueryOutputOn()

        BB = [-options['width']/2+options['lc']-options['r'],-options['r'],2.*options['r'],2.*options['r']]
        nintx = nint[0]
        ninty = nint[1]

        ChangeActivePlotsVar("C11")
        DrawPlots()
        Lineout(start_point = (BB[0],BB[1]+BB[3],0), 
                end_point   = (BB[0],BB[1],      0)) 
        SetActiveWindow(2)
        info = GetPlotInformation()
        Cleft=-mytrapz(info["Curve"])
        DeleteActivePlots()

        ### C e1 . n right edge
        SetActiveWindow(1)
        Lineout(start_point = (BB[0]+BB[2],BB[1],      0), 
                end_point   = (BB[0]+BB[2],BB[1]+BB[3],0)) 
        SetActiveWindow(2)
        info = GetPlotInformation()
        Cright=mytrapz(info["Curve"])
        DeleteActivePlots()

        ### C e1 . n top edge
        SetActiveWindow(1)
        ### -C e1 . n left edge
        ChangeActivePlotsVar("C21")
        Lineout(start_point = (BB[0]+BB[2],BB[1]+BB[3],0), 
                end_point   = (BB[0]      ,BB[1]+BB[3],0))
        SetActiveWindow(2)
        info = GetPlotInformation()
        Ctop = mytrapz(info["Curve"])
        DeleteActivePlots()

        ### C e1 . n bottom edge
        SetActiveWindow(1)
        Lineout(start_point = (BB[0]      ,BB[1],0), 
                end_point   = (BB[0]+BB[2],BB[1],0)) 
        SetActiveWindow(2)
        info = GetPlotInformation()
        Cbot = -mytrapz(info["Curve"])
        DeleteActivePlots()

        print "Jint = %e  ( = %e %+e %+e %+e)"%(Cleft+Ctop+Cright+Cbot,Cleft,Ctop,Cright,Cbot)

        SetActiveWindow(1)
        DeleteAllPlots()
        SetActiveWindow(2)
        DeleteAllPlots()
        DeleteWindow()
        CloseDatabase(MyDatabase)
        return options['lc'],Cleft+Ctop+Cright+Cbot

if __name__ == "__main__":
    import sys  
    import os.path

    f = open('Jintegral.txt','a')
    f.write('#path l G\n')
    for d in sys.argv[1:]:
        li,Gi = computeJ(d)
        f.write("{0} {1} {2}\n".format(d, li, Gi))
        f.flush()
    f.close()

    exit()

    
