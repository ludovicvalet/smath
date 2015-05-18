# -*- coding: utf8 -*-
from phystricks import *

import phystricksCommons

def CXWooOMPOQT():
    # 5A
    pspict,fig = SinglePicture("CXWooOMPOQT")

    moustaches=[]

    # Le delta_y n'a pas d'importance parce qu'il est recalculé plus bas.
    moustaches.append(Moustache(7.90,10.20,14.45,16.70,20.00,h=0.5,delta_y=0.75))   # DS1
    moustaches.append(Moustache(5.10,8.75,10.87,16.29,20.00,h=0.5,delta_y=0.75))    # DS2
    #moustaches.append(Moustache(5.88,10.36,14.41,16.75,20.00,h=0.5,delta_y=0.75))   # DS3
    #moustaches.append(Moustache(4.42,9.80,12.57,16.64,20.00,h=0.5,delta_y=0.75))    # DS4
    #moustaches.append(Moustache(8.00,12.60,14.00,18.70,20.00,h=0.5,delta_y=0.75))   # DS5
    #moustaches.append(Moustache(3.50,7.00,11.00,13.28,17.50,h=0.5,delta_y=0.75))    # DS6

    moustaches.append(BoxDiagram([13.941666666666666, 17.516666666666666, 15.5, 17.416666666666664, 13.341666666666665, 5.949999999999999, 5.883333333333333, 10.308333333333334, 14.733333333333334, 19.46666666666667, 13.925, 17.066666666666666, 14.966666666666665, 8.033333333333333, 14.783333333333331, 20.0, 9.216666666666667, 16.366666666666667, 16.3, 12.991666666666669, 10.433333333333334, 14.091666666666665, 9.691666666666666, 20.0],h=0.5,delta_y=0.75))  # DS3
    moustaches.append(BoxDiagram([9.366666666666667, 20.0, 16.616666666666667, 12.629999999999999, 8.37, 5.0166666666666675, 8.02, 11.233333333333334, 18.61, 19.166666666666668, 7.15, 16.04, 14.351666666666665, 4.416666666666666, 11.5, 17.65, 11.158333333333335, 12.475000000000001, 17.766666666666666, 10.333333333333334, 14.783333333333335, 14.0, 12.506666666666666, 16.65],h=0.5,delta_y=0.75))    # DS4
    moustaches.append(BoxDiagram([13.0, 19.0, 19.0, 20.0, 13.5, 14.5, 11.5, 12.5, 20.0, 19.5, 12.5, 15.0, 15.5, 7.5, 12.5, 19.0, 14.5, 14.0, 16.0, 10.0, 14.0, 17.5, 12.0],h=0.5,delta_y=0.75))   #DS5
    moustaches.append(BoxDiagram([7.0, 14.0, 14.0, 13.5, 3.5, 4.0, 16.5, 13.5, 7.0, 7.0, 11.0, 3.5, 17.0, 11.5, 11.0, 12.5, 6.0, 12.0, 8.0, 17.5],h=0.5,delta_y=0.75))      # DS6
    moustaches.append(BoxDiagram([7.0, 18.0, 13.5, 12.0, 7.5, 5.0, 8.5, 15.5, 18.0, 12.0, 12.5, 16.0, 6.0, 8.0, 19.5, 13.0, 13.5, 6.5, 16.0, 13.5,     11.5, 20.0],h=0.5,delta_y=0.75))

    phystricksCommons.DS_statistics(moustaches,pspict)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

def PJQooTWPTXV():
    # 5B
    pspict,fig = SinglePicture("PJQooTWPTXV")

    moustaches=[]

    # Le delta_y n'a pas d'importance parce qu'il est recalculé plus bas.
    moustaches.append(Moustache(6.00,8.99,11.50,14.37,20.00,h=0.5,delta_y=0.75))    # DS1
    moustaches.append(Moustache(4.93,7.71,11.85,14.03,16.48,h=0.5,delta_y=0.75))    # DS2
    #moustaches.append(Moustache(4.90,7.38,10.35,13.36,17.09,h=0.5,delta_y=0.75))    # DS3
    #moustaches.append(Moustache(1.50,7.57,10.23,13.12,16.03,h=0.5,delta_y=0.75))    # DS4
    #moustaches.append(Moustache(4.50,6.50,9.25,14.03,15.50,h=0.5,delta_y=0.75))     # DS5
    #moustaches.append(Moustache(1.50,7.50,9.50,11.40,16.00,h=0.5,delta_y=0.75))     # DS6


    moustaches.append(BoxDiagram([14.706666666666667, 13.156666666666666, 6.576666666666666, 17.093333333333334, 11.899999999999999, 7.136666666666668, 15.216666666666665, 10.348333333333333, 13.391666666666666, 11.57, 5.466666666666667, 11.666666666666666, 9.8, 4.9, 7.726666666666668, 15.936666666666667, 6.8966666666666665, 15.319999999999999, 13.226666666666665, 9.666666666666668, 7.65, 7.35, 7.513333333333334],h=0.5,delta_y=0.75))      # DS3
    moustaches.append(BoxDiagram([14.483333333333333, 10.674999999999997, 8.191666666666665, 16.033333333333328, 11.391666666666664, 1.4999999999999998, 13.099999999999998, 9.333333333333332, 14.558333333333332, 5.933333333333333, 7.583333333333331, 11.558333333333332, 14.141666666666664, 6.116666666666666, 7.233333333333332, 13.916666666666663, 5.483333333333332, 15.349999999999998, 11.999999999999998, 15.208333333333332, 9.783333333333331, 8.508333333333331, 8.299999999999999],h=0.5,delta_y=0.75))     # DS4
    moustaches.append(BoxDiagram([14.0, 9.0, 7.0, 15.5, 14.0, 9.0, 12.5, 11.5, 5.0, 5.0, 10.5, 8.5, 7.0, 6.0, 6.5, 15.0, 6.5, 14.5, 10.0, 15.0, 7.0, 7.0, 4.5],h=0.5,delta_y=0.75))   # DS5
    moustaches.append(BoxDiagram([12.000000000000002, 12.000000000000002, 11.500000000000002, 16.000000000000004, 10.000000000000002, 9.500000000000002, 10.500000000000002, 9.000000000000002, 11.000000000000002, 8.500000000000002, 8.000000000000002, 11.500000000000002, 7.500000000000002, 1.5000000000000002, 7.500000000000002, 13.500000000000002, 5.500000000000001, 11.000000000000002, 9.500000000000002, 9.000000000000002, 7.000000000000001, 4.000000000000001, 5.500000000000001],h=0.5,delta_y=0.75))     # DS6

    moustaches.append(BoxDiagram([11.5, 15.0, 15.5, 13.5, 3.0, 13.5, 6.0, 15.0, 10.5, 7.5, 14.0, 14.0, 5.0, 7.0, 12.5, 6.5, 11.5, 13.0, 11.0, 6.0, 5.0],h=0.5,delta_y=0.75))       # DS 7


    phystricksCommons.DS_statistics(moustaches,pspict)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()


def JNGEooISdbXx():
    # 5AB mélangés
    pspict,fig = SinglePicture("JNGEooISdbXx")

    moustaches=[]

    # Le delta_y n'a pas d'importance parce qu'il est recalculé plus bas.
    moustaches.append(Moustache(6.00,10.10,12.10,16.30,20.00,h=0.5,delta_y=0.75))   # DS1
    moustaches.append(Moustache(4.93,8.08,11.45,15.20,20.00,h=0.5,delta_y=0.75))    # DS2

    phystricksCommons.DS_statistics(moustaches,pspict)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

def TYIooYKqeNv():
    PJQooTWPTXV()           # 5B
    CXWooOMPOQT()           # 5A
    #JNGEooISdbXx()         # 5A et 5B mélangés
