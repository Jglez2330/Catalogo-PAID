import numpy as np
import cv2
import matplotlib.pyplot as plt

A = cv2.imread('../../Imagenes/scissor.jpg', cv2.IMREAD_GRAYSCALE)
B = np.ones((2, 2), np.uint8)
C = np.bitwise_and(A, np.invert(cv2.erode(A, B)))

fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
ax1.imshow(A, cmap='gray')

ax2.imshow(B, cmap='gray')

ax3.imshow(C, cmap='gray')

plt.show()