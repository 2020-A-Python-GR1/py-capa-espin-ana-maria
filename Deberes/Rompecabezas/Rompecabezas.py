import numpy as np
import matplotlib.pyplot as plt 
from scipy import ndimage
from scipy import misc
from random import sample

mapache = misc.face()
rompecabezas = []
juego = []

def partes_4(imagen):
    global rompecabezas
    arr1, arr2 = np.split(mapache,2)
    arr1, arr3 = np.hsplit(arr1,2)
    arr2, arr4 = np.hsplit(arr2,2)
    rompecabezas.append(arr1)
    rompecabezas.append(arr2)
    rompecabezas.append(arr3)
    rompecabezas.append(arr4)
    dibujar(rompecabezas,"Imagen Original")
    desordenar()
    
def dibujar(lista_rompecabezas, titulo):
    fig, axs = plt.subplots(2, 2, sharex='col', sharey='row',
                        gridspec_kw={'hspace': 0, 'wspace': 0})
    (ax1, ax2), (ax3, ax4) = axs
    fig.suptitle(titulo)
    axs[0, 0].imshow(lista_rompecabezas[0])
    axs[0, 1].imshow(lista_rompecabezas[2])
    axs[1, 0].imshow(lista_rompecabezas[1])
    axs[1, 1].imshow(lista_rompecabezas[3])
    for ax in fig.get_axes():
        ax.label_outer()
    plt.show
        
def desordenar():
    global rompecabezas
    global juego
    lista_random = (sample(rompecabezas,4))
    longitud = len(rompecabezas)
    for i in range(longitud):
        juego.append(lista_random[i])
    #dibujar(juego,"---DESORDENADO---")
    
def mover_piezas():
    global juego
    aux_juego = juego[:]
    print("Las piezas son:\n0 2\n1 3")
    opcion_1 = (int(input("Escoge la piza a mover: ")))
    opcion_2 = (int(input("Escoge la pieza a intercambiar: ")))
    juego[opcion_2] = juego[opcion_1]
    juego[opcion_1] = aux_juego[opcion_2]
    dibujar(juego, "Inicia el Juego")
    
    
partes_4(mapache)