# [Quiz] gaussina bluring에서 sigmaX = sigmaY를 0.1 ~ 4까지 조정하고,
# - weight를 0.1 ~ 2까지 조정할 때 변화되는 blur 이미지와 sharpened 이미지를
# - trackbar를 이용하여 그려보자.
# - 가중치 설정시 주의해야됨 값 누락없이 모든 범위 포함시키도록

import cv2 as cv
import numpy as np

img = cv.imread('image/filter_blur.jpg')

weight = 5  # 10*w
sigma = 10  # 10*sigma
img_blurred = cv.GaussianBlur(img, (0,0), sigma/10)
img_sharpened = cv.addWeighted(img, weight/10+1, img_blurred, -weight/10, 0)

cv.imshow('img', img)
cv.imshow('img_blurred', img_blurred)
cv.imshow('img_sharpened', img_sharpened)

def onChangeSigma(val):
    global img_blurred, img_sharpened, weight
    cv.GaussianBlur(img, (0,0), max(val/10, 0.05), dst=img_blurred)
    cv.imshow('img_blurred', img_blurred)
    cv.addWeighted(img, weight/10+1, img_blurred, -weight/10, 0, dst=img_sharpened)
    cv.imshow('img_sharpened', img_sharpened)

def onChangeWeight(val):
    global img_blurred, img_sharpened, weight
    weight = val
    cv.addWeighted(img, val/10+1, img_blurred, -val/10, 0, dst=img_sharpened)
    cv.imshow('img_sharpened', img_sharpened)

cv.createTrackbar('sigma*10', 'img_blurred', sigma, 40, onChangeSigma)
cv.createTrackbar('weight*10', 'img_sharpened', weight, 20, onChangeWeight)
cv.waitKey()
