# coding: utf-8
from solids import *
from draw import *

def main_q1():

    cubo = Paralelepipedo()
    cubo.criaParalelepipedo(pontoInicial =(-0.75,-0.75,0),edge = 1.5)
    plot_objetos([(cubo,"red")])

    paralelepipedo = Paralelepipedo()
    paralelepipedo.criaParalelepipedo(pontoInicial =(0,0,0), x=1.5, y=5, z=2.5)
    plot_objetos([(paralelepipedo,"blue")])
  
    piramide = Piramide()
    piramide.criaPiramide(origin_point = (-1,-1,0), edge = 2, z = 3)
    piramide.rotacaoEixoY(45,pivot_point = (0,0,0))
    plot_objetos([(piramide,"black")])
  
    tronco = PiramideTronco()
    tronco.criaPiramideTronco(lower_edge = 3, upper_edge = 1.3, z = 2.5)
    plot_objetos([(tronco,"brown")])
    
    
def main_q2():
    
    solids_list = []
    
    cubo = Paralelepipedo()
    cubo.criaParalelepipedo(pontoInicial =(0.5,0,0),edge = 1.5)
    solids_list.append((cubo,"red"))

    paralelepipedo = Paralelepipedo()
    paralelepipedo.criaParalelepipedo(pontoInicial =(-2,0,0), x=1.5, y=5, z=2.5)
    solids_list.append((paralelepipedo,"blue"))
  
    piramide = Piramide()
    piramide.criaPiramide(origin_point = (2.5,0,0), edge = 2, z = 3)
    solids_list.append((piramide,"black"))
  
    tronco = PiramideTronco()
    tronco.criaPiramideTronco(origin_point = (-5.5,0,0),lower_edge = 3, upper_edge = 1.3, z = 2.5)
    solids_list.append((tronco,"green"))
    
    plot_objetos(solids_list)
    
def main_q3():
    
    solids_list = []
    
    cubo = Paralelepipedo()
    cubo.criaParalelepipedo(pontoInicial =(0.5,0,0),edge = 1.5)
    solids_list.append((cubo,"red"))

    paralelepipedo = Paralelepipedo()
    paralelepipedo.criaParalelepipedo(pontoInicial =(-2,0,0), x=1.5, y=5, z=2.5)
    solids_list.append((paralelepipedo,"blue"))
  
    piramide = Piramide()
    piramide.criaPiramide(origin_point = (2.5,0,0), edge = 2, z = 3)
    solids_list.append((piramide,"black"))
  
    tronco = PiramideTronco()
    tronco.criaPiramideTronco(origin_point = (-5.5,0,0),lower_edge = 3, upper_edge = 1.3, z = 2.5)
    solids_list.append((tronco,"green"))
    
    plot_objetos(solids_list)


if __name__ == "__main__":
    #main_q1()
    #main_q2()
    main_q3()
