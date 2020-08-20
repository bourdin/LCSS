SetFactory("OpenCASCADE");
// All units of length must be scaled by a factor x0 (usually 1e-3), given in the 00_INFO.json file

width    =  100;   // total width of the domain
height   =  60;    // total height of the domain 
xc0      = -40;    // lower left corner of the rounded rectangle to cut
yc0      = -20;    
xc1      =  40;    // upper right corner of the rounded rectangle to cur
yc1      =  20;   
wBrittle =  4;     // width of the area where the mesh is refined around the beam path
                   // must be  wide enough so that the rounded part of teh rectangle is 
                   // contained in the region with a fine mesh, i.e. 
                   // wBrittle > 2 R ( sqrt(2)-1) where R is the radius (R is a good choice)
depth    =  10;     // not used in 2D
hf       =  3.e-2; // fine mesh
hc       =  0.5;   // coarse mesh
yc       =  yc0;   // position of the initial crack (must be in the refined area or the script will break)
lf       =  1;     // length of the initial physical crack represented by a very elongated ellipse 
epsc     =  lf/50; // height of the ellipse


hf = 0.1;
hc = 2;
lf = 3;
epsc = 1;

Printf("Domain size: %g x %g x %g",width,height,depth);
Printf("Using hf=%g, hc=%g",hf,hc);

Mesh.Format                  = 1;
Mesh.MshFileVersion          = 2;
Mesh.CharacteristicLengthFromPoints = 0;
Mesh.CharacteristicLengthFromCurvature = 0;
Mesh.CharacteristicLengthExtendFromBoundary = 0;
//Mesh.OptimizeNetgen          = 1;
Mesh.Optimize                = 1;


box0 = newv;
Box(box0) = {-width/2,-height/2,-depth,width,height,depth};

box1 = newv;
Box(box1) = {xc0+wBrittle/2,yc0+wBrittle/2,-depth,xc1-xc0-wBrittle,yc1-yc0-wBrittle,depth};

box2 = newv;
Box(box2) = {xc0-wBrittle/2,yc0-wBrittle/2,-depth,xc1-xc0+wBrittle,yc1-yc0+wBrittle,depth};

box3 = newv;
Box(box3) = {-width/2,yc0-wBrittle/2,-depth,xc0-wBrittle/2+width/2,wBrittle,depth};


// Initial Physical crack
physicalCrackC = newc;
Ellipse(physicalCrackC) = {-width/2,yc,-depth,lf,epsc};
physicalCrackL = newl;
Curve Loop(physicalCrackL) = {physicalCrackC};
physicalCrackS = news;
Plane Surface (physicalCrackS) = {physicalCrackL};
out[] = Extrude {0, 0, depth} {Surface{physicalCrackS}; };
physicalCrackV = out[1];

out   = BooleanDifference{ Volume{box0}; Delete; }
                         { Volume{box1, box2, box3}; };
zone3 = out[0];

out   = BooleanDifference{ Volume{box2}; Delete; }
                         { Volume{box1}; };
zone2 = out[0];
zone1 = box1[0];

out   = BooleanDifference{ Volume{box3}; Delete; }
                         { Volume{physicalCrackV}; Delete;};
zone4 = out[0];

// Imprint all volumes and surfaces at the cost of renumbering everything
Coherence;

// Delete everything but the upper skin
Delete {
  Volume{1,13,25,37}; 
}
Delete {
  Surface{7,8,9,10,11,14,16,22,23,25,26,27,28,29,30,31,32,33,35,36,38,39,40,41};
}






Field[1]           =  Box;
Field[1].XMin      = -width/2;
Field[1].XMax      =  xc1+wBrittle/2.;
Field[1].YMin      =  yc0-wBrittle/2;
Field[1].YMax      =  yc0+wBrittle/2;
Field[1].ZMin      =  -depth;
Field[1].ZMax      =  0;
Field[1].VIn       =  hf;
Field[1].VOut      =  hc;
Field[1].Thickness =  wBrittle;
 
Field[2]           =  Box;
Field[2].XMin      =  xc0-wBrittle/2.;
Field[2].XMax      =  xc1+wBrittle/2.;
Field[2].YMin      =  yc1-wBrittle/2;
Field[2].YMax      =  yc1+wBrittle/2;
Field[2].ZMin      =  -depth;
Field[2].ZMax      =  0;
Field[2].VIn       =  hf;
Field[2].VOut      =  hc;
Field[2].Thickness =  wBrittle;

Field[3]           =  Box;
Field[3].XMin      =  xc0-wBrittle/2.;
Field[3].XMax      =  xc0+wBrittle/2.;
Field[3].YMin      =  yc0-wBrittle/2;
Field[3].YMax      =  yc1+wBrittle/2;
Field[3].ZMin      =  -depth;
Field[3].ZMax      =  0;
Field[3].VIn       =  hf;
Field[3].VOut      =  hc;
Field[3].Thickness =  wBrittle;

Field[4]           =  Box;
Field[4].XMin      =  xc1-wBrittle/2.;
Field[4].XMax      =  xc1+wBrittle/2.;
Field[4].YMin      =  yc0-wBrittle/2;
Field[4].YMax      =  yc1+wBrittle/2;
Field[4].ZMin      =  -depth;
Field[4].ZMax      =  0;
Field[4].VIn       =  hf;
Field[4].VOut      =  hc;
Field[4].Thickness =  wBrittle;

Field[10]           = Min;
Field[10].FieldsList = {1,2,3,4};

Background Field   = 10;
 
//Brittle part of the body ;
Physical Surface(1) = {34,37};

//Elastic part of the body ;
Physical Surface(2) = {12,24};

//Physical crack
Physical Line(31) = {76,77};

// 3 vertices along the upper face in order to block rigid motions
// LL corner
Physical Point(500) = {33};
// UL corner
Physical Point(501) = {38};
// LR corner
Physical Point(502) = {40};
