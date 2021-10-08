import numpy as np
import cv2
import matplotlib.pyplot as plt


def dilatacion(A, r):
    m, n = np.shape(A)
    Y = np.zeros((m, n), dtype=np.uint8)

    for i in range(m):
        for j in range(n):
            sup = i - r
            inf = i + r
            izq = j - r
            der = j + r

            sup = 0 if sup < 0 else sup
            inf = m - 1 if inf > (m - 1) else inf
            izq = 0 if izq < 0 else izq
            der = n - 1 if der > (n - 1) else der
            Y[i, j] = np.max(A[sup:inf, izq:der][:])
    return Y


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


def apertura(A, r):
    return dilatacion(erosion(A, r), r)


A = cv2.imread('../../Imagenes/huella.jpg', cv2.IMREAD_GRAYSCALE)
A = np.array(A, dtype=np.uint8)
# B = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], dtype=np.uint8)
r = 1
C = apertura(A, r)

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.imshow(A, cmap='gray')

ax2.imshow(C, cmap='gray')

plt.show()
