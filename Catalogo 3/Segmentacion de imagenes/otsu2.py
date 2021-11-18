from skimage import data
from skimage.filters import threshold_multiotsu
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("../Imagenes/imagen6.jpg", cv2.IMREAD_GRAYSCALE)
m, n = np.shape(image)

T = threshold_multiotsu(image)
print(T[0])
print(T[1])
out = np.zeros((m, n), dtype=np.double)

mask = (T[0]<image) & (image<T[1])
out[mask] = 0.5
out[image<=T[0]] = 0
out[T[1]<=image] = 1

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.imshow(image, cmap='gray')

ax2.imshow(out, cmap='gray')
plt.show()

