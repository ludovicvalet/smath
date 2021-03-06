# -*- coding: utf8 -*-
from phystricks import *
def NUWooJepuh():
    pspict,fig = SinglePicture("NUWooJepuh")
    pspict.dilatation_X(0.7)
    pspict.dilatation_Y(0.7)


    xmin=-3
    xmax=3
    ymin=-3
    ymax=3
    x=var('x')

    f=phyFunction(-3*x-2).fit_inside(xmin,xmax,ymin,ymax)
    f.put_mark(0.2,-45,"\( d_1\)",pspict=pspict,position="corner")

    A=Point(2,1)
    B=Point(-3,0)
    A.put_mark(0.2,45,"\( A\)",pspict=pspict,position="corner")
    B.put_mark(0.2,90+45,"\( B\)",pspict=pspict,position="corner")
     
    pspict.DrawGraphs(f,A,B)
    pspict.DrawDefaultGrid()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
