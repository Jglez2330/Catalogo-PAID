import numpy as np
import cv2
import scipy.io

A = cv2.imread('../../Imagenes/boat.jpg', cv2.IMREAD_GRAYSCALE)
A = np.double(A)

m, n = np.shape(A)

B = np.zeros((m, n))

c = 0.5
b = 10

B = c * A + b

cv2.imwrite("boat.jpg", B)
