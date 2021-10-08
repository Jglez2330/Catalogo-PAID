import numpy as np
import cv2
import matplotlib.pyplot as plt
import math


def rippling(A, Lx, Ly):
    """
    Esta funcion que crea una animacion de onda en una imagen
    Sintaxis: rippling(A, Lx, Ly)
    Entrada:
        A -> Matriz de una imagen
        Lx -> Longitud en X de la onda
        Ly -> Longitud en Y de la onda
    Salida:
        Animacion del rippling de la imagen de entrada
    """
    m, n, c = np.shape(A)
    fig, (ax1, ax2) = plt.subplots(1, 2)
    im1 = ax1.imshow(cv2.cvtColor(A, cv2.COLOR_BGR2RGB))
    ax1.set_title('Imagen Original')
    ax2.imshow(cv2.cvtColor(A, cv2.COLOR_BGR2RGB))
    ax2.set_title('Transformación Rippling')
    plt.ion()
    for k in range(5, 200, 5):
        Ax = k
        Ay = k
        B = np.zeros((m, n, c))
        for i in range(m):
            for j in range(n):
                new_x = round(i + Ax * math.sin(2*math.pi*j/Lx))
                new_y = round(j + Ay * math.sin(2*math.pi*i/Ly))
                if 0 < new_x < m and 0 < new_y < n:
                    B[new_x, new_y, :] = A[i, j, :]
        ax2.imshow(cv2.cvtColor(np.uint8(B), cv2.COLOR_BGR2RGB))
        plt.pause(1/160)
        plt.show()
    plt.ioff()


I_color = cv2.imread('../../Imagenes/shrek.jpg')
rippling(I_color, 1, 100)
