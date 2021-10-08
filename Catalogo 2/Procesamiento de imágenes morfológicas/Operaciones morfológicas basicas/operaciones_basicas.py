import numpy as np
import cv2
import matplotlib.pyplot as plt


def plot(A, B, C, U, I, D, Texto):
    fig, ((ax1, ax2, ax3), (ax4, ax5, ax6), (ax7, ax8, ax9), (ax10, ax11, ax12)) = plt.subplots(4, 3)
    ax1.imshow(Texto, cmap='gray')
    ax3.imshow(C, cmap='gray')
    ax1.set_title('Complemento')

    ax4.imshow(A, cmap='gray')
    ax5.imshow(B, cmap='gray')
    ax6.imshow(U, cmap='gray')
    ax4.set_title('Union')

    ax7.imshow(A, cmap='gray')
    ax8.imshow(B, cmap='gray')
    ax9.imshow(I, cmap='gray')
    ax7.set_title('Interseccion')

    ax10.imshow(A, cmap='gray')
    ax11.imshow(B, cmap='gray')
    ax12.imshow(D, cmap='gray')
    ax10.set_title('Diferencia')
    plt.show()


def complemento(A):
    return np.invert(A)


def interseccion(A, B):
    return np.bitwise_and(A, B)


def union(A, B):
    return np.bitwise_or(A, B)


def diferencia(A, B):
    return np.bitwise_and(A, np.invert(B))


Texto = cv2.imread('../../Imagenes/fundamental.jpg', cv2.IMREAD_GRAYSCALE)
C = complemento(Texto)

A = cv2.imread('../../Imagenes/scissor.jpg', cv2.IMREAD_GRAYSCALE)
B = cv2.imread('../../Imagenes/block.jpg', cv2.IMREAD_GRAYSCALE)

I = interseccion(A, B)
U = union(A, B)
D = diferencia(A, B)

plot(A, B, C, U, I, D, Texto)
