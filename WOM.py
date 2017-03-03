
'''


'''

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


#  Find intersection of the ray with an sphere of index n_s
# Generate one ray
ray = generate_ray(point_source)
ray = {'origin':sp.array([0., 0., 0.]),\
       'direction':sp.array([0., 1., 0.])}
ray_info(ray)


# Generate sphere
sphere = {'center':sp.array([7., 12., 0.]), 'radius':7. }
print 'Sphere: ', sphere

# Now I can calculate the intercept
intercept = intercept_sphere_ray(sphere, ray)
print 'Intercept: ',intercept

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
