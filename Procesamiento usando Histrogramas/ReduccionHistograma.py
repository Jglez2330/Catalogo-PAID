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

def reducirHistograma(img_path, smin, smax):
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
    f = histograma(image)
    (image_final, r) = reducirHistograma("../Imagenes/peppers.jpeg", 75, 127)
    fig = plt.subplots(1, 1)
    #plt.bar(f, np.max(f)+ 10)
    plt.imshow(image_final, cmap='gray', vmin=0, vmax=255)
    plt.show()