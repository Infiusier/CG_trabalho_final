# coding: utf-8
from typing import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

from solids import *

class Draw():
    def __init(self):
        self.ax = None

    def create_camera_axis(self,volume_vision_mid_point, eye_coordinates):
        axis_n = np.subtract(volume_vision_mid_point, eye_coordinates)
        
        aux_vector = (0.12345, 0.54321, 0)
        
        axis_u = np.cross(axis_n, aux_vector)
        axis_v = np.cross(axis_u, axis_n)
        
        axis_u = (axis_u / np.linalg.norm(axis_u))[0]
        axis_v = (axis_v / np.linalg.norm(axis_v))[0]
        axis_n = (axis_n / np.linalg.norm(axis_n))[0]
    
        return [axis_u, axis_v, axis_n]
    
    
    def create_matplot_image(self,view: str = "3d"):
        fig = plt.figure(figsize=(9,9))
        
        if view == "3d":
            self.ax = fig.add_subplot(111, projection="3d")
            self.init_xyz_axis()
        
        elif view == "2d":
            self.ax = fig.add_subplot(111)
            self.init_xy_axis()
    
    def init_xyz_axis(self):
        self.ax.set_xlabel("X Axis")
        self.ax.set_ylabel("Y Axis")
        self.ax.set_zlabel("Z Axis")
    
        self.ax.plot([6, -6], [0, 0], [0, 0], color='Black', alpha=0.1)
        self.ax.plot([0, 0], [6, -6], [0, 0], color='Black', alpha=0.1)
        self.ax.plot([0, 0], [0, 0], [6, -6], color='Black', alpha=0.1)
        
    def init_xy_axis(self):
        self.ax.set_xlabel("X Axis")
        self.ax.set_ylabel("Y Axis")
    
        self.ax.plot([6, -6], [0, 0], [0, 0], color='Black', alpha=0.1)
        self.ax.plot([0, 0], [6, -6], [0, 0], color='Black', alpha=0.1)
    
    def init_uvn_camera_axis(self,eye: Tuple):
        eye_coordinates = eye[0]
        eye_axis = eye[1]
        
        self.ax.scatter(eye_coordinates[0], eye_coordinates[1], eye_coordinates[2], c="black")
        self.ax.text(eye_coordinates[0], eye_coordinates[1], eye_coordinates[2],"Eye", c="Black")
        
        self.ax.quiver(eye_coordinates[0], eye_coordinates[1], eye_coordinates[2], eye_axis[0], eye_axis[1], eye_axis[2], length=5, normalize=True)
    
    def draw_solids(self,solids: List[Tuple],view: str = "3d", eye: Tuple = None):
        self.create_matplot_image(view)
        
        if eye != None and view == "3d":
            self.init_uvn_camera_axis(eye)
    
        for solid,color in solids:
            
            if view == "3d":
                self.ax.add_collection3d(Poly3DCollection(solid.faces, facecolors=color, linewidths=2, edgecolors=color, alpha=0.1))
            
            for edge in solid.edges:
                
                if view == "3d":
                    self.ax.plot([edge[0][0], edge[1][0]],[edge[0][1], edge[1][1]],zs=[edge[0][2], edge[1][2]], color=color)
                    
                elif view == "2d":
                    self.ax.plot([edge[0][0], edge[1][0]],[edge[0][1], edge[1][1]], color=color)
    
        plt.show()
    