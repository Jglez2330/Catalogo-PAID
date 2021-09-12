import cv2
import numpy as np
import matplotlib.pyplot as plt


def histograma(image):
    """
    Esta funcion calcula el histograma de una imagen

    Sintaxis: histograma(img_path)

    Entrada:
        img_path -> direccion de la imagen a calcular el histograma

    Salida:
        Array de tamaño de 256 con el histograma

    """
    (height, width) = image.shape
    hist = np.zeros(256, np.uint32)
    for i in range(width):
        for j in range(height):
            hist[image[j, i]] += 1
    return hist

def reducirHistograma(img_path, smin, smax):
    """
    Esta funcion calcula una imagen con el histograma reducido

    Sintaxis: reducirHistograma(img_path, smin, smax)

    Entrada:
        img_path -> direccion de la imagen a calcular el histograma
        smin -> valor minimo limite de la reduccion
        smax -> valor maximo limite de la reduccion

    Salida:
        Imagen del tamaño original con el histograma reducido

    """
    image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    image = image.astype(float)

    rmin = np.min(image)
    rmax = np.max(image)

    if not (rmin < smin < rmax) or not (rmin < smax < rmax):
        return ([], [])

    result_image = ((smax - smin)/(rmax - rmin)) * (image - rmin) + smin

    return (result_image, histograma(result_image.astype(int)))
if __name__ == '__main__':
    image = cv2.imread("../Imagenes/peppers.jpeg", cv2.IMREAD_GRAYSCALE)
    
    (image_final, r) = reducirHistograma("../Imagenes/peppers.jpeg", 75, 127)
    fig, axs = plt.subplots(2, 2)

    axs[0, 0].imshow(image, cmap='gray')
    axs[0, 0].set_title('Imagen Original')

    hist_ori = histograma(image)
    axs[1, 0].plot(hist_ori)
    axs[1, 0].set_title('Histograma Original')

    axs[0, 1].imshow(image_final, cmap='gray', vmin=0, vmax=255)
    axs[0, 1].set_title('Imagen Modificada')

    axs[1, 1].plot(r)
    axs[1, 1].set_title('Histograma Reducido')
    plt.show()