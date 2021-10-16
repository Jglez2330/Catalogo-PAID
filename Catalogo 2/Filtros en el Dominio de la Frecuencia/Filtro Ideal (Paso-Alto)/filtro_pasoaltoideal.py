import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import cv2

def imageConvert2Show(A):
    Amin = np.min(A)
    Amax = np.max(A)
    return np.uint8(np.dot(np.divide(np.subtract(A, Amin), np.subtract(Amax, Amin)), 255))

def filtroPasoAltoIdeal(D0):
    # Esta funcion aplica el filtro paso alto ideal a una imagen en escala de grises
    # Parametros de entrada: D0 = valor del radio del
    #                        circulo del filtro paso alto ideal

    fig, ax = plt.subplots(3, 2)

    A = cv2.imread('../../Imagenes/edificio_china.jpg', cv2.IMREAD_GRAYSCALE)
    ax[0, 0].imshow(A, cmap='gray')
    ax[0, 0].set_title('Imagen Original')

    A = np.double(A)
    F = np.fft.fft2(A)
    ax[0, 1].imshow(imageConvert2Show(np.log(1 + np.abs(F))), cmap='gray')
    ax[0, 1].set_title('Imagen Fourier') 
    
    Fshift = np.fft.fftshift(F)
    ax[1, 0].imshow(imageConvert2Show(np.log(1 + np.abs(Fshift))), cmap='gray')
    ax[1, 0].set_title('Imagen Fourier (shift)') 

    m, n = A.shape
    D = np.zeros((m ,n))
    for u in range(1, m + 1):
        for v in range(1, n + 1):
            D[u - 1, v - 1] = np.sqrt((u - (m / 2)) ** 2 + (v - (n / 2)) ** 2)

    Fmask = np.greater(D, D0)
    ax[1, 1].imshow(imageConvert2Show(np.log(1 + np.abs(Fmask))), cmap='gray')
    ax[1, 1].set_title('Mascara Fourier')

    Fmask = np.fft.fftshift(Fmask)

    Fresult = np.fft.fftshift(np.multiply(F, Fmask))
    ax[2, 0].imshow(imageConvert2Show(np.log(1 + np.abs(Fresult))), cmap='gray')
    ax[2, 0].set_title('Resultado Fourier')

    Fresult = np.fft.fftshift(Fresult)

    B = np.fft.ifft2(Fresult)
    B = np.uint8(np.abs(B))
    ax[2, 1].imshow(B, cmap='gray')
    ax[2, 1].set_title('Resultado')

    plt.show()

    return

# Ejemplo
filtroPasoAltoIdeal(30)