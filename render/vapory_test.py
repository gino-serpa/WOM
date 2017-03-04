from vapory import *

camera = Camera( 'location', [8, 2, 2],\
                 'look_at', [0, 0, 0] )


light1 = LightSource( [4, -4, 4], \
                     'color', [1, 1, 1] )
light2 = LightSource( [4,  4, 4], \
                     'color', [1, 1, 1] )
light3 = LightSource( [4,  -4, -4], \
                    'color', [1, 1, 1] )
light4 = LightSource( [4,  4, -4], \
                      'color', [1, 1, 1] )
objects = [light1, light2, light3, light4]

d = 2.6
sphere1 = Sphere( [0, d, 0], 3)
sphere2 = Sphere( [0, -d, 0], 3)
intersection = Intersection(sphere1,\
                            sphere2,\
                            Texture( Pigment( 'color', [0, 0, 1])))
objects.append(intersection)

scene = Scene( camera, objects = objects )
scene.render("WOM.png", width = 800, height = 600 )
