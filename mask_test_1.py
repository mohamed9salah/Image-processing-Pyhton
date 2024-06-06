import cv2
import numpy as np


image = cv2.imread('images/2.png')


mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (50, 50), (200, 200), 255, -1)


result = cv2.bitwise_and(image, image, mask=mask)


cv2.imshow('Mask', mask)
cv2.imshow('Original Image', image)
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
