from scipy import signal
import numpy as np


def convolution(matrixA, matrixB):
    """
    This function will calculate the convolution of 2 matrixes.
    :param matrixA: matrix A to convolution
    :param matrixB: matrix B to convolution
    :returns: result to convolution of A and B in the matrix
    """
    (m1, n1) = matrixA.shape
    (m2, n2) = matrixB.shape
    C = np.zeros((m1 + m2 - 1, n1 + n2 - 1), np.int32)
    for j in range(1, m1 + m2):
        for i in range(1, n1 + n2):
            C[j - 1, i - 1] = convolution_aux(matrixA, matrixB, i, j)

    return C


def convolution_aux(matrixA, matrixB, i, j):
    """
    This function calculates a 1D convolution of both submatrixes
    :param matrixA: matrix A to convolution
    :param matrixB: matrix B to convolution
    :param i: coordenate from the submatix in x axis
    :param j: coordenate from the submatix in y axis
    :returns: result to convolution of A and B in the matrix
    """
    (m1, n1) = matrixA.shape
    (m2, n2) = matrixB.shape
    start_p = np.maximum(1, j - m2 + 1)
    end_p = np.minimum(j, m1)
    result = 0
    for p in range(start_p, end_p + 1):
        start_q = np.maximum(1, i - n2 + 1)
        end_q = np.minimum(i, n1)
        temp = 0
        for q in range(start_q, end_q + 1):
            temp += matrixA[p - 1, q-1] * matrixB[j - p, i - q]
        result += temp
    return result


A = np.array([[-2, 1, 2], [1, 2, 3], [1, 1, 1]])
B = np.array([[-4, 3, 4], [0, 0, 0]])

print("Implementation of convolution")
convol = convolution(A, B)
print(convol)

A = np.array([[-2, 1, 2], [1, 2, 3], [1, 1, 1]])
B = np.array([[-4, 3, 4], [0, 0, 0]])

print("Scipy implementation of convolution")
convol = signal.convolve2d(A, B)
print(convol)
