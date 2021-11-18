import numpy as np
import cv2
import matplotlib.pyplot as plt
from skimage import data
from skimage.filters import threshold_otsu


A = cv2.imread("../Imagenes/imagen6.jpg", cv2.IMREAD_GRAYSCALE)
m, n = np.shape(A)

th = threshold_otsu(A)

B = np.zeros((m, n))
B[A > th] = 1
B[A <= th] = 0

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.imshow(A, cmap='gray')

ax2.imshow(B, cmap='gray')
plt.show()
