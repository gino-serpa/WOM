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
    solution = min(solutions)
    return solution
