import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import cv2

def filtroGaussiano(mascara):
    # Esta funcion aplica el filtro gaussiano a una imagen en escala de grises
    # Parametros de entrada: mascara = determina si la mascara a utilizar
    #                        es de 3x3 o 5x5

    A = cv2.imread('../../Imagenes/baby_yoda.jpg', cv2.IMREAD_GRAYSCALE)

    A = np.double(A)

    if (mascara == 3):
        B = np.matrix('1 2 1; 2 4 2; 1 2 1')
        B = np.dot(1/16, B)
    else:
        B = np.matrix('1 4 6 4 1; 4 16 24 16 4; 6 24 36 24 6; 4 16 24 16 4; 1 4 6 4 1')
        B = np.dot(1/256, B)

    C = signal.convolve2d(A, B, mode='same')
    C = np.uint8(C)

    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.imshow(A, cmap='gray')
    ax1.set_title('Imagen Original')
    ax2.imshow(C, cmap='gray')
    ax2.set_title('Imagen Modificada')

    plt.show()

    return

# Ejemplo
filtroGaussiano(5)