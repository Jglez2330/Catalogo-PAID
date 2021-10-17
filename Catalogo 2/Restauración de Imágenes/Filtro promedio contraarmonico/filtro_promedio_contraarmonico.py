import cv2
import matplotlib.pyplot as plt
import numpy as np

# Codigo obtenido de https://stackoverflow.com/users/4863031/shubham-pachori en https://stackoverflow.com/questions/22937589/how-to-add-noise-gaussian-salt-and-pepper-etc-to-image-in-python-with-opencv


def noisy(noise_typ, image):
    if noise_typ == "gauss":
        row, col, ch = image.shape
        mean = 0
        var = 0.1
        sigma = var**0.5
        gauss = np.random.normal(mean, sigma, (row, col, ch))
        gauss = gauss.reshape(row, col, ch)
        noisy = image + gauss
        return noisy
    elif noise_typ == "p":
        [row, col] = image.shape
        s_vs_p = 0.5
        amount = 0.04
        out = np.copy(image)
        # Salt mode

        # Pepper mode
        num_pepper = np.ceil(amount * image.size * (1. - s_vs_p))
        coords = [np.random.randint(0, i - 1, int(num_pepper))
                  for i in image.shape]
        out[coords] = 0
        return out
    elif noise_typ == "s":
        [row, col] = image.shape
        s_vs_p = 0.5
        amount = 0.04
        out = np.copy(image)
        # Salt mode
        num_salt = np.ceil(amount * image.size * s_vs_p)
        coords = [np.random.randint(0, i - 1, int(num_salt))
                  for i in image.shape]
        out[coords] = 1
        # Pepper mode
        return out
    elif noise_typ == "s&p":
        [row, col] = image.shape
        s_vs_p = 0.5
        amount = 0.04
        out = np.copy(image)
        # Salt mode
        num_salt = np.ceil(amount * image.size * s_vs_p)
        coords = [np.random.randint(0, i - 1, int(num_salt))
                  for i in image.shape]
        out[coords] = 1
        # Pepper mode
        num_pepper = np.ceil(amount * image.size * (1. - s_vs_p))
        coords = [np.random.randint(0, i - 1, int(num_pepper))
                  for i in image.shape]
        out[coords] = 0
        return out
    elif noise_typ == "poisson":
        vals = len(np.unique(image))
        vals = 2 ** np.ceil(np.log2(vals))
        noisy = np.random.poisson(image * vals) / float(vals)
        return noisy
    elif noise_typ == "speckle":
        row, col, ch = image.shape
        gauss = np.random.randn(row, col, ch)
        gauss = gauss.reshape(row, col, ch)
        noisy = image + image * gauss
        return noisy


def contraharmonic_mean_filter(image, kernel_dims, R):
    (m, n) = image.shape

    result = np.zeros((m, n), np.float)

    for i in range(n):
        for j in range(m):
            kernel = cv2.getRectSubPix(
                image, (kernel_dims, kernel_dims), (i, j))

            numerator_power = np.power(kernel, R + 1)
            denominator_power = np.power(kernel, R)

            numerator = np.sum(numerator_power)
            denominator = np.sum(denominator_power)
            if (denominator != 0):
                result[j, i] = numerator/denominator
    return result


img_path = "./Imagenes/peppers.jpeg"

image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
[m, n] = image.shape

noi = noisy("p", image/255)

kernel_size = (3, 3)
noi = np.float32(noi)
filtered_image = contraharmonic_mean_filter(noi, 3, 2.0)


#fig, axs = plt.subplots(1, 4)
#plt.imshow(image, cmap='gray', vmin=0, vmax=255)

plt.imshow(image, cmap='gray', vmin=0, vmax=255)
plt.title("Imagen original")
plt.show()


plt.imshow(noi, cmap='gray', vmin=0, vmax=1)
plt.title("Imagen con ruido")
plt.show()


plt.imshow(filtered_image, cmap='gray')
plt.title("Imagen con filtro")
plt.show()
