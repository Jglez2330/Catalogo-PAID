import numpy as np
import cv2
import scipy.io
import json

def proyeccion_bilateral(A, r, p, n):
    Y2 = np.random.randn(n, r)
    for k in range(p):
        Y1 = A @ Y2
        Y2 = np.transpose(A) @ Y1
    Q, r_value = np.linalg.qr(Y2)
    Q = Q[:, 0:r]
    B = A @ Q
    C = np.transpose(Q)
    A = B @ C
    return A, B, C

def save_matrices(B, C, nameB, nameC):
    a_file = open(f"{nameB}.mat", "w")
    B = cv2.normalize(B, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    C = cv2.normalize(C, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    for row in B:
        np.savetxt(a_file, row)
    a_file.close()

    a_file = open(f"{nameC}.mat", "w")
    for row in C:
        np.savetxt(a_file, row)
    a_file.close()

I_color = cv2.imread('../../Imagenes/Barbara.png')
m, n, c = np.shape(I_color)
Ar = I_color[:, :, 0]
Ag = I_color[:, :, 1]
Ab = I_color[:, :, 2]

r = 50
p = 5

Arr, Brr, Crr = proyeccion_bilateral(Ar, r, p, n)
Agr, Bgr, Cgr = proyeccion_bilateral(Ag, r, p, n)
Abr, Bbr, Cbr = proyeccion_bilateral(Ab, r, p, n)

save_matrices(Brr, Crr, 'Br', 'Cr')
save_matrices(Bgr, Cgr, 'Bg', 'Cg')
save_matrices(Bbr, Cbr, 'Bb', 'Cb')

A_final = np.dstack((Arr, Agr, Abr))
cv2.imwrite("Barbara_comprimida.png", A_final)
