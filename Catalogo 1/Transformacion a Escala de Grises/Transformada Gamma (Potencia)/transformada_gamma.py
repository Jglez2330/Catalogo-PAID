import matplotlib.pyplot as plt
import numpy as np
import cv2

def transformacionGamma(c, gamma):
    # Esta funcion aplica una transformacion gamma (potencial) a una imagen en 
    # escala de grises con el fin de modificar el brillo de la imagen
    # esta funcion estrecha los valores oscura y amplia los valores claros
    # Parametros de entrada: c = constante que al ser igual a 1 permite el
    #                        comportamiento descrito de la función
    #                        gamma = constante que al ser mayor que uno, 
    #                        aclara la imagen, al ser igual a 1, la imagen 
    #                        se mantiene igual y al encontrarse entre 0 y 1,
    #                        se oscurece la imagen

    A = cv2.imread('../../Imagenes/boat.jpg', cv2.IMREAD_GRAYSCALE)
    A = np.double(A)

    m, n = np.shape(A)

    B = np.zeros((m, n))

    B = c * (A ** gamma)

    B = np.uint8(B)
    cv2.imwrite("boat.jpg", B)

    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.imshow(A, cmap='gray')
    ax1.set_title('Imagen Original')
    ax2.imshow(B, cmap='gray', vmin=0, vmax=255)
    ax2.set_title('Imagen Modificada')

    plt.show()

    return

# Ejemplo
transformacionGamma(1, 0.7)