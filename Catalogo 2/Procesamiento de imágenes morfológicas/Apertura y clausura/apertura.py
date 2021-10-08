import numpy as np
import cv2
import matplotlib.pyplot as plt


A = cv2.imread('../../Imagenes/huella.jpg', cv2.IMREAD_GRAYSCALE)
B = np.ones((2, 2), np.uint8)
C = cv2.morphologyEx(A, cv2.MORPH_OPEN, B)

fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
ax1.imshow(A, cmap='gray')

ax2.imshow(B, cmap='gray')

ax3.imshow(C, cmap='gray')

plt.show()


