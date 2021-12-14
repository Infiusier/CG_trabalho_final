# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from solids import *
from typing import *

def create_camera_axis(volume_vision_mid_point, eye_coordinates):
    n = np.subtract(volume_vision_mid_point, eye_coordinates)
    aux_vector = (0.12345, 0.54321, 0)
    u = np.cross(n, aux_vector)
    v = np.cross(u, n)

    u = (u / np.linalg.norm(u))[0]
    v = (v / np.linalg.norm(v))[0]
    n = (n / np.linalg.norm(n))[0]

    return [u, v, n]


def create_plot_image(view: str = "3d"):
    fig = plt.figure(figsize=(9,9))
    
    if view == "3d":
        ax = fig.add_subplot(111, projection="3d")
    
    elif view == "2d":
        ax = fig.add_subplot(111)
    
    return ax

def init_xyz_axis(ax):
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")

    ax.plot([6, -6], [0, 0], [0, 0], color='Black', alpha=0.1)
    ax.plot([0, 0], [6, -6], [0, 0], color='Black', alpha=0.1)
    ax.plot([0, 0], [0, 0], [6, -6], color='Black', alpha=0.1)

def init_uvn_camera_axis(ax,eye: Tuple):
    eye_coordinates = eye[0]
    eye_axis = eye[1]
    
    ax.scatter(eye_coordinates[0], eye_coordinates[1], eye_coordinates[2], c="black")
    ax.text(eye_coordinates[0], eye_coordinates[1], eye_coordinates[2],"Eye", c="Black")
    
    ax.quiver(eye_coordinates[0], eye_coordinates[1], eye_coordinates[2], eye_axis[0], eye_axis[1], eye_axis[2], length=5, normalize=True)

def plot_solids(solids: List[Tuple],view: str = "3d", eye: Tuple = None):
    ax = create_plot_image(view)
    
    if eye != None:
        init_uvn_camera_axis(ax,eye)

    for solid,color in solids:
        for edge in solid.edges:
            
            if view == "3d":
                ax.plot([edge[0][0], edge[1][0]],[edge[0][1], edge[1][1]],zs=[edge[0][2], edge[1][2]])
                
            elif view == "2d":
                ax.plot([edge[0][0], edge[1][0]],[edge[0][1], edge[1][1]], color=color)

        if view == "3d":
            ax.add_collection3d(Poly3DCollection(solid.faces, facecolors=color, linewidths=2, edgecolors=color, alpha=0.1))

    if view == "3d":
        init_xyz_axis(ax)
        
    plt.show()
    
#===============================================================================
# def plot_objetos_q4(objetos: List[Solid]):
#     fig = plt.figure()
#     ax = fig.add_subplot(111)
# 
#     for objeto in objetos:
#         for linha in objeto.arestas:
#             print(linha)
#             ax.plot(
#                 [linha[0][0], linha[1][0]],
#                 [linha[0][1], linha[1][1]], color=objeto.cor[0])
# 
#     plt.show()
#===============================================================================