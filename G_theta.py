# G_theta
# 4, Febuary  2015
# Erwan Tanne   (erwan.tanne@gmail.com)


#visit -cli -nowin -s G_theta.py 
def computeGTheta(rootdir):
    import json
    import os.path
    with open(os.path.join(rootdir,'00_INFO.json')) as fp:
        options = json.load(fp)

        MyDatabase = os.path.join(rootdir,'{prefix:s}_out.gen'.format(**options))
        OpenDatabase(MyDatabase)

        #Define Expression
        DefineScalarExpression("X", 'coord(Mesh)[0]+{width:e}/2.-{lc:e}'.format(**options))
        DefineScalarExpression("Y", 'coord(Mesh)[1]')
        DefineScalarExpression("R0", "min({r:e},max(sqrt(X*X+Y*Y),{r:e}/2))".format(**options))

        DefineVectorExpression("Displacement_2D", "{Displacement_X,Displacement_Y}")
        DefineTensorExpression("GRAD_U", "{{gradient(Displacement_2D[0])[0],gradient(Displacement_2D[0])[1]},{gradient(Displacement_2D[1])[0],gradient(Displacement_2D[1])[1]}}")
        DefineTensorExpression("EPS_2D", "0.5*(GRAD_U + transpose(GRAD_U))")
        DefineTensorExpression("STRESS_2D", "{{ Stress_XX, Stress_XY},{Stress_XY,Stress_YY}}")

        DefineScalarExpression("Theta_scal", "0.5*(1+cos(atan(1)*4.*(2.*R0-{r:e})/{r:e}))".format(**options))
        DefineVectorExpression("Theta_vec", '{Theta_scal, 0.}')
        DefineTensorExpression("GRAD_Theta_vec", "{{gradient(Theta_vec[0])[0],gradient(Theta_vec[0])[1]},{gradient(Theta_vec[1])[0],gradient(Theta_vec[1])[1]}}")

        DefineScalarExpression("G_theta", "trace(STRESS_2D*(GRAD_U*GRAD_Theta_vec))-.5*trace(STRESS_2D*EPS_2D)*divergence(Theta_vec)")

        #Draw G_theta
        AddPlot("Pseudocolor", "G_theta")
        DrawPlots()
        SuppressQueryOutputOn()
        Query("Average Value")
        Gtheta = GetQueryOutputValue() * options['width'] * options['height']

        DeleteActivePlots()
        CloseDatabase(MyDatabase)
        return options['lc'],Gtheta


if __name__ == "__main__":
    import sys
    f = open('Gtheta.txt','a')
    f.write('#path l G\n')
    for d in sys.argv[1:]:
        li,Gi = computeGTheta(d)
        f.write("{0} {1} {2}\n".format(d, li, Gi))
        f.flush()
    f.close()
    exit()