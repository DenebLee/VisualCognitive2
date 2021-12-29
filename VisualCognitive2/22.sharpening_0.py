# sharpening의 기본적인 알고리즘은
# 1. 입력 이미지에서 bluring을 뺀 gradient를
# 2. 입력 이미지에 더하여 경계값을 증가시키는 방식이다.
# - X + w(X - Blur(x)) : w는 Gradient에 대한 가중치
# - (1+w)X - w Blur(x) : 이거 어디서 봤습니다. 어딜까요?

import cv2 as cv
import numpy as np

img = cv.imread('image/filter_blur.jpg')

weight = 5
img_blurred = cv.GaussianBlur(img, (5,5), 0)
img_sharpened = cv.addWeighted(img, weight+1, img_blurred, -weight, 0)

cv.imshow('img', img)
cv.imshow('img_blurred', img_blurred)
cv.imshow('img_sharpened', img_sharpened)
cv.waitKey()

# [Quiz] gaussina bluring에서 sigmaX = sigmaY를 0.1 ~ 4까지 조정하고,
# - weight를 0.1 ~ 2까지 조정할 때 변화되는 blur 이미지와 sharpened 이미지를
# - trackbar를 이용하여 그려보자.