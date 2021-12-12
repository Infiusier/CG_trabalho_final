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
    
    plot_objetos(solids_list,view = "2d")
    
def main_q3():
    
    cubo = Paralelepipedo()
    cubo.criaParalelepipedo(pontoInicial =(0.5,0,0),edge = 1.5)

    paralelepipedo = Paralelepipedo()
    paralelepipedo.criaParalelepipedo(pontoInicial =(-2,0,0), x=1.5, y=5, z=2.5)
      
    piramide = Piramide()
    piramide.criaPiramide(origin_point = (2.5,0,0), edge = 2, z = 3)
    
    tronco = PiramideTronco()
    tronco.criaPiramideTronco(origin_point = (-5.5,0,0),lower_edge = 3, upper_edge = 1.3, z = 2.5)

    '''A aaprtir daqui e necessario revisar oq ta acontecendo'''
    olho = (-5, -5, -5)
    pontoMedio = Objetos.centroVolumeVisão(cubo, piramide)

    eixos = criaEixos(pontoMedio, olho)
    inv_eixos = np.linalg.inv(eixos)

    cubo.vertices = np.matmul(inv_eixos, cubo.vertices.T).T

    piramide.vertices = np.matmul(inv_eixos, piramide.vertices.T).T

    paralelepipedo.vertices = np.matmul(inv_eixos, paralelepipedo.vertices.T).T

    tronco.vertices = np.matmul(inv_eixos, tronco.vertices.T).T
    
    
    solids_list = []
    solids_list.append((cubo,"red"))
    solids_list.append((paralelepipedo,"blue"))
    solids_list.append((piramide,"black"))
    solids_list.append((tronco,"green"))
    
    for solid,color in solids_list:
        solid.update_solid_features()
    
    plot_objetos(solids_list, eye = (olho,inv_eixos))

if __name__ == "__main__":
    #main_q1()
    #main_q2()
    main_q3()
