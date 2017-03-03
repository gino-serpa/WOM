
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


def intercept_sphere_ray(sphere, ray):
    center = sphere['center']
    radius = sphere['radius']
    print '\nSphere center and radius: ', center, radius

    p0 = ray['origin']
    d  = ray['direction']
    print 'Ray origin and direction: ', p0, d

    # Solve the equation
    A = sp.inner(d,d)
    B = 2 * sp.inner(d,p0-center)
    C = sp.inner(p0-center,p0-center)-radius**2
    t = solve_quadratic(A, B, C)
    print 'solution', t
    if t!=None:
        intercept = p0 + t*d
    return intercept

def solve_quadratic(a,b,c):
    # So there is a better way in which there are no problems
    # if numerator and denominators are too small
    disc = b**2-4*a*c
    if disc < 0: return None
    if disc ==0:
        x=-b/2
        if x<0:
            return None
        else:
            return x
    radical = sp.sqrt(disc)
    x1 = (-b+radical)/(2*a)
    x2 = (-b-radical)/(2*a)
    solutions=[]
    if x1>0: solutions.append(x1)
    if x2>0: solutions.append(x2)
    if len(solutions)==0: return None
    solution=min(solutions)
    return solution


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
