from phystricks import *
def HistoAutomobile():
    pspict,fig = SinglePicture("HistoAutomobile")
    pspict.dilatation(1)

    H=Histogram([(0,0.25,137),(0.25,0.5,106),(0.5,1,112),(1,2.5,154),(2.5,5,100),(5,10,33)])
    H.legende="Chiffre d'affaires (en millions d'euros)"

    pspict.DrawGraphs(H)
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()
