import numpy as np
import matplotlib.pyplot as plt


def bitwise_and(img1, img2):
    # Check the dimensions of images
    if img1.shape != img2.shape:
        raise ValueError("Images must have the same dimensions")
    # Initialize result image
    result = np.zeros(img1.shape, dtype=np.uint8)

    # Apply bitwise AND to each pixel
    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):
            result[i, j] = img1[i, j] & img2[i, j]

    return result


def bitwise_or(img1, img2):
    # Check the dimensions of images
    if img1.shape != img2.shape:
        raise ValueError("Images must have the same dimensions")
    # Initialize result image
    result = np.zeros(img1.shape, dtype=np.uint8)

    # Apply bitwise OR to each pixel
    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):
            result[i, j] = img1[i, j] | img2[i, j]

    return result


def bitwise_not(img):
    # Initialize result image
    result = np.zeros(img.shape, dtype=np.uint8)

    # Apply bitwise NOT to each pixel
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            result[i, j] = ~img[i, j]

    return result



img1 = np.zeros((100, 100), dtype=np.uint8)
img1[30:70, 30:70] = 255


img2 = np.zeros((100, 100), dtype=np.uint8)
img2[30:70, 50:90] = 255


# result_img = bitwise_or(img1, img2)
result_img = bitwise_not(img1)
fig, axs = plt.subplots(1, 3, figsize=(15, 5))
axs[0].imshow(img1, cmap='gray')
axs[0].set_title('Image 1')
axs[0].axis('off')

axs[1].imshow(img2, cmap='gray')
axs[1].set_title('Image 2')
axs[1].axis('off')

axs[2].imshow(result_img, cmap='gray')
axs[2].set_title('Result of bitwise_and')
axs[2].axis('off')

plt.show()
