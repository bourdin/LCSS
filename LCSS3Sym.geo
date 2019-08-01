SetFactory("OpenCASCADE");
width   = {width};
height  = {height};
hf      = {hf};
hc      = {hc};
r       = {r};
lc      = {lc};
lf      = {lf};
epsc    = height/1000;

Point(1)  = {{-width/2+lc,0,0,hf}};
Point(2)  = {{-width/2,-epsc,0,hf}};
Point(3)  = {{-width/2,-height/2,0,hf}};
Point(4)  = {{width/2,-height/2,0,hf}};
Point(5)  = {{width/2,0,0,hf}};
Point(6)  = {{-width/2+lf,0,0,hf}};

For i In {{1:6}}
        Line(i) = {{i,i%6+1}};
EndFor
Line Loop(1) = {{1:6}};
Plane Surface(1) = {{1}};


// Sizing function:
Mesh.CharacteristicLengthFromPoints = 0;
Mesh.CharacteristicLengthFromCurvature = 0;
Mesh.CharacteristicLengthExtendFromBoundary = 0;

Field[1]           = Distance;
Field[1].EdgesList = {{1,6}};

Field[2]         = Threshold;
Field[2].IField  = 1;
Field[2].LcMin   = hf;
Field[2].LcMax   = hc;
Field[2].DistMin = r;
Field[2].DistMax = 3*r;

Background Field = 2;

Physical Surface(1) = {{1}};
// Top 
Physical Line(10)   = {{3}};
//Left 
Physical Line(11)   = {{2}};
//Right
Physical Line(12)   = {{4}};
// Crack bottom
Physical Line(20)   = {{1}};
// Logical crack
Physical Line(21)   = {{6}};
// Symmetry axis
Physical Line(22)   = {{5}};

// Lower left corner
Physical Point(300) = {{3}};
// Middle right point
Physical Point(301) = {{5}};
//Crack tip
Physical Point(400) = {{1}};


