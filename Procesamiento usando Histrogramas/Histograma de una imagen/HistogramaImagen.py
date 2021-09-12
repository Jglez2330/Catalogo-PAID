import cv2
import numpy as np
import matplotlib.pyplot as plt


def histograma(img_path):
    """
    Esta funcion calcula el histograma de una imagen

    Sintaxis: histograma(img_path)

    Entrada:
        img_path -> direccion de la imagen a calcular el histograma

    Salida:
        Array de tamaño de 256 con el histograma

    """
    image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    (height, width) = image.shape
    hist = np.zeros(256, np.uint32)
    for i in range(width):
        for j in range(height):
            hist[image[j, i]] += 1
    return hist


if __name__ == '__main__':
    r = histograma("../Imagenes/boat.jpg")
    fig = plt.subplots(1, 1)
    plt.plot(r)
    plt.title("Histograma de la imagen")
    plt.show()


    

    