import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from solids import *
from typing import List


def init_plot():
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection="3d")
    return fig, ax

def init_eixos(ax):
    ax.set_xlabel("Eixo X")
    ax.set_ylabel("Eixo Y")
    ax.set_zlabel("Eixo Z")

    ax.plot([5.2, -5.2], [0, 0], [0, 0], color='Black', alpha=0.4)
    ax.plot([0, 0], [5.2, -5.2], [0, 0], color='Black', alpha=0.4)
    ax.plot([0, 0], [0, 0], [5.2, -5.2], color='Black', alpha=0.4)

def plot_objeto(objeto: Objetos):
    fig, ax = init_plot()

    for linha in objeto.arestas:
        print(linha)
        ax.plot(
            [linha[0][0], linha[1][0]],
            [linha[0][1], linha[1][1]],
            zs=[linha[0][2], linha[1][2]],
        )

    ax.add_collection3d(Poly3DCollection(
        objeto.faces, facecolors=objeto.cor[0], linewidths=1.5, edgecolors=objeto.cor[0], alpha=objeto.cor[1]))

    ax.set_zlim3d(-5, 5)
    ax.set_xlim3d(-5, 5)
    ax.set_ylim3d(-5, 5)

    init_eixos(ax)

    save_image(objeto.titulo)
    plt.show()
    
def save_image(image_name: str):
    plt.savefig(image_name)


def plot_objetos(objetos: List[Objetos], titulo: str):
    fig, ax = init_plot()

    for objeto in objetos:
        for linha in objeto.arestas:
            print(linha)
            ax.plot(
                [linha[0][0], linha[1][0]],
                [linha[0][1], linha[1][1]],
                zs=[linha[0][2], linha[1][2]],
            )

        ax.add_collection3d(Poly3DCollection(
            objeto.faces, facecolors=objeto.cor[0], linewidths=1.5, edgecolors=objeto.cor[0], alpha=objeto.cor[1]))

    ax.set_zlim3d(-6, 6)
    ax.set_xlim3d(-6, 6)
    ax.set_ylim3d(-6, 6)

    init_eixos(ax)

    plt.savefig("imagens/" + titulo + ".png")
    plt.show()


def plot_objetos_q3(objetos: List[Objetos], comp_u, comp_v, comp_n, olho):
    fig, ax = init_plot()

    ax.scatter(olho[0], olho[1], olho[2], c="black")

    ax.text(olho[0], olho[1], olho[2],
            "Eye", c="Black")

    for objeto in objetos:
        for linha in objeto.arestas:
            print(linha)
            ax.plot(
                [linha[0][0], linha[1][0]],
                [linha[0][1], linha[1][1]],
                zs=[linha[0][2], linha[1][2]],
            )

        ax.add_collection3d(Poly3DCollection(
            objeto.faces, facecolors=objeto.cor[0], linewidths=1.5, edgecolors=objeto.cor[0], alpha=objeto.cor[1]))

    ax.set_zlim3d(-6, 6)
    ax.set_xlim3d(-6, 6)
    ax.set_ylim3d(-6, 6)

    ax.set_xlabel("Eixo X")
    ax.set_ylabel("Eixo Y")
    ax.set_zlabel("Eixo Z")

    ax.plot([6, -6], [olho[1], olho[1]], [olho[2], olho[2]], color='Black', alpha=0.4)
    ax.plot([olho[0], olho[0]], [6, -6], [olho[2], olho[2]], color='Black', alpha=0.4)
    ax.plot([olho[0], olho[0]], [olho[1], olho[1]], [6, -6], color='Black', alpha=0.4)

    plt.savefig("imagens/" + "questao3" + ".png")
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

    plt.savefig("imagens/" + "questao4" + ".png")
    plt.show()
