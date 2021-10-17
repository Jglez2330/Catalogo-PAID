import numpy as np
import cv2
import matplotlib.pyplot as plt


def mean_filter(imagen, kernel_size):
    """
    This function applies the mean filter of kernel_size to an image
    Sintaxis: mean_filter(image:image, kernel_size:tuple)
    Entrada:
        image -> Array_like representing the image
        kernel_size -> tuple with the dimensions of the kernel
    Salida:
        Array that represents the new image with the mean filter applied
    """
    (height, width) = imagen.shape
    blank_image = np.zeros((height, width), np.uint8)
    for i in range(width):
        for j in range(height):
            blank_image[j, i] = mean_filter_aux(imagen, kernel_size, i, j)
    return blank_image


def mean_filter_aux(Imagen, window, coordena_x, coordena_y):
    """
    Auxilary functio for the mean calculation, get a submatrix that will act as a kernel for the image
    :param Imagen: Array (numpy) representing the image
    :param window: Size of the kernel or window
    :param coordena_x: Coordinate for the submatrix center in x
    :param coordena_y: Coordinate for the submatrix center in y
    :return: An array with the mean values for each channel
    """
    kernel = cv2.getRectSubPix(Imagen, window, (coordena_x, coordena_y))
    return round(np.mean(kernel))


img_path = "./Imagenes/baby_yoda.jpg"

image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
[m, n] = image.shape
noise = np.random.normal(loc=30, scale=60, size=(m, n))

image_with_noise = image + noise
kernel_size = (17, 17)

filtered_image = mean_filter(image_with_noise, kernel_size)


plt.imshow(image, cmap='gray', vmin=0, vmax=255)
plt.title("Imagen original")
plt.show()


plt.imshow(image_with_noise, cmap='gray', vmin=0, vmax=255)
plt.title("Imagen con ruido")
plt.show()

plt.imshow(filtered_image, cmap='gray', vmin=0, vmax=255)
plt.title("Imagen con filtro")
plt.show()
