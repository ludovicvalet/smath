# -*- coding: utf8 -*-

from __future__ import division
from phystricks import *

x=var('x')
f=phyFunction( sin(2*x)+x/3 ).graph(-2,2)

def FFyFBoe():
    pspict,fig = SinglePicture("FFyFBoe")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1.3)

    pspict.DrawGraphs(f)
    pspict.DrawDefaultGrid()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
