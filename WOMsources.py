import scipy as sp

def define_source():
    source = {'origin':sp.array([0., 0., 0.])}
    return source

def source_info(source):
    print "\n\t\tSource Information"
    for key in source.keys():
        print key,': ',source[key]
    print
    return
