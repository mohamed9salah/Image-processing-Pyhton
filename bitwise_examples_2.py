from bitwise_operations import *
import cv2

img1 = cv2.imread('images/night_sky.jpg')
img2 = cv2.imread('images/moon.jpeg')

print('Image 1 shape:', img1.shape)
print('Image 2 shape:', img2.shape)

img_2_shape = img2.shape
roi = img1[0:img_2_shape[0], 0:img_2_shape[1]]
cv2.imshow('roi', roi)
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)

mask_inv = bitwise_not(mask)

# Now black-out the area of moon in ROI
img1_bg = bitwise_and(roi, roi, mask=mask_inv)

# Take only region of moon from moon image.
img2_fg = bitwise_and(img2, img2, mask=mask)
cv2.imshow('img2_fg', img2_fg)
# Put moon in ROI and modify the main image
dst = cv2.add(img1_bg, img2_fg)
img1[0:img_2_shape[0], 0:img_2_shape[1]] = dst


# Create resizable windows for our display images
cv2.namedWindow('img1_bg', cv2.WINDOW_NORMAL)
cv2.namedWindow('img2_fg', cv2.WINDOW_NORMAL)
cv2.namedWindow('mask', cv2.WINDOW_NORMAL)
cv2.namedWindow('mask_inv', cv2.WINDOW_NORMAL)
cv2.namedWindow('dst',cv2.WINDOW_NORMAL)
cv2.namedWindow('res', cv2.WINDOW_NORMAL)

cv2.imshow('mask', mask)
cv2.imshow('mask_inv', mask_inv)
cv2.imshow('img1_bg', img1_bg)
cv2.imshow('img2_fg', img2_fg)
cv2.imshow('dst', dst)
cv2.imshow('res', img1)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
