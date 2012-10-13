# -*- coding: utf8 -*-
from phystricks import *
def FaussePerspectivewAwxAJ():
    pspict,fig = SinglePicture("FaussePerspectivewAwxAJ")
    pspict.dilatation(1)

    c=3
    perspective=ObliqueProjection(30,0.5)
    A=perspective.point(0,0,c)
    B=perspective.point(c,0,c)
    C=perspective.point(c,0,0)
    D=perspective.point(0,0,0)

    A.put_mark(0.2,135,"\( A\)",automatic_place=pspict)
    B.put_mark(0.2,45,"\( B\)",automatic_place=pspict)
    C.put_mark(0.2,-45,"\( C\)",automatic_place=pspict)
    D.put_mark(0.2,225,"\( D\)",automatic_place=pspict)
    #A.parameters.symbol="none"
    #B.parameters.symbol="none"
    #C.parameters.symbol="none"
    #D.parameters.symbol="none"

    carre=Polygon(A,B,C,D)
    carre.parameters.filled()
    K=Segment(A,B).center()
    L=Segment(D,C).center()
    J=perspective.point(c+1,0,c)
    K.parameters.symbol="x"
    L.parameters.symbol="x"
    J.parameters.symbol="x"
    K.put_mark(0.2,90,"\( K\)",automatic_place=pspict)
    L.put_mark(0.2,-90,"\( L\)",automatic_place=pspict)
    J.put_mark(0.2,90,"\( J\)",automatic_place=pspict)

    pspict.DrawGraphs(A,B,C,D,carre,K,L,J)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
