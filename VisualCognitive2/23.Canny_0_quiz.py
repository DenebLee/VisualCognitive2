# [Quiz] 아래 범위에 걸쳐 trackbar를 생성하고 그 결과를 살펴보자.
# thresh1 = [0, 100], thresh2 = [50, 150]

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

def onChange1(val):
    global thresh1, thresh2, img, edge
    thresh1 = min(val, thresh2-1)
    cv.Canny(img, thresh1, thresh2, edge)
    cv.imshow('edge', edge)

def onChange2(val):
    global thresh1, thresh2, img, edge
    thresh2 = max(val, thresh1+1)
    cv.Canny(img, thresh1, thresh2, edge)
    cv.imshow('edge', edge)

cv.imshow('img', img)
cv.namedWindow('edge')
cv.imshow('edge', edge)
cv.createTrackbar('th1', 'edge', thresh1, 200, onChange1)
cv.createTrackbar('th2', 'edge', thresh2, 250, onChange2)

cv.waitKey()