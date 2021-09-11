import cv2
import numpy as np
import matplotlib.pyplot as plt


def histograma(image):
    (height, width) = image.shape
    hist = np.zeros(256, np.uint32)
    for i in range(width):
        for j in range(height):
            hist[image[i, j]] += 1
    return hist

def estirarHistograma(img_path):
    image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)



    rmin = np.min(image)
    rmax = np.max(image)

    result_image = (255/(rmax - rmin)) * (image - rmin)

    return (result_image, histograma(result_image.astype(int)))
if __name__ == '__main__':
    image = cv2.imread("../Imagenes/peppers.jpeg", cv2.IMREAD_GRAYSCALE)
    f = histograma(image)
    (image_final, r) = estirarHistograma("../Imagenes/peppers.jpeg")
    fig = plt.subplots(1, 1)
    #plt.bar(f, np.max(f)+ 10)
    plt.imshow(image_final, cmap='gray', vmin=0, vmax=255)
    plt.show()