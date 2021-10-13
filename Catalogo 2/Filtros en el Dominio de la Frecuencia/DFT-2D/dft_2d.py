import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import cv2

def imageConvert2Show(A):
    Amin = np.min(A)
    Amax = np.max(A)
    return np.uint8(np.dot(np.divide(np.subtract(A, Amin), np.subtract(Amax, Amin)), 255))

def dft2d():
    # Esta funcion calcula la transformada discreta de Fourier
    # de una imagen a escala de grises

    A = cv2.imread('../../Imagenes/paisaje.jpg', cv2.IMREAD_GRAYSCALE)
    m, n = A.shape

    A = np.double(A)
    F = np.zeros((m, n), dtype = 'complex_')

    for u in range(1, m + 1):
        for v in range(1, n + 1):
            for x in range(m):
                for y in range(n):
                    F[u - 1, v - 1] += A[x, y] * np.exp(-1 * 1j * 2 * np.pi * ((u * x / m) + (v * y / n)))

    Ffreq = np.log(1 + np.abs(F))
    Ffreq = imageConvert2Show(Ffreq)

    Fshift = np.log(1 + np.abs(np.fft.fftshift(F)))
    Fshift = imageConvert2Show(Fshift)

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
    ax1.imshow(A, cmap='gray')
    ax1.set_title('Imagen Espacial')
    ax2.imshow(Ffreq, cmap='gray')
    ax2.set_title('Imagen Frecuencia')
    ax3.imshow(Fshift, cmap='gray')
    ax3.set_title('Imagen Frecuencia Modulo')

    plt.show()

    return

# Ejemplo
dft2d()