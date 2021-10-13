import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import cv2

def filtroSobel():
    # Esta funcion aplica el filtro sobel a una imagen en escala de grises

    A = cv2.imread('../../Imagenes/baby_yoda.jpg', cv2.IMREAD_GRAYSCALE)

    A = np.double(A)

    Bx = np.matrix('-1 -2 -1; 0 0 0; 1 2 1')
    By = np.matrix('-1 0 1; -2 0 2; -1 0 1')

    Cx = signal.convolve2d(A, Bx, mode='same')
    Cy = signal.convolve2d(A, By, mode='same')

    C = np.sqrt(np.add(np.power(Cx, 2), np.power(Cy, 2)))

    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.imshow(A, cmap='gray')
    ax1.set_title('Imagen Original')
    ax2.imshow(C, cmap='gray', vmin=0, vmax=255)
    ax2.set_title('Imagen Modificada')

    plt.show()

    return

# Ejemplo
filtroSobel()