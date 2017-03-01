import scipy as sp

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
    print
    return
