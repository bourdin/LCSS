SetFactory("OpenCASCADE");
width   = {width};
height  = {height};
hf      = {hf};
hc      = {hc};
r       = {r};
lc      = {lc};
lf      = {lf};
epsc    = height/1000;
beamPos = {position};

Point(1)  = {{-width/2+lc,0,0,hf}};
Point(2)  = {{-width/2,-epsc,0,hf}};
Point(3)  = {{-width/2,-height/2,0,hf}};
Point(4)  = {{width/2,-height/2,0,hf}};
Point(5)  = {{width/2,0,0,hf}};
Point(6)  = {{width/2,height/2,0,hf}};
Point(7)  = {{-width/2,height/2,0,hf}};
Point(8)  = {{-width/2,epsc,0,hf}};
Point(10) = {{-width/2+lf,0,0,hf}};
Point(99) = {{beamPos,0,0,hf}};
For i In {{1:8}}
        Line(i) = {{i,i%8+1}};
EndFor
Line(9)  = {{1, 10}};
Line(10) = {{10, 5}};
Line Loop(1) = {{1,2,3,4,-10,-9}};
Plane Surface(1) = {{1}};
Line Loop(2) = {{9,10,5,6,7,8}};
Plane Surface(2) = {{2}};

Line(99) = {{1,99}};

// Sizing function:
Mesh.CharacteristicLengthFromPoints = 0;
Mesh.CharacteristicLengthFromCurvature = 0;
Mesh.CharacteristicLengthExtendFromBoundary = 0;

Field[1]           = Distance;
Field[1].EdgesList = {{1,8,9,99}};

Field[2]         = Threshold;
Field[2].IField  = 1;
Field[2].LcMin   = hf;
Field[2].LcMax   = hc;
Field[2].DistMin = r;
Field[2].DistMax = 3*r;

Background Field = 2;

Physical Surface(1) = {{1}};
Physical Surface(2) = {{2}};
// Top bottom
Physical Line(10)   = {{3,6}};
//Left 
Physical Line(11)   = {{2,7}};
//Right
Physical Line(12)   = {{4, 5}};
// Crack bottom
Physical Line(20)   = {{1}};
// Crack top
Physical Line(21)   = {{8}};
// Logical crack
Physical Line(30)   = {{9}};

// Lower left corner
Physical Point(300) = {{3}};
// Middle right point
Physical Point(301) = {{5}};
//Upper left corner
Physical Point(302) = {{7}};


