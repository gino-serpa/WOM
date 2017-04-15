import scipy as sp

def define_detector(d):
    '''
    d: distance from origin (this is of course temporary )
    '''
    detector = {'point':sp.array([0., d,0.]), \
             'normal':sp.array([0.,1.,0.]),\
             'width':  10.,\
             'height': 10.,\
             'width pixels': 100,\
             'height pixels': 100,\
             'array':sp.zeros((100,100))}
    return detector

def detector_info(detector):
    print '\n\t\tDetector Information'
    for key in detector.keys():
        print key,': ',detector[key]
    print

    return
