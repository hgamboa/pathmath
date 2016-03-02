import numpy.random
from numpy import *
from pylab import *
from scipy import interpolate

from numpy.testing import assert_almost_equal, assert_approx_equal

def get_path_smooth_s(t,s,x,y,stol=1):
    #stol in samples per pixel
    _ss = arange(s[0], s[-1], stol)
    #TODO: evaluate the usage of weights
    splxs = interpolate.UnivariateSpline(s,x)
    xs = splxs(_ss)

    splys = interpolate.UnivariateSpline(s,y)
    ys = splys(_ss)

    splts = interpolate.UnivariateSpline(s,t)
    ts = splts(_ss)

    nss = get_s(xs,ys)

    ss = arange(nss[0], nss[-1], stol)

    xs = splxs(ss)
    ys = splys(ss)
    ts = splts(ss)



    #TODO: Assert that dss is constant
    vs= diff(ss)[0]/splts(ss,nu=1)


    # angle = atan(dy/dx)
    # unwrap removes descontinuities.
    angle = unwrap(atan2(splys.derivative()(ss),splxs.derivative()(ss)))

    # c = (dx * ddy - dy * ddx) / ((dx^2+dy^2)^(3/2))
    curvature_top =     splxs.derivative()(ss) * splys.derivative(2)(ss) -
                        splys.derivative()(ss) * splxs.derivative(2)(ss)

    curvuature_bottom = (splxs.derivative()(ss)**2 + splys.derivative()(ss)**2) ** (3/2.0)

    curvature = curvature_top/curvature_bottom


    return ts, ss, xs, ys, vs, angle, curvature


def get_path_smooth_t(t,s,x,y,ttol=10):
    #ttol in samples per second

    return tt, st, xt, yt



def get_s(x,y):
    ds = sqrt(diff(x)**2+diff(y)**2)
    s = cumsum(concatenate(([0],ds)))

    return s

def get_v(t,s):
    return diff(s)/diff(t)

def generate_circle(r=1.0,step=0.01):
    t = arange(0,2*pi,step)
    x = sin(t)*r
    y = cos(t)*r

    return t,x,y

def check_incremental_s(s):
    return all(diff(s)>0.0)


