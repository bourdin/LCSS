SetFactory("OpenCASCADE");
width   = {width};
height  = {height};
hf      = {hf};
hc      = {hc};
r       = {criticalRadius};
lc      = {lc};
beamPos = {position};
epsc    = height/1000;

Point(1)  = {{-width/2+lc,0,0,hf}};
Point(2)  = {{-width/2,-epsc,0,hf}};
Point(3)  = {{-width/2,-height/2,0,hf}};
Point(4)  = {{width/2,-height/2,0,hf}};
Point(5)  = {{width/2,height/2,0,hf}};
Point(6)  = {{-width/2,height/2,0,hf}};
Point(7)  = {{-width/2,epsc,0,hf}};

For i In {{1:7}}
        Line(i) = {{i,i%7+1}};
EndFor
Line Loop(1) = {{1:7}};
Plane Surface(1) = {{1}};

Point(10)    = {{beamPos,0,0,hf}};

// Sizing function:
Mesh.CharacteristicLengthFromPoints = 0;
Mesh.CharacteristicLengthFromCurvature = 0;
Mesh.CharacteristicLengthExtendFromBoundary = 0;

Field[1]           = Distance;
Field[1].NodesList = {{1,10}};

Field[2]         = Threshold;
Field[2].IField  = 1;
Field[2].LcMin   = hf;
Field[2].LcMax   = hc;
Field[2].DistMin = r;
Field[2].DistMax = 3*r;

Background Field = 2;

Physical Surface(1) = {{1}};
Physical Line(10)   = {{2,3,4,5,6}};
Physical Line(20)   = {{1}};
Physical Line(21)   = {{7}};

Physical Point(300) = {{3}};
Physical Point(301) = {{4}};
Physical Point(302) = {{5}};


