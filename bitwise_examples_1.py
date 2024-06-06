import np

from bitwise_operations import *
import cv2

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


mask = np.zeros(image1.shape[:2], dtype="uint8")
cv2.rectangle(mask, (50, 50), (200, 200), 255, -1)

mask_result_and = bitwise_and(image1, image2,mask=mask)
cv2.imshow('mask AND', mask_result_and)

mask_result_or = bitwise_or(image1, image2,mask=mask)
cv2.imshow('mask OR', mask_result_or)

mask_result_xor = bitwise_xor(image1, image2,mask=mask)
cv2.imshow('mask XOR', mask_result_xor)

mask_result_not = bitwise_not(image2,mask=mask)
cv2.imshow('mask NOT', mask_result_not)


cv2.waitKey(0)
cv2.destroyAllWindows()