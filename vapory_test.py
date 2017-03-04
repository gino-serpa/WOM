

from vapory import *

from WOMlenses import *

# Set the lights
light1 = LightSource( [30, -30, 30], \
                     'color', [1, 1, 1] )
light2 = LightSource( [30,  30, 30], \
                     'color', [1, 1, 1] )
light3 = LightSource( [30,  -30, -30], \
                    'color', [1, 1, 1] )
light4 = LightSource( [30,  30, -30], \
                      'color', [1, 1, 1] )
objects = [light1, light2, light3, light4]

# Set the camera
camera = Camera( 'location', [48, 12, 12],\
                 'look_at', [0, 0, 0] )

# Draw the three axis
L = 40.
r_axis = 0.06
x_axis = Cylinder([ 0, 0, 0], [0,0,L], r_axis,\
                    Texture( Pigment( 'color', [1., 0., 0.])))
y_axis = Cylinder([ 0, 0, 0], [ 0, L, 0], r_axis,\
                    Texture( Pigment( 'color', [0., 1., 0.])))
z_axis = Cylinder([ 0, 0, 0], [ L, 0, 0], r_axis,\
                    Texture( Pigment( 'color', [0, 0., 1.])))
objects.append(x_axis)
objects.append(y_axis)
objects.append(z_axis)

# Set a bi convex lens
    # Get the lens
lens1 = choose_lens('Newport KBX043', 10.)
sphere1 = Sphere([0,0,0],\
                lens1['lens_charateristics']['Radius of Curvature'],\
                Texture(Pigment('color',[0,0,1])))
objects.append(sphere1)
'''
d = 2.6
sphere1 = Sphere( [0, d, 0], 3)
sphere2 = Sphere( [0, -d, 0], 3)
intersection = Intersection(sphere1,\
                            sphere2,\
                            Texture( Pigment( 'color', [0, 0, 1])))
objects.append(intersection)
'''

scene = Scene( camera, objects = objects )
scene.render("WOM.png", width = 800, height = 600 )
