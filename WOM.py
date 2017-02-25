
'''

Things I know I will need

* A function to calculate the interception of a ray with a plane
* A function to calculate interception of a ray with a sphere

Maybe I need classes

'''

import scipy as sp
import pylab as pl

def define_detector(d):
    detector = {'point':sp.array([0., d,0.]), \
             'normal':sp.array([0.,1.,0.]),\
             'width':  10.,\
             'height': 10.,\
             'width pixels': 100,\
             'height pixels': 100,\
             'array':sp.zeros((100,100))}
    return detector

def detector_info(detector):
    print 'Detector Information'
    for key in detector.keys():
        print key,': ',detector[key]
    print
    return

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

def define_source():
    source = {'origin':sp.array([0., 0., 0.])}
    return source

def source_info(source):
    print "Source Information"
    for key in source.keys():
        print key,': ',source[key]
    print
    return

def generate_ray(source):
    ray={}
    ray['origin']    = sp.array([0.,0.,0.])
    ray['direction'] = random_3D_direction()

    return ray

def random_3D_direction():
    phi       = sp.random.uniform(0,sp.pi*2)
    cos_theta = sp.random.uniform(-1,1)
    theta     = sp.arccos(cos_theta)
    sin_theta = sp.sin(theta)
    x = sin_theta*sp.cos(phi)
    y = sin_theta*sp.sin(phi)
    z = cos_theta
    return sp.array([x,y,z])

def ray_info(ray):
    print 'Ray information'
    for key in ray.keys():
        print key,': ',ray[key]
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

def choose_lens(lens_choice):
    if lens_choice=='Newport KBX043':
        lens ={'Lens Shape': 'Bi-Convex',\
                'length unit': 'mm',\
               'Diameter': 25.4,\
               'Lens Material': 'N-BK7',\
               'Antireflection Coating': "Uncoated",\
               'Effective Focal Length': 19.0,\
               'Surface Quality': "40-20 scratch-dig",\
               'Surface Accuracy Irregularity': "lambda/4",\
               'Surface Accuracy, Power': '1.5 lambda',\
               'Surface Flatness': 'lambda/4',\
               'Focal Length, Back': 13.28,\
               'F/#': 0.7,\
               'Centration': '<=3 arc min',\
               'Principle Plane 2': -5.71,\
               'Principle Plane 1': 5.71,
               'Radius of Curvature': 16.687,
               'Chamfers': '0-0.8 mm face width',
               'Chamfers Angle/Tolerance': '45deg +-15deg, typical',
               'Diameter Tolerance': '+0/-0.1 mm',
               'Focal Length Tolerance': '+-1 %',
               'Center Thickness': 14.725,
               'Center Thickness Tolerance': '+-0.1 mm',
               'Edge Thickness': 3.0,
               'Clear Aperture': '>=central 90% of diameter'}
        return lens
    return 'None'


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
lens1 = choose_lens('Newport KBX043')
print lens1

# Ray Trace
iterations = 1000*1000
i=0
while i < iterations:
    # Generate a ray from the source
    #print i
    ray = generate_ray(point_source)
    #ray_info(ray)

    # Find the interception with the detector
    point = get_ray_detector_intercept(ray, detector_1)
    #print 'Intersection point: ',point

    # Accumulate energy in the detector
    integrate_detector(detector_1, point)

    i+=1

# Display the detector
im = pl.imshow(detector_1['array'],cmap='hot')
pl.show()
