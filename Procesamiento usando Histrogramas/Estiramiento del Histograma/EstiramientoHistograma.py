import cv2
import numpy as np
import matplotlib.pyplot as plt


def histograma(image):
    """
    Esta funcion calcula el histograma de una imagen

    Sintaxis: histograma(image)

    Entrada:
        img_path -> Imagen a calcular el histograma

    Salida:
        Array de tamaño de 256 con el histograma

    """
    (height, width) = image.shape
    hist = np.zeros(256, np.uint32)
    for i in range(width):
        for j in range(height):
            hist[image[j, i]] += 1
    return hist


def estirarHistograma(img_path):
    """
    Esta funcion calcula una imagen con el histograma estirado

    Sintaxis: estirarHistograma(img_path)

    Entrada:
        img_path -> direccion de la imagen a calcular el histograma

    Salida:
        Imagen del tamaño original con el histograma estirado
    """
    image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    rmin = np.min(image)
    rmax = np.max(image)

    result_image = (255 / (rmax - rmin)) * (image - rmin)
    result_image = result_image.astype(np.uint8)

    return (result_image, histograma(result_image))


if __name__ == '__main__':
    image_ori = cv2.imread("../Imagenes/sydney.jpeg", cv2.IMREAD_GRAYSCALE)

    (image_final, r) = estirarHistograma("../Imagenes/sydney.jpeg")

    fig, axs = plt.subplots(2, 2)

    axs[0, 0].imshow(image_ori, cmap='gray', vmin=0, vmax=255)
    axs[0, 0].set_title('Imagen Original')

    hist_ori = histograma(image_ori)
    axs[1, 0].plot(hist_ori)
    axs[1, 0].set_title('Histograma Original')

    axs[0, 1].imshow(image_final, cmap='gray', vmin=0, vmax=255)
    axs[0, 1].set_title('Imagen Modificada')

    axs[1, 1].plot(r)
    axs[1, 1].set_title('Histograma Estirado')

    plt.show()