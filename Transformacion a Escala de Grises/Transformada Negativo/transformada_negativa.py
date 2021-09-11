import matplotlib.pyplot as plt
import numpy as np
import cv2

def transformacionNegativa():
    # Esta funcion aplica una transformacion negativa (la cual es un tipo de 
    # tranformacion lineal) a una imagen en escala de grises con el fin de 
    # mostrar una imagen negativa

    A = cv2.imread('../../Imagenes/boat.jpg', cv2.IMREAD_GRAYSCALE)
    A = np.double(A)

    m, n = np.shape(A)

    B = np.zeros((m, n))

    c = -1
    b = 255

    B = c * A + b

    cv2.imwrite("boat.jpg", B)

    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.imshow(A, cmap='gray')
    ax1.set_title('Imagen Original')
    ax2.imshow(B, cmap='gray')
    ax2.set_title('Imagen Modificada')

    plt.show()

    return

# Ejemplo
transformacionNegativa()