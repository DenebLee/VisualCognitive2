# [Quiz] leanna.bmp 파일을 grayscale로 읽고, 이에 대한 노이이즈를 추가한 후
# - 검은색 또는 하얀색으로 전체 픽셀의 10%를 대체한 노이즈를 numpy스럽게 생성
# medianBlur와 bilateral 필터를 각각 적용하여 가장 적절한 파라미터를 트랙바로 확인해보자.

import numpy as np
import cv2
import random

src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

# 검은색 또는 하얀색으로 전체 픽셀의 10%를 대체한 노이즈를 생성
# for i in range(0, int(src.size / 10)):
#     x = random.randint(0, src.shape[1] - 1)
#     y = random.randint(0, src.shape[0] - 1)
#     src[x, y] = (i % 2) * 255

bools = np.random.choice([True, False], src.shape, p=[.1, .9])
noises = np.random.choice([0, 255], bools.sum())
src[bools] = noises

vars, varr, mfsize = 100, 50, 1
blf = cv2.bilateralFilter(src, -1, vars/10, varr/10)
med = cv2.medianBlur(src, 2*mfsize+1)

cv2.imshow('src', src)
cv2.imshow('bilateral', blf)
cv2.imshow('medianBlur', med)

def onChangeVars(var):
    global vars, varr, blf
    vars = var
    blf = cv2.bilateralFilter(src, -1, vars/10, varr/10)
    cv2.imshow('bilateral', blf)

def onChangeVarr(var):
    global vars, varr, blf
    varr = var
    blf = cv2.bilateralFilter(src, -1, vars/10, varr/10)
    cv2.imshow('bilateral', blf)

def onChangeFsize(var):
    global mfsize
    mfsize = var
    med = cv2.medianBlur(src, 2 * mfsize + 1)
    cv2.imshow('medianBlur', med)

cv2.createTrackbar('vars*10', 'bilateral', vars, 200, onChangeVars)
cv2.createTrackbar('varr*10', 'bilateral', varr, 100, onChangeVarr)
cv2.createTrackbar('mfsize//2', 'medianBlur', mfsize, 4, onChangeFsize)

cv2.waitKey()
cv2.destroyAllWindows()

# 결론적으로 :
# - bilateral은 white noise에 강하고, 이상치에는 동작하지 못한다.
# - medianBlur는 white noise에도 적당히 강하고, 이상치에도 잘 동작한다.

# [Quiz] leanna.bmp 파일을 grayscale로 읽고, 이에 대한 노이이즈를 추가한 후
# - 픽셀 전체적으로 평균이 0이고, 표준편차가 3인 노이즈
# medianBlur와 bilateral 필터를 각각 적용하여 가장 적절한 파라미터를 트랙바로 확인해보자.