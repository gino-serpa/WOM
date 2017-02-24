
'''

Things I know I will need

* A function to calculate the interception of a ray with a plane
* A function to calculate interception of a ray with a sphere

Maybe I need classes

'''

import scipy as sp

def define_detector(d):
    detector = {'point':sp.array([0., d,0.]), \
             'normal':sp.array([0.,1.,0.]),\
             'width':  10.,\
             'height': 10.,\
             'width pixels': 100,\
             'height pixels': 100}
    return detector

def detector_info(detector):
    print 'Detector Information'
    print 'Point :', detector['point']
    print 'Normal :',detector['normal']
    print 'Width :',detector['width']
    print 'Height :',detector['height']
    print 'Width pixels :',detector['width pixels']
    print 'Height pixels :',detector['height pixels']
    print
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
    ray['direction'] = sp.array([1.,2.,1.])
    ray['origin']    = sp.array([0.,0.,0.])
    return ray

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
        point = P_0r + t*d
        return point
    return


'''----------------------------------------------------

                    Main
Gino Serpa
---------------------------------------------------- '''



# Define a detector
detector_1 = define_detector(2)
detector_info(detector_1)


# Define a source
point_source = define_source()
source_info(point_source)

# Ray Trace
iterations = 100
i=0
while i < iterations:
    # Generate a ray from the source
    ray = generate_ray(point_source)
    ray_info(ray)

    # Find the interception with the detector
    point = get_ray_detector_intercept(ray, detector_1)
    # Accumulate energy in the detector
    i+=1

# Display the detector
