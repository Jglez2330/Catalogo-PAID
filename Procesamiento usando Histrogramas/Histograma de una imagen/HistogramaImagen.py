import cv2
import numpy as np
import matplotlib.pyplot as plt


def histograma(img_path):
    image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    (height, width) = image.shape
    hist = np.zeros(256, np.uint32)
    for i in range(width):
        for j in range(height):
            hist[image[i, j]] += 1
    return hist


if __name__ == '__main__':
    r = histograma("../Imagenes/boat.jpg")
    fig = plt.subplots(1, 1)
    plt.plot(r)
    plt.show()


    

    