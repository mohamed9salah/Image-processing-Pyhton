import cv2
import numpy as np


mask_image = cv2.imread('images/1.png', cv2.IMREAD_GRAYSCALE)


_, mask = cv2.threshold(mask_image, 128, 255, cv2.THRESH_BINARY)


image = cv2.imread('images/2.png')


if mask.shape == image.shape[:2]:

    result = cv2.bitwise_and(image, image, mask=mask)

    cv2.imshow('Mask', mask)
    cv2.imshow('Original Image', image)
    cv2.imshow('Result', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("The dimensions of the mask and the image do not match!")
