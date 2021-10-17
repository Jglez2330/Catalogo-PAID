import matplotlib.pyplot as plt
import numpy as np
from scipy.stats.mstats import gmean
import cv2


def geometric_mean_filter(image, kernel_size):
    """
    This function applies the geometrix mean filter to an image in array format
    :param image: array_like representing the image
    :param kernel_size: tuple representing the kernel size
    :return: array_like representing the image with the geometric mean filter 
    """

    (height, width) = image.shape

    blank_image = np.zeros((height, width), np.uint8)
    for i in range(width):
        for j in range(height):
            blank_image[j, i] = geometric_mean_filter_aux(
                image, kernel_size, i, j)
    return blank_image


def geometric_mean_filter_aux(Imagen, window, coordena_x, coordena_y):
    """
    Auxilary function for the geometric mean calculation, get a submatrix that will act as a kernel for the image
    :param Imagen: Array (numpy) representing the image
    :param window: Size of the kernel or window
    :param coordena_x: Coordinate for the submatrix center in x
    :param coordena_y: Coordinate for the submatrix center in y
    :return: An array with the geometric mean values for each channel
    """

    kernel = cv2.getRectSubPix(
        Imagen, window, (coordena_x, coordena_y)).clip(1, 255)
    prod = np.prod(kernel) + 1
    return prod**(1/(window[0]*window[1]))


img_path = "./Imagenes/chest.jpg"

image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
[m, n] = image.shape
noise = np.random.normal(loc=30, scale=30, size=(m, n))

image_with_noise = image + noise
kernel_size = (3, 3)

image_with_noise = np.float32(image_with_noise).clip(0, 255)
filtered_image = geometric_mean_filter(image_with_noise, kernel_size)


plt.imshow(image, cmap='gray', vmin=0, vmax=255)
plt.title("Imagen original")
plt.show()

plt.imshow(image_with_noise, cmap='gray', vmin=0, vmax=255)
plt.title("Imagen con ruido")
plt.show()

plt.imshow(filtered_image, cmap='gray', vmin=0, vmax=255)
plt.title("Imagen con filtro")
plt.show()
