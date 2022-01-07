# Canny edge detector : 9장 참고

import cv2 as cv
import numpy as np

img = cv.imread('image/edge_test1.jpg', cv.IMREAD_COLOR)

# thresh2 is recommended to be 2~3 times of thresh1
thresh1, thresh2 = 50, 120

# the order of thresh1 and thresh2 is irrelevant
# - Canny(img, lowthrh, highthrh, apertureSize = 3, L2gradient=False)
# - gradient를 구할 때 사용할 sobel kernel size
# - L2gradient=False 이므로, 기본적으로 L1 gradient를 사용한다.
edge = cv.Canny(img, thresh1, thresh2)

cv.imshow('img', img)
cv.imshow('edge', edge)
cv.waitKey()


# thresh1 = [0, 100], thresh2 = [50, 150]
