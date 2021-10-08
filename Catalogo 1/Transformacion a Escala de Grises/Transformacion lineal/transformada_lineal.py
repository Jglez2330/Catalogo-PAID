import matplotlib.pyplot as plt
import numpy as np
import cv2

def transformacionLineal(c, b):
    # Esta funcion aplica una transformacion lineal a una imagen en escala de grises
    # con el fin de modificar el brillo de la imagen
    # Parametros de entrada: c = constante que al ser mayor que 1, aclara el pixel 
    #                            y al encontrarse entre 0 y 1 oscurece el pixel
    #                        b = constante que al ser mayor que cero, aclara el pixel 
    #                            y al ser menor que cero, oscurece el pixel

    A = cv2.imread('../../Imagenes/boat.jpg', cv2.IMREAD_GRAYSCALE)
    A = np.double(A)

    m, n = np.shape(A)

    B = np.zeros((m, n))

    B = c * A + b

    cv2.imwrite("boat.jpg", B)
    
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.imshow(A, cmap='gray')
    ax1.set_title('Imagen Original')
    ax2.imshow(B, cmap='gray', vmin=0, vmax=255)
    ax2.set_title('Imagen Modificada')

    plt.show()

    return

# Ejemplo
transformacionLineal(0.5, 10)