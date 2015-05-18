# -*- coding: utf8 -*-

from phystricks import *
from phystricksCommons import Pyramide

def DLUGooTzdMAu():
    pspict,fig = SinglePicture("DLUGooTzdMAu")
    #pspict.dilatation_X(1)
    #pspict.dilatation_Y(1)
    pspict.dilatation(1)

    x=var('x')
    pyramide=Pyramide(4,0.9,0.5)
    pyramide.centres[(0,0)].put_mark(0.0,0,"\( -15\)",automatic_place=(pspict,"center"))
    pyramide.centres[(1,0)].put_mark(0.0,0,"\ldots",automatic_place=(pspict,"center"))
    pyramide.centres[(1,1)].put_mark(0.0,0,"\( 10\)",automatic_place=(pspict,"center"))
    pyramide.centres[(3,0)].put_mark(0.0,0,"\( 7\)",automatic_place=(pspict,"center"))

    pspict.DrawGraphs(pyramide)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

def BJDWooWkSKfU():
    pspict,fig = SinglePicture("BJDWooWkSKfU")
    #pspict.dilatation_X(1)
    #pspict.dilatation_Y(1)
    pspict.dilatation(1)

    x=var('x')
    pyramide=Pyramide(4,0.9,0.5)
    pyramide.centres[(0,0)].put_mark(0.0,0,"\( 1\)",automatic_place=(pspict,"center"))
    pyramide.centres[(1,0)].put_mark(0.0,0,"\ldots",automatic_place=(pspict,"center"))
    pyramide.centres[(2,0)].put_mark(0.0,0,"\(2\)",automatic_place=(pspict,"center"))
    pyramide.centres[(3,0)].put_mark(0.0,0,"\( 3\)",automatic_place=(pspict,"center"))

    pspict.DrawGraphs(pyramide)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

def LOGZooNgDIkE():
    DLUGooTzdMAu()
    BJDWooWkSKfU()