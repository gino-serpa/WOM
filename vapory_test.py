import scipy as sp

from vapory import *

from WOMlenses import *

RED    = [ 1, 0, 0]
GREEN  = [ 0, 1, 0]
BLUE   = [ 0, 0, 1]
ORIGIN = [ 0, 0, 0]
WHITE =  [ 1, 1, 1]
X = sp.array([ 1, 0, 0])
Y = sp.array([ 0, 1, 0])
Z = sp.array([ 0, 0, 1])

def get_pov_lens(lens):
    print lens
    radius = lens['lens_charateristics']['Radius of Curvature']
    thickness = lens['lens_charateristics']['Center Thickness']
    diameter = lens['lens_charateristics']['Diameter']
    sphere1 = Sphere(radius*Y,
                      radius)
    sphere2 = Sphere((-radius+thickness)*Y,
                      radius)
    pov_lens = Intersection(sphere1,sphere2)
    bounding_cylinder = Cylinder([0,0,0],[0,thickness,0],diameter/2.)
    pov_lens = Intersection(pov_lens,bounding_cylinder,
                        Texture(Pigment('color', BLUE)))
    return pov_lens

'''
3! = 6
'''

# Set the lights
light1 = LightSource( [30, -30, 30],
                     'color', WHITE )
light2 = LightSource( [30,  30, 30],
                     'color', WHITE )
light3 = LightSource( [30,  -30, -30],
                     'color', WHITE )
light4 = LightSource( [30,  30, -30],
                     'color', WHITE )
objects = [light1, light2, light3, light4]

# Set the camera
camera = Camera( 'location', 100*X+40*Y+10*Z,
                 'look_at', ORIGIN )

# Draw the three axis
L = 40.
r_axis = 0.06
x_axis = Cylinder(ORIGIN, L*X, r_axis,
                    Texture( Pigment( 'color', RED)))
y_axis = Cylinder(ORIGIN, L*Y, r_axis,\
                    Texture( Pigment( 'color', GREEN)))
z_axis = Cylinder(ORIGIN, L*Z, r_axis,\
                    Texture( Pigment( 'color', BLUE)))
objects.append(x_axis)
objects.append(y_axis)
objects.append(z_axis)

# Set a bi convex lens
    # Get the lens
lens1 = choose_lens('Newport KBX043', 10.)

pov_lens1 = get_pov_lens(lens1)
objects.append(pov_lens1)

scene = Scene( camera, objects = objects )
scene.render("WOM.png", width = 800, height = 600 )
