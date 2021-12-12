# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from solids import *
from typing import List


def init_plot(view: str):
    fig = plt.figure(figsize=(10, 10))
    
    if view == "3d":
        ax = fig.add_subplot(111, projection="3d")
    
    elif view == "2d":
        ax = fig.add_subplot(111)
    
    return fig, ax

def init_eixos(ax):
    ax.set_xlabel("Eixo X")
    ax.set_ylabel("Eixo Y")
    ax.set_zlabel("Eixo Z")

    ax.plot([5.2, -5.2], [0, 0], [0, 0], color='Black', alpha=0.4)
    ax.plot([0, 0], [5.2, -5.2], [0, 0], color='Black', alpha=0.4)
    ax.plot([0, 0], [0, 0], [5.2, -5.2], color='Black', alpha=0.4)

#===============================================================================
# def plot_objeto(objeto: Objetos, color: str = "black"):
#     '''Nao esta sendo utilizada'''
#     fig, ax = init_plot()
# 
#     for linha in objeto.arestas:
#         ax.plot(
#             [linha[0][0], linha[1][0]],
#             [linha[0][1], linha[1][1]],
#             zs=[linha[0][2], linha[1][2]],
#         )
# 
#     ax.add_collection3d(Poly3DCollection(
#         objeto.faces, facecolors=color, linewidths=1.5, edgecolors=color, alpha=0.1))
# 
#     ax.set_zlim3d(-5, 5)
#     ax.set_xlim3d(-5, 5)
#     ax.set_ylim3d(-5, 5)
# 
#     init_eixos(ax)
#     plt.show()
#===============================================================================
    


def plot_objetos(objetos: List[Tuple],view: str = "3d"):
    fig, ax = init_plot(view)
    
    print(view)

    for objeto,color in objetos:
        for linha in objeto.arestas:
            #print(linha)
            
            if view == "3d":
                ax.plot(
                    [linha[0][0], linha[1][0]],
                    [linha[0][1], linha[1][1]],
                    zs=[linha[0][2], linha[1][2]],
                )
                
            elif view == "2d":
                ax.plot(
                    [linha[0][0], linha[1][0]],
                    [linha[0][1], linha[1][1]], color=color)

        if view == "3d":
            ax.add_collection3d(Poly3DCollection(objeto.faces, facecolors=color, linewidths=1.5, edgecolors=color, alpha=0.1))

    #ax.set_zlim3d(-6, 6)
    #ax.set_xlim3d(-6, 6)
    #ax.set_ylim3d(-6, 6)

    if view == "3d":
        init_eixos(ax)
        
    plt.show()
    
def plot_objetos_q4(objetos: List[Objetos]):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    for objeto in objetos:
        for linha in objeto.arestas:
            print(linha)
            ax.plot(
                [linha[0][0], linha[1][0]],
                [linha[0][1], linha[1][1]], color=objeto.cor[0])

    plt.show()


def plot_objetos_q3(objetos: List[Tuple], comp_u, comp_v, comp_n, olho):
    fig, ax = init_plot()

    ax.scatter(olho[0], olho[1], olho[2], c="black")

    ax.text(olho[0], olho[1], olho[2],"Eye", c="Black")

    for objeto,color in objetos:
        for linha in objeto.arestas:
            print(linha)
            ax.plot(
                [linha[0][0], linha[1][0]],
                [linha[0][1], linha[1][1]],
                zs=[linha[0][2], linha[1][2]],
            )

        ax.add_collection3d(Poly3DCollection(
            objeto.faces, facecolors=color, linewidths=1.5, edgecolors=color, alpha=0.1))

    ax.set_zlim3d(-6, 6)
    ax.set_xlim3d(-6, 6)
    ax.set_ylim3d(-6, 6)

    ax.set_xlabel("Eixo X")
    ax.set_ylabel("Eixo Y")
    ax.set_zlabel("Eixo Z")

    ax.plot([6, -6], [olho[1], olho[1]], [olho[2], olho[2]], color='Black', alpha=0.4)
    ax.plot([olho[0], olho[0]], [6, -6], [olho[2], olho[2]], color='Black', alpha=0.4)
    ax.plot([olho[0], olho[0]], [olho[1], olho[1]], [6, -6], color='Black', alpha=0.4)

    plt.show()



