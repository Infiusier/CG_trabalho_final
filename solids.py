from dataclasses import dataclass
import numpy as np
from math import sin, cos, radians
from typing import List, Tuple, Any


@dataclass
class Objetos:
    vertices: Any = None  
    arestas: Any = None
    faces: Any = None
    origem: List[float] = (0,0,0)  
    titulo: str = ""
    cor: List[any] = None

    def criaArestas(self):
        pass

    def criaFaces(self):
        pass

    def montaObjeto(self):
        self.criaArestas()
        self.criaFaces()

    def translacao(self, destino: Tuple):
        origem = [destino[index] - self.origem[index] for index, value in enumerate(destino)]

        matrizDeTranslacao = np.array(
            [
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [origem[0], origem[1], origem[2], 1],
            ]
        )

        self.vertices = np.hstack((self.vertices, np.ones((len(self.vertices), 1))))
        self.vertices = np.dot(self.vertices, matrizDeTranslacao)

        self.vertices = np.delete(self.vertices, 3, axis=1)
        self.origem = destino

    def rotacaoEixoY(self, angulo):
        angulo = radians(angulo)
        rot = np.array(
            [
                [cos(angulo), -sin(angulo), 0],
                [sin(angulo), cos(angulo), 0],
                [0, 0, 1]
            ])

        self.vertices = np.matmul(self.vertices, rot)

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
    @staticmethod
    def criaPiramideTronco(xBase: float = 1, yBase: float = 1, z: float = 1, xSuperior: float = 1, ySuperior: float = 1):
        paralelepipedo = Paralelepipedo(
            vertices=np.array(
                [
                    [0, 0, 0],      
                    [xBase, 0, 0],  
                    [xBase, yBase, 0],
                    [0, yBase, 0],
                    [(xBase-xSuperior)/2, (yBase-ySuperior)/2, z],       
                    [(xBase-xSuperior)/2 + xSuperior,  (yBase-ySuperior)/2, z],
                    [(xBase-xSuperior)/2 + xSuperior, (yBase-ySuperior)/2 + ySuperior, z],
                    [(xBase-xSuperior)/2, (yBase-ySuperior)/2 + ySuperior, z], 
                ]
            )
        )

        return paralelepipedo

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
    @staticmethod
    def criaParalelepipedo(pontoInicial: Tuple, x: float = 1, y: float = 1, z: float = 1):
        paralelepipedo = Paralelepipedo(
            vertices=np.array(
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
        )

        return paralelepipedo

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
    @staticmethod
    def criaPiramide(x: float = 1, y: float = 1, z: float = 1):
        return Piramide(
            vertices=np.array(
                [
                    [0, 0, 0], 
                    [x, 0, 0], 
                    [x, y, 0], 
                    [0, y, 0],  
                    [x/2, y/2, z], 
                ]
            )
        )

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
