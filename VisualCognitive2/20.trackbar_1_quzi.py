

# [Quiz] 동일한 회색 컬러 이미지를 HSV 포맷으로 변경한 후,
# 각 값을 trackbar로 변경할 때 나타나는 컬러 이미지를 출력하자.

import cv2 as cv
import numpy as np


def onChangeH(val):
    global imghsv
    print('H:', val)
    imghsv[:,:,0] = val
    img = cv.cvtColor(imghsv, cv.COLOR_HSV2BGR)
    cv.imshow('img', img)


def onChangeS(val):
    global imghsv
    print('S:', val)
    imghsv[:,:,1] = val
    img = cv.cvtColor(imghsv, cv.COLOR_HSV2BGR)
    cv.imshow('img', img)

def onChangeV(val):
    global imghsv
    print('V:', val)
    imghsv[:,:,2] = val
    img = cv.cvtColor(imghsv, cv.COLOR_HSV2BGR)
    cv.imshow('img', img)

init_H, init_S, init_V = 0, 0, 128
img = np.full((480,640,3), 128, np.uint8)
imghsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

cv.namedWindow('img')
cv.createTrackbar('H', 'img', init_H, 179, onChangeH)
cv.createTrackbar('S', 'img', init_S, 255, onChangeS)
cv.createTrackbar('V', 'img', init_V, 255, onChangeV)

cv.imshow('img', img)
cv.waitKey()