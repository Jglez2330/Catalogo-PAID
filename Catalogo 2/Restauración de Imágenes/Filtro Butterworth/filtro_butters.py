def dist_matrix(img):
    """
    This function generates a matrix with the distance of each pixel from the center
    img -> image in a array_like representation
    result -> matrix of distances
    """
    [m, n] = img.shape
    result = np.zeros((m, n))

    n1 = n//2
    m1 = m//2
    for i in range(n):
        for j in range(m):
            result[j, i] = np.sqrt((i-n1)**2 + (j-m1)**2)
    return result


def butterworth_rejection_filter(image, w, d0, n):
    """
    This function applies a butterworth filter to an image to remove periodic noise
    :param image: array_like representing the image
    :param w: width of the ring of the filter
    :param d0: diameter of the outer ring
    :returns: array_like representing the image with the ideal reject band filter
    """
    [m, n] = image.shape
    dist = dist_matrix(image)

    alpha = ((dist*w)/(np.power(dist, 2) - d0**2))
    beta = 1 + np.power(alpha, 2*n)

    H = 1/beta

    Ffreq = np.fft.fft2(image)
    F_shift = np.fft.fftshift(Ffreq)

    frw1 = np.log(1 + np.abs(F_shift))

    freq_with_filter = np.fft.fftshift(np.fft.fftshift(H) * Ffreq)

    frw2 = np.log(1 + np.abs(freq_with_filter))

    result = np.fft.ifft2(np.fft.fftshift(freq_with_filter))
    result = np.abs(result)
    result *= (255.0/result.max())
    return [np.uint8(result), frw1, frw2]


A = cv2.imread('./Imagenes/camarografo.jpeg', cv2.IMREAD_GRAYSCALE)
B = cv2.imread('./Imagenes/ruido_periodico.jpeg', cv2.IMREAD_GRAYSCALE)
np.warnings.filterwarnings('ignore')

C = B*0.35 + A
[r, fwo, fw] = butterworth_rejection_filter(C, 8, 32, 5)

plt.imshow(C, cmap='gray')
plt.title("Imagen con ruido peridico")
plt.show()

plt.imshow(fwo, cmap='gray')
plt.title("Frecuencia imagen")
plt.show()

plt.imshow(r, cmap='gray')
plt.title("Imagen con filtro")
plt.show()

plt.imshow(fw, cmap='gray')
plt.title("Frecuencia imagen con filtro")
plt.show()
