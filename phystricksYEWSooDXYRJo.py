# -*- coding: utf8 -*-
from phystricks import *
def YEWSooDXYRJo():
    pspict,fig = SinglePicture("YEWSooDXYRJo")
    pspict.dilatation(0.3)

    A=Point(0,0)
    B=Point(6,0)
    C=Point(0,3)

    A.put_mark(0.2,180+45,"\( K\)",automatic_place=(pspict,"corner"))
    B.put_mark(0.2,-45,"\( L\)",automatic_place=(pspict,"corner"))
    C.put_mark(0.2,90+45,"\( M\)",automatic_place=(pspict,"corner"))

    rh=RightAngle(  Segment(C,A),Segment(A,B),0.6,0,1  )

    trig=Polygon(A,B,C)
    trig.edges[0].put_mark(0.2,-90,"\( 16\)",automatic_place=(pspict,"N"))

    trig.edges[1].put_mark(0.2,trig.edges[1].advised_mark_angle*degree+180,"\( ?\)",automatic_place=(pspict,"corner"))
    trig.edges[2].put_mark(0.2,180,"\( 12\)",automatic_place=(pspict,"E"))

    pspict.DrawGraphs(A,B,C,trig,rh)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()