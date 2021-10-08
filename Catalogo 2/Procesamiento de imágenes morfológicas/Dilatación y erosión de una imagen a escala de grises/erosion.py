import numpy as np
import cv2
import matplotlib.pyplot as plt


def erosion(A, r):
    m, n = np.shape(A)
    Y = np.zeros((m, n), dtype=np.uint8)

    for i in range(m):
        for j in range(n):
            sup = i - r
            inf = i + r
            izq = j - r
            der = j + r

            sup = 0 if sup < 0 else sup
            inf = m-1 if inf > (m-1) else inf
            izq = 0 if izq < 0 else izq
            der = n-1 if der > (n-1) else der
            Y[i, j] = np.min(A[sup:inf, izq:der][:])
    return Y


A = cv2.imread('../../Imagenes/cuadro_raro.jpg', cv2.IMREAD_GRAYSCALE)
A = np.array(A, dtype=np.uint8)
r = 1
C = erosion(A, r)


fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.imshow(A, cmap='gray')

ax2.imshow(C, cmap='gray')

plt.show()
