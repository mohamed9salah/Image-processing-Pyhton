import numpy as np
import cv2


def bitwise_and(img1, img2):
    # Check the dimensions of images
    if img1.shape != img2.shape:
        raise ValueError("Images must have the same dimensions")
    # Initialize result image
    result = np.zeros(img1.shape, dtype=np.uint8)

    # Apply bitwise AND to each pixel
    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):
            for k in range(img1.shape[2]):
                result[i, j, k] = img1[i, j, k] & img2[i, j, k]

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
            for k in range(img1.shape[2]):
                result[i, j, k] = img1[i, j, k] | img2[i, j, k]

    return result


def bitwise_xor(img1, img2):
    # Check the dimensions of images
    if img1.shape != img2.shape:
        raise ValueError("Images must have the same dimensions")
    # Initialize result image
    result = np.zeros(img1.shape, dtype=np.uint8)

    # Apply bitwise XOR to each pixel
    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):
            for k in range(img1.shape[2]):
                result[i, j, k] = img1[i, j, k] ^ img2[i, j, k]

    return result


def bitwise_not(img):
    # Initialize result image
    result = np.zeros(img.shape, dtype=np.uint8)

    # Apply bitwise NOT to each pixel
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(img.shape[2]):
                result[i, j, k] = ~img[i, j, k]

    return result


image1 = cv2.imread('images/1.png')
image2 = cv2.imread('images/2.png')

cv2.imshow('1st image', image1)
cv2.imshow('2nd image', image2)

result_and = bitwise_and(image1, image2)
cv2.imshow('AND', result_and)

result_or = bitwise_or(image1, image2)
cv2.imshow('OR', result_or)

result_xor = bitwise_xor(image1, image2)
cv2.imshow('XOR', result_xor)

result_not = bitwise_not(image2)
cv2.imshow('NOT', result_not)

cv2.waitKey(0)
cv2.destroyAllWindows()
