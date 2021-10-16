import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import cv2

def enfatizarBordes(c):
    # Esta funcion aplica el filtro laplaciano a una imagen en escala de grises
    # con el fin de enfatizar sus bordes
    # Parametros de entrada: c = coeficiente que determina que tan
    #                        marcado se muestran los bordes

    A = cv2.imread('../../Imagenes/baby_yoda.jpg', cv2.IMREAD_GRAYSCALE)

    A = np.double(A)
    B = np.matrix('1 1 1; 1 -8 1; 1 1 1')
    C = signal.convolve2d(A, B, mode='same')
   
    D = np.add(A, np.dot(c, C))

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
    ax1.imshow(A, cmap='gray')
    ax1.set_title('Imagen Original')
    ax2.imshow(C, cmap='gray', vmin=0, vmax=255)
    ax2.set_title('Bordes de la Imagen')
    ax3.imshow(D, cmap='gray', vmin=0, vmax=255)
    ax3.set_title('Imagen Modificada')

    plt.show()

    return

# Ejemplo
enfatizarBordes(5)