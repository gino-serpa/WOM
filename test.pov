#include "colors.inc"

	//		Here goes the camera definition
camera {location <50, 30, 50> look_at <0, 0, 0>}

	//		Here goes the background definition
background {color Silver}

	//		Here go the light definitions
light_source { <8, 8, 8> color White}
light_source { <8, 8, -8> color White}
light_source { <8, -8, 8> color White}
light_source { <8, -8, -8> color White}

	//		Here go the axis definition
#declare L_axis = 40;
#declare r_axis = 0.2 ;
cylinder { <  0, 0, 0>,
	< L_axis, 0, 0>,
	r_axis
	open
	texture{ pigment {color Red transmit 0.75}}}
cylinder { <  0, 0, 0>,
	<  0, L_axis, 0>,
	r_axis
	open
	texture{ pigment {color Green transmit 0.75}}}
cylinder { <  0, 0, 0>,
	<  0, 0, L_axis>,
	r_axis
	open
	texture{ pigment {color Blue transmit 0.75}}}

	//		Here goes a lens 
#declare Curv_lens = 16.687;
#declare Lens_thickness = 14.725;
#declare Lens_diameter = 25.4;
#declare Left_sphere =
	sphere { <0,Curv_lens,0>, 
	Curv_lens}
intersection {
	object{Left_sphere}
	object{Left_sphere
		rotate 180*x
		translate Lens_thickness*y}
	object{cylinder{<0,0,0>,<0,Lens_thickness,0>,Lens_diameter/2.}}
	texture {pigment { color LightBlue transmit 0.35}}
	}
