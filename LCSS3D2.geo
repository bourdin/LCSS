SetFactory("OpenCASCADE");
//width   = {width};
//height  = {height};
//depth   = {depth};
//hf      = {hf};
//hc      = {hc};
//r       = {r};
//lc      = {lc};
//lf      = {lf};
//epsc    = height/1000;


r0       = 1.e-4;
width    = 50;
height   = 50;
depth    = 0.7e-3/r0;
hf       = depth/50;
hc       = depth/3;
hBrittle = depth/2;
wBrittle = 2*width/3;
lc       = 2;
lf       = 4;
epsc     = hBrittle/10;

Printf("Domain size: %g x %g x %g",width,height,depth);
Printf("Using hf=%g, hc=%g",hf,hc);

//Mesh.Algorithm               = 6;
//Mesh.Algorithm3D             = 1;
Mesh.Format                  = 1;
Mesh.MshFileVersion          = 2;
Mesh.CharacteristicLengthFromPoints = 0;
Mesh.CharacteristicLengthFromCurvature = 0;
Mesh.CharacteristicLengthExtendFromBoundary = 0;
//Mesh.OptimizeNetgen          = 1;
Mesh.Optimize                = 1;


elasticRegion = newv;
Box(elasticRegion) = {-width/2,-height/2,-depth,width,height,depth};

// The beam and crack must remain in the brittleRegion
brittleRegion = newv;
Box(brittleRegion) = {-width/2,-hBrittle/2,-depth,wBrittle,hBrittle,depth};
out[] = BooleanFragments{ Volume{elasticRegion}; Delete; }
                        { Volume{brittleRegion}; Delete; };


// //Printing the fragment command helps identifying the inside from the outside. 
//Printf("out[0] %g",out[0]);
//Printf("out[1] %g",out[1]);
//Printf("out[2] %g",out[2]);

brittleRegion = out[0];
elasticRegion = out[1];

// Initial Physical crack
physicalCrackC = newc;
Ellipse(physicalCrackC) = {-width/2,0,-depth,lf,epsc};
physicalCrackL = newl;
Curve Loop(physicalCrackL) = {physicalCrackC};
physicalCrackS = news;
Plane Surface (physicalCrackS) = {physicalCrackL};
out[] = Extrude {0, 0, depth} {Surface{physicalCrackS}; };
physicalCrackV = out[1];
//Printf("Subtracting %g from %g",physicalCrackV,brittleRegion);
brittleRegion = BooleanDifference{ Volume{brittleRegion}; Delete; }
                         { Volume{physicalCrackV};  Delete; };

// Initial logical crack
lcrackBegin = newp;
Point(lcrackBegin) = {-width/2+lf,0,-depth};
lcrackEnd = newp;
Point(lcrackEnd) = {-width/2+lf+lc,0,-depth};
logicalCrackL = newl;
Line(logicalCrackL) = {lcrackBegin,lcrackEnd};
out[] = Extrude {0, 0, depth} {Line{logicalCrackL}; };
logicalCrackS = out[1];
out = BooleanFragments{ Volume{brittleRegion};  Delete; }
                      { Surface{logicalCrackS}; Delete; };
//Printf("out[0] %g",out[0]);
//Printf("out[1] %g",out[1]);
//Printf("out[2] %g",out[2]);
//Printf("brittleRegion %g",brittleRegion);
//Printf("logicalCrackS %g",logicalCrackS);


Field[1]           =  Box;
Field[1].XMin      = -width/2;
Field[1].XMax      = -width/2+wBrittle;
Field[1].YMin      = -hBrittle/2;
Field[1].YMax      =  hBrittle/2;
Field[1].ZMin      =  -depth;
Field[1].ZMax      =  0;
Field[1].VIn       =  hf;
Field[1].VOut      =  hc;
Field[1].Thickness =  hBrittle;

Background Field   = 1;

//Brittle part of the body ;
Physical Volume(1) = {brittleRegion};

//Elastic part of the body ;
Physical Volume(2) = {elasticRegion};

//Logical crack
Physical Surface(30) = {logicalCrackS};
//Physical crack
Physical Surface(31) = {29,31};

//Bottom face
Physical Surface(32) = {15,30};
//Top face
Physical Surface(33) = {14,28};

// 3 vertices along the lower face in order to block rigid motions
// LL corner
Physical Point(400) = {18};
// UL corner
Physical Point(401) = {22};
// LR corner
Physical Point(402) = {24};

// 3 vertices along the upper face in order to block rigid motions
// LL corner
Physical Point(500) = {17};
// UL corner
Physical Point(501) = {19};
// LR corner
Physical Point(502) = {21};
