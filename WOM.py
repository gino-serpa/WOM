
'''


'''

import scipy as sp
import pylab as pl
from WOMsources import *
from WOMdetectors import *
from WOMlenses import *
from WOMrays import *

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


def get_ray_detector_intercept(ray, plane):
    n = plane['normal']
    d = ray['direction']
    denominator = sp.inner(d, n)
    if denominator==0:
        return None
    else:
        P_0p = plane['point']
        P_0r = ray['origin']
        numerator = sp.inner(P_0p-P_0r, n)
        t = numerator/denominator
        if t<0: return None
        point = P_0r + t*d
        return point
    return


'''----------------------------------------------------

                    Main
Gino Serpa
---------------------------------------------------- '''

# Define a source
point_source = define_source()
source_info(point_source)

# Define a detector
detector_1 = define_detector(2)
detector_info(detector_1)

# Define a lens (Newport KBX043)
lens1 = choose_lens('Newport KBX043', 10.)
print lens1

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
