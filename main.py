from solids import *
from draw import *

def main():

    cubo = Paralelepipedo.criaParalelepipedo(pontoInicial =(-0.75,-0.75,0), x=1.5, y=1.5, z=1.5)
    cubo.titulo = "Cubo"
    cubo.cor = ("purple", 0.1)
    cubo.montaObjeto()
    plot_objeto(objeto=cubo)

#===============================================================================
#     paralelepipedo = Paralelepipedo.criaParalelepipedo(pontoInicial =(0,0,0), x=1.5, y=5, z=2.5)
#     paralelepipedo.titulo = "Paralelepipedo"
#     paralelepipedo.cor = ("blue", 0.1)
#     paralelepipedo.montaObjeto()
#     plot_objeto(objeto=paralelepipedo)
# 
#     piramide = Piramide.criaPiramide(2, 2, 3)
#     piramide.titulo = "Piramide"
#     piramide.cor = ("gray", 0.1)
#     piramide.translacao((-1, -1, 0))
#     piramide.rotacaoEixoY(45)
#     piramide.montaObjeto()
#     plot_objeto(objeto=piramide)
# 
#     tronco = PiramideTronco.criaPiramideTronco(xBase=3, yBase=3, z=2.5, xSuperior=1.3, ySuperior=1.3)
#     tronco.titulo = "Tronco"
#     tronco.cor = ("green", 0.1)
#     tronco.montaObjeto()
#     plot_objeto(objeto=tronco)
#===============================================================================


if __name__ == "__main__":
    main()
