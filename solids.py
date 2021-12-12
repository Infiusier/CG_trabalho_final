# coding: utf-8
from dataclasses import dataclass
import numpy as np
from math import sin, cos, radians
from typing import List, Tuple, Any


class Objetos():
    
    def __init__(self):
        self.vertices: Any = None  
        self.arestas: Any = None
        self.faces: Any = None
        self.origem: List[float] = [0,0,0]
        
    def update_solid_features(self):
        self.criaArestas()
        self.criaFaces()
        self.origem = self.vertices[0]

    def translacao(self, point : Tuple):
        '''Implementação de uma forma mais simples de transladar '''
        for i in range(len(self.vertices)):
            line = self.vertices[i]
            line[0] += point[0]
            line[1] += point[1]
            line[2] += point[2]
            self.vertices[i] = line
                  
        #self.origem[0] += point[0]
        #self.origem[1] += point[1]
        #self.origem[2] += point[2]
        self.origem = self.vertices[0]
              
        self.update_solid_features()
       
#===============================================================================
#         '''Implementação q n entendi'''
#         origem = []
#          
#         origem.append(x - self.origem[0])
#         origem.append(y - self.origem[1])
#         origem.append(z - self.origem[2])  
# 
#         matrizDeTranslacao = np.array(
#             [
#                 [1, 0, 0, 0],
#                 [0, 1, 0, 0],
#                 [0, 0, 1, 0],
#                 [origem[0], origem[1], origem[2], 1],
#             ]
#         )
# 
#         self.vertices = np.hstack((self.vertices, np.ones((len(self.vertices), 1))))
#         self.vertices = np.dot(self.vertices, matrizDeTranslacao)
# 
#         self.vertices = np.delete(self.vertices, 3, axis=1)
#         self.origem = (x,y,z)
#         
#         self.update_solid_features()
#===============================================================================
           
    def rotacaoEixoY(self, angulo, pivot_point: Tuple = None):
        
        if pivot_point == None:
            pivot_point = tuple(self.origem)
            
        
        aux_origin = self.origem[:]
        
        translation_point = (0-pivot_point[0],0-pivot_point[1],0-pivot_point[2])
        
        self.translacao(translation_point)
        
        angulo = radians(angulo)
        rot = np.array(
            [
                [cos(angulo), -sin(angulo), 0],
                [sin(angulo), cos(angulo), 0],
                [0, 0, 1]
            ])

        self.vertices = np.matmul(self.vertices, rot)
        self.origem = self.vertices[0]
        
        translation_point = (pivot_point[0],pivot_point[1],pivot_point[2])
        self.translacao(translation_point)
        
        self.update_solid_features()

    def centroDeMassa(self):
        somaX = somaY = somaZ = 0
        for ponto in self.vertices:
            somaX += ponto[0]
            somaY += ponto[1]
            somaZ += ponto[2]

        totalPontos = len(self.vertices)

        centroDeMassa = [somaX / totalPontos, somaY / totalPontos, somaZ / totalPontos]

        return centroDeMassa

    def centroVolumeVisão(self, *objetos):
        somaX = somaY = somaZ = 0
        pontosCentrais = []
        for objeto in objetos:
            pontosCentrais.append(objeto.centroDeMassa())

        for ponto in pontosCentrais:
            somaX += ponto[0]
            somaY += ponto[1]
            somaZ += ponto[2]

        totalPontosCentrais = len(pontosCentrais)

        centroVolume = [[somaX / totalPontosCentrais, somaY / totalPontosCentrais, somaZ / totalPontosCentrais]]

        return centroVolume


class PiramideTronco(Objetos):
    
    def __init__(self):
        super().__init__()
    
    def criaPiramideTronco(self,origin_point: Tuple = (0,0,0),xBase: float = 1, yBase: float = 1, z: float = 1, xSuperior: float = 1, ySuperior: float = 1, lower_edge = None, upper_edge = None):
        
        if lower_edge != None:
            xBase = lower_edge
            yBase = lower_edge
            
        if upper_edge != None:
            xSuperior = upper_edge
            ySuperior = upper_edge
       
        self.vertices=np.array(
            [
                [origin_point[0], origin_point[1], origin_point[2]],      
                [origin_point[0] + xBase, origin_point[1], origin_point[2]],  
                [origin_point[0] + xBase, origin_point[1] + yBase, origin_point[2]],
                [origin_point[0], origin_point[1] + yBase, origin_point[2]],
                [origin_point[0] + (xBase-xSuperior)/2, origin_point[1] + (yBase-ySuperior)/2, origin_point[2] + z],       
                [origin_point[0] + (xBase-xSuperior)/2 + xSuperior, origin_point[1] + (yBase-ySuperior)/2, origin_point[2] + z],
                [origin_point[0] + (xBase-xSuperior)/2 + xSuperior, origin_point[1] + (yBase-ySuperior)/2 + ySuperior, origin_point[2] + z],
                [origin_point[0] + (xBase-xSuperior)/2, origin_point[1] + (yBase-ySuperior)/2 + ySuperior, origin_point[2] + z], 
            ]
        )
        
        self.update_solid_features()
       

    def criaArestas(self):
        self.arestas = [
            [self.vertices[0], self.vertices[1]], 
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
            [self.vertices[3], self.vertices[7]], 
        ]

    def criaFaces(self):
        self.faces = [
            [
                self.vertices[0],
                self.vertices[1],
                self.vertices[2],
                self.vertices[3],
            ], 
            [
                self.vertices[4],
                self.vertices[5],
                self.vertices[6],
                self.vertices[7],
            ],
            [
                self.vertices[2],
                self.vertices[3],
                self.vertices[7],
                self.vertices[6],
            ], 
            [
                self.vertices[1],
                self.vertices[2],
                self.vertices[6],
                self.vertices[5],
            ], 
            [
                self.vertices[0],
                self.vertices[1],
                self.vertices[5],
                self.vertices[4],
            ],  
            [
                self.vertices[0],
                self.vertices[3],
                self.vertices[7],
                self.vertices[4],
            ], 
        ]


class Paralelepipedo(Objetos):
    
    def __init__(self):
        super().__init__()

    def criaParalelepipedo(self,pontoInicial: Tuple = (0,0,0), x: float = 1, y: float = 1, z: float = 1, edge: float = None):
        
        if edge != None:
            x = edge
            y = edge
            z = edge
        
        self.vertices = np.array(
                [
                    [pontoInicial[0], pontoInicial[1], pontoInicial[2]],  
                    [pontoInicial[0] + x, pontoInicial[1], pontoInicial[2]],  
                    [pontoInicial[0] + x, pontoInicial[1] + y, pontoInicial[2]], 
                    [pontoInicial[0], pontoInicial[1] + y, pontoInicial[2]],  
                    [pontoInicial[0], pontoInicial[1], pontoInicial[2] + z], 
                    [pontoInicial[0] + x, pontoInicial[1], pontoInicial[2] + z],
                    [pontoInicial[0] + x, pontoInicial[1] + y, pontoInicial[2] + z], 
                    [pontoInicial[0], pontoInicial[1] + y, pontoInicial[2] + z],
                ]
        )
        
        self.update_solid_features()
        
    def criaArestas(self):
        self.arestas = [
            [self.vertices[0], self.vertices[1]],  
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
            [self.vertices[3], self.vertices[7]], 
        ]

    def criaFaces(self):
        self.faces = [
            [
                self.vertices[0],
                self.vertices[1],
                self.vertices[2],
                self.vertices[3],
            ],  
            [
                self.vertices[4],
                self.vertices[5],
                self.vertices[6],
                self.vertices[7],
            ], 
            [
                self.vertices[2],
                self.vertices[3],
                self.vertices[7],
                self.vertices[6],
            ], 
            [
                self.vertices[1],
                self.vertices[2],
                self.vertices[6],
                self.vertices[5],
            ],
            [
                self.vertices[0],
                self.vertices[1],
                self.vertices[5],
                self.vertices[4],
            ],
            [
                self.vertices[0],
                self.vertices[3],
                self.vertices[7],
                self.vertices[4],
            ],
        ]


class Piramide(Objetos):
    
    def __init__(self):
        super().__init__()

    def criaPiramide(self,origin_point: Tuple = (0,0,0),x: float = 1, y: float = 1, z: float = 1, edge = None):
        
        if  edge != None:
            x = edge
            y = edge
        
        self.vertices=np.array(
            [
                [origin_point[0], origin_point[1], origin_point[2]], 
                [origin_point[0] + x, origin_point[1], origin_point[2]], 
                [origin_point[0] + x, origin_point[1] + y, origin_point[2]], 
                [origin_point[0],origin_point[1] + y, origin_point[2]],  
                [origin_point[0] + x/2,origin_point[1] + y/2,origin_point[2] + z], 
            ]
        )
        
        self.update_solid_features()
        

    def criaArestas(self):
        self.arestas = [
            [self.vertices[0], self.vertices[1]],
            [self.vertices[1], self.vertices[2]], 
            [self.vertices[2], self.vertices[3]], 
            [self.vertices[3], self.vertices[0]], 
            [self.vertices[0], self.vertices[4]], 
            [self.vertices[1], self.vertices[4]],
            [self.vertices[2], self.vertices[4]],
            [self.vertices[3], self.vertices[4]],
        ]

    def criaFaces(self):
        self.faces = [
            [
                self.vertices[0],
                self.vertices[1],
                self.vertices[2],
                self.vertices[3],
            ], 
            [self.vertices[0], self.vertices[1], self.vertices[4]], 
            [self.vertices[1], self.vertices[2], self.vertices[4]], 
            [self.vertices[2], self.vertices[3], self.vertices[4]],
            [self.vertices[3], self.vertices[0], self.vertices[4]], 
        ]
