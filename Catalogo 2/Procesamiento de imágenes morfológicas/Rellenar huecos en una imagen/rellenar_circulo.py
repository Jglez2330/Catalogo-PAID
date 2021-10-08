import numpy as np
import cv2
import matplotlib.pyplot as plt

A = cv2.imread('../../Imagenes/circulo.jpg', cv2.IMREAD_GRAYSCALE)
A = np.array(A, dtype=np.uint8)
B = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], dtype=np.uint8)
m, n = np.shape(A)

fig, (ax1, ax2) = plt.subplots(1, 2)
Xk = np.zeros((m, n), np.uint8)
Xk[m//2, n//2] = 1
plt.ion()

for i in range(100):
    Xk = np.bitwise_and(cv2.dilate(Xk, B), np.invert(A))
    ax1.imshow(A, cmap='gray')
    ax2.imshow(Xk, cmap='gray')

    if i % 5 == 0:
        plt.pause(0.0000000001)
        plt.show()

plt.ioff()
