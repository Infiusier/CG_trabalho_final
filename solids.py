# coding: utf-8
import numpy as np
from math import *
from typing import *

class Solid():
    
    def __init__(self):
        self.faces: Any = None
        self.vertices: Any = None  
        self.edges: Any = None
        self.origin: List[float] = [0,0,0]
        
    def update_solid_features(self):
        self.update_faces()
        self.update_edges()
        
        self.origin = self.vertices[0]

    def solid_translation(self, point : Tuple):
        for i in range(len(self.vertices)):
            line = self.vertices[i]
            line[0] += point[0]
            line[1] += point[1]
            line[2] += point[2]
            self.vertices[i] = line
                  
        self.origin = self.vertices[0]
              
        self.update_solid_features()
           
    def solid_rotation(self, angle, pivot_point: Tuple = None):
        
        if pivot_point == None:
            pivot_point = tuple(self.origin)
            
        
        aux_origin = self.origin[:]
        
        translation_point = (0-pivot_point[0],0-pivot_point[1],0-pivot_point[2])
        
        self.solid_translation(translation_point)
        
        angle = radians(angle)
        rot = np.array(
            [[cos(angle), -sin(angle), 0],
             [sin(angle), cos(angle), 0],
             [0, 0, 1]])

        self.vertices = np.matmul(self.vertices, rot)
        self.origin = self.vertices[0]
        
        translation_point = (pivot_point[0],pivot_point[1],pivot_point[2])
        self.solid_translation(translation_point)
        
        self.update_solid_features()

    def solid_center_of_mass(self):
        x_coordinates = 0
        y_coordinates = 0
        z_coordinates = 0
        
        for point in self.vertices:
            x_coordinates += point[0]
            y_coordinates += point[1]
            z_coordinates += point[2]
            
        
        CoM_x = x_coordinates / len(self.vertices)
        CoM_y = y_coordinates / len(self.vertices)
        CoM_z = z_coordinates / len(self.vertices)

        return [CoM_x, CoM_y, CoM_z]

    @staticmethod
    def solid_vision_volume(solids: List):
        x_coordinates = 0
        y_coordinates = 0
        z_coordinates = 0
         
        for solid in solids:
            x_coordinates += solid.solid_center_of_mass()[0]
            y_coordinates += solid.solid_center_of_mass()[1]
            z_coordinates += solid.solid_center_of_mass()[2]
         
        VV_x = x_coordinates/len(solids)
        VV_y = y_coordinates/len(solids)
        VV_z = z_coordinates/len(solids)
 
        return [[VV_x,VV_y,VV_z]]
    
class Parallelepiped(Solid):
    
    def __init__(self):
        super().__init__()

    def create_parallelepiped(self,origin_point: Tuple = (0,0,0), x: float = 1, y: float = 1, z: float = 1, edge: float = None):
        
        if edge != None:
            x = edge
            y = edge
            z = edge
        
        self.vertices = np.array([[origin_point[0], origin_point[1], origin_point[2]],  
                                  [origin_point[0] + x, origin_point[1], origin_point[2]],  
                                  [origin_point[0] + x, origin_point[1] + y, origin_point[2]], 
                                  [origin_point[0], origin_point[1] + y, origin_point[2]],  
                                  [origin_point[0], origin_point[1], origin_point[2] + z], 
                                  [origin_point[0] + x, origin_point[1], origin_point[2] + z],
                                  [origin_point[0] + x, origin_point[1] + y, origin_point[2] + z], 
                                  [origin_point[0], origin_point[1] + y, origin_point[2] + z]])
        
        self.update_solid_features()
        
    def update_edges(self):
        self.edges = [[self.vertices[0], self.vertices[1]],  
                      [self.vertices[1], self.vertices[2]],  
                      [self.vertices[2], self.vertices[3]], 
                      [self.vertices[3], self.vertices[0]],  
                      [self.vertices[4], self.vertices[5]],  
                      [self.vertices[5], self.vertices[6]],
                      [self.vertices[6], self.vertices[7]], 
                      [self.vertices[7], self.vertices[4]],  
                      [self.vertices[0], self.vertices[4]], 
                      [self.vertices[1], self.vertices[5]], 
                      [self.vertices[2], self.vertices[6]],
                      [self.vertices[3], self.vertices[7]]]

    def update_faces(self):
        self.faces = [[self.vertices[0],self.vertices[1],self.vertices[2],self.vertices[3]],  
                      [self.vertices[4],self.vertices[5],self.vertices[6],self.vertices[7]], 
                      [self.vertices[2],self.vertices[3],self.vertices[7],self.vertices[6]], 
                      [self.vertices[1],self.vertices[2],self.vertices[6],self.vertices[5]],
                      [self.vertices[0],self.vertices[1],self.vertices[5],self.vertices[4]],
                      [self.vertices[0],self.vertices[3],self.vertices[7],self.vertices[4]]]
        
class Pyramid(Solid):
    
    def __init__(self):
        super().__init__()

    def create_pyramid(self,origin_point: Tuple = (0,0,0),x: float = 1, y: float = 1, z: float = 1, edge = None):
        
        if  edge != None:
            x = edge
            y = edge
        
        self.vertices=np.array([[origin_point[0], origin_point[1], origin_point[2]], 
                                [origin_point[0] + x, origin_point[1], origin_point[2]], 
                                [origin_point[0] + x, origin_point[1] + y, origin_point[2]], 
                                [origin_point[0],origin_point[1] + y, origin_point[2]],  
                                [origin_point[0] + x/2,origin_point[1] + y/2,origin_point[2] + z]])
        
        self.update_solid_features()
        

    def update_edges(self):
        self.edges = [[self.vertices[0], self.vertices[1]],
                      [self.vertices[1], self.vertices[2]], 
                      [self.vertices[2], self.vertices[3]], 
                      [self.vertices[3], self.vertices[0]], 
                      [self.vertices[0], self.vertices[4]], 
                      [self.vertices[1], self.vertices[4]],
                      [self.vertices[2], self.vertices[4]],
                      [self.vertices[3], self.vertices[4]]]

    def update_faces(self):
        self.faces = [[self.vertices[0],self.vertices[1],self.vertices[2],self.vertices[3]], 
                      [self.vertices[0], self.vertices[1], self.vertices[4]], 
                      [self.vertices[1], self.vertices[2], self.vertices[4]], 
                      [self.vertices[2], self.vertices[3], self.vertices[4]],
                      [self.vertices[3], self.vertices[0], self.vertices[4]]]

class Pyramid_trunk(Solid):
    
    def __init__(self):
        super().__init__()
    
    def create_pyramid_trunk(self,origin_point: Tuple = (0,0,0),x_lower: float = 1, y_lower: float = 1, z: float = 1, x_upper: float = 1, y_upper: float = 1, lower_edge = None, upper_edge = None):
        
        if lower_edge != None:
            x_lower = lower_edge
            y_lower = lower_edge
            
        if upper_edge != None:
            x_upper = upper_edge
            y_upper = upper_edge
       
        self.vertices=np.array([[origin_point[0], origin_point[1], origin_point[2]],      
                                [origin_point[0] + x_lower, origin_point[1], origin_point[2]],  
                                [origin_point[0] + x_lower, origin_point[1] + y_lower, origin_point[2]],
                                [origin_point[0], origin_point[1] + y_lower, origin_point[2]],
                                [origin_point[0] + (x_lower-x_upper)/2, origin_point[1] + (y_lower-y_upper)/2, origin_point[2] + z],       
                                [origin_point[0] + (x_lower-x_upper)/2 + x_upper, origin_point[1] + (y_lower-y_upper)/2, origin_point[2] + z],
                                [origin_point[0] + (x_lower-x_upper)/2 + x_upper, origin_point[1] + (y_lower-y_upper)/2 + y_upper, origin_point[2] + z],
                                [origin_point[0] + (x_lower-x_upper)/2, origin_point[1] + (y_lower-y_upper)/2 + y_upper, origin_point[2] + z]])
        
        self.update_solid_features()
       

    def update_edges(self):
        self.edges = [[self.vertices[0], self.vertices[1]], 
                      [self.vertices[1], self.vertices[2]],  
                      [self.vertices[2], self.vertices[3]],  
                      [self.vertices[3], self.vertices[0]],  
                      [self.vertices[4], self.vertices[5]],  
                      [self.vertices[5], self.vertices[6]],  
                      [self.vertices[6], self.vertices[7]],  
                      [self.vertices[7], self.vertices[4]],  
                      [self.vertices[0], self.vertices[4]],  
                      [self.vertices[1], self.vertices[5]],  
                      [self.vertices[2], self.vertices[6]], 
                      [self.vertices[3], self.vertices[7]]]

    def update_faces(self):
        self.faces = [[self.vertices[0],self.vertices[1],self.vertices[2],self.vertices[3]], 
                      [self.vertices[4],self.vertices[5],self.vertices[6],self.vertices[7]],
                      [self.vertices[2],self.vertices[3],self.vertices[7],self.vertices[6]], 
                      [self.vertices[1],self.vertices[2],self.vertices[6],self.vertices[5]], 
                      [self.vertices[0],self.vertices[1],self.vertices[5],self.vertices[4]],  
                      [self.vertices[0],self.vertices[3],self.vertices[7],self.vertices[4]]]
