

import scipy as sp
import pylab as pl

from WOMsources import *
from WOMdetectors import *
from WOMlenses import *
from WOMrays import *
from WOMintercepts import *

def integrate_detector(detector, point):
    if point!=None:
        x = point[0]
        z = point[2]
        delta_x = 10./100
        delta_z = 10./100
        if sp.absolute(x)< 5 and sp.absolute(z)<5:
            #print 'There is a hit'
            pixel_x = int((x+5)/delta_x)
            #print pixel_x
            pixel_z = int((z+5)/delta_z)
            detector['array'][pixel_x,pixel_z]+=1
    return

def traverse_lens(lens, ray):
    '''
    Here is the plan
    * create two spheres and a box that define the lens
    * Find the first interception (discard everything that does
      not enter the first sphere)
    * Given the intercept find the ray inisde the glass (Snell3d)
    * Find the next intercept that should be the second sphere
    * Again snell 3d

    '''
    # Given the lens generate both spheres and the cylinder
    sphere1 = {'center':sp.array([7., 12., 0.]), 'radius':7. }
    print 'Sphere: ', sphere1
    cylinder = {'length':2, 'radius':1}
    print 'Cylinder', cylinder
    sphere2 = {'center':sp.array([7., 12., 0.]), 'radius':7. }
    print 'Sphere: ', sphere2

    # Now I can calculate the intercept
    intercept = intercept_sphere_ray(sphere1, ray)
    print 'Intercept: ',intercept

    ray_out = {'origin':sp.array([0,0,0]),\
               'direction':sp.array([1,1,1])}
    return ray_out


'''----------------------------------------------------

                    Main
Gino Serpa
---------------------------------------------------- '''

# Define a source
point_source = define_source()
source_info(point_source)

# Define a lens (Newport KBX043)
lens1 = choose_lens('Newport KBX043', 10.)
print lens1

# Define a detector
detector_1 = define_detector(2)
detector_info(detector_1)

# Generate one ray
ray_in = generate_ray(point_source)
ray_in = {'origin':sp.array([0., -25.4, 0.]),\
       'direction':sp.array([0.,   5.0, 5.])}
ray_info(ray_in)

# Traverse a lense
ray_out = traverse_lens(lens1,ray_in)
ray_info(ray_out)

# Now I can calculate the refraction



'''
# Ray Trace
iterations = 1000*1000
i=0
while i < iterations:
    # Generate a ray from the source
    ray = generate_ray(point_source)

    # Find exit ray after traversing the lens
    new_ray = traverse_element(lense1,ray)

    # Find the interception with the detector
    point = get_ray_detector_intercept(ray, detector_1)
    #print 'Intersection point: ',point

    # Accumulate energy in the detector
    integrate_detector(detector_1, point)

    i+=1

# Display the detector
im = pl.imshow(detector_1['array'],cmap='hot')
pl.show()
'''
