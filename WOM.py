
'''

Things I know I will need

* A function to calculate the interception of a ray with a plane
* A function to calculate interception of a ray with a sphere

I have no class, so no classes

'''

import scipy as sp

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
        point = P_0r + t*d
        return point
    return

'''----------------------------------------------------

                    Main

---------------------------------------------------- '''

'''# Define a ray
ray = {'origin':sp.array([0.,0.,0.]), \
       'direction':sp.array([0., sp.sqrt(2.)/2, sp.sqrt(2.)/2])}
print 'ray = ', ray
'''

# Define a detector
detector = {'point':sp.array([0.,1.,0.]), \
         'normal':sp.array([0.,1.,0.])}
print 'detector = ', detector

# Find the interception
point_source = {'origin':sp.array([0., 0., 0.])}

iterations = 100
i=0
while i < iterations:
    ray = generate_ray()
    point = get_ray_detector_intercept(ray, detector)
