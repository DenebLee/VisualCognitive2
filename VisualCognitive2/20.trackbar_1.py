# multi trackbars
# - BGR 각각에 대해 trackbar를 적용

import cv2 as cv
import numpy as np


def onChangeB(val):
    print('B:', val)
    img[:,:,0] = val
    cv.imshow('img', img)


def onChangeG(val):
    print('G:', val)
    img[:,:,1] = val
    cv.imshow('img', img)


def onChangeR(val):
    print('R:', val)
    img[:,:,2] = val
    cv.imshow('img', img)


init_val = 128
img = np.full((480,640,3), init_val, np.uint8)
cv.namedWindow('img')
cv.createTrackbar('R', 'img', init_val, 255, onChangeR)
cv.createTrackbar('G', 'img', init_val, 255, onChangeG)
cv.createTrackbar('B', 'img', init_val, 255, onChangeB)

cv.imshow('img', img)
cv.waitKey()

# [Quiz] 동일한 회색 컬러 이미지를 HSV 포맷으로 변경한 후,
# 각 값을 trackbar로 변경할 때 나타나는 컬러 이미지를 출력하자.