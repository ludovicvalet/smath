# -*- coding: utf8 -*-
from phystricks import *
def KTEDooQRUWXz():
    pspict,fig = SinglePicture("KTEDooQRUWXz")
    #pspict.dilatation_X(1)
    #pspict.dilatation_Y(1)
    pspict.dilatation(0.5)
    pspict.rotation(-25)


    S=Point(0,0)
    T=Point(6,0)
    U=Point(8,4)

    trig=Polygon(S,T,U)
    trig.put_mark(0.2,points_names="STU",pspict=pspict)

    V=trig.edges[0].midpoint()
    mediane=Segment(V,U)
    W=mediane.midpoint()

    remediane=Segment(S,W)

    trig.edges[0].divide_in_two(n=2,d=0.1,l=0.4,angle=45,pspict=pspict)
    mediane.divide_in_two(n=1,d=0.1,l=0.4,angle=45,pspict=pspict)

    trgris=Polygon(S,W,U)
    trgris.parameters.filled()
    trgris.parameters.fill.color="lightgray"

    L=Point(U.x,T.y)
    s1=Segment(T,L)
    s2=Segment(U,L)
    for s in [s1,s2]:
        s.parameters.style="dashed"
    rh=RightAngleAOB(U,L,T)
    
    s2.put_measure(measure_distance=-0.5,mark_distance=0.2,mark_angle=0,name="\SI{4}{\kilo\meter}",automatic_place=(pspict,""))
    V.put_mark(0.2,angle=None,added_angle=180,text="\( V\)",automatic_place=(pspict,""))
    W.put_mark(0.2,angle=None,added_angle=180,text="\( W\)",automatic_place=(pspict,""))

    no_symbol(trig.vertices,V,W)
    pspict.DrawGraphs(trgris,trig,V,W,mediane,remediane,s1,s2,rh,W,V)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
