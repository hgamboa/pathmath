from pathmath import *

import numpy.random
from numpy import *
from pylab import *
from scipy import interpolate


def test_circle_perimeter():
    t,x,y = generate_circle()
    s = get_s(x,y)

    assert_almost_equal(s[-1],2*pi,decimal=2)

def test_incremental_s():
    t,x,y = generate_circle()
    s = get_s(x,y)

    assert(check_incremental_s(s))


def test_constant_ds():
    e = numpy.random.exponential(scale=0.1, size=100)
    d = cumsum(e[e>0.05])
    t=d[d<2*pi]

    x= sin(t)
    y= cos(t)

    s = get_s(x,y)
    v = get_v(t,s)

    #v chould be constant a near 1
    assert_approx_equal(sum(v),len(v),2)

    print v

test_circle_perimeter()
test_incremental_s()
test_constant_ds()
