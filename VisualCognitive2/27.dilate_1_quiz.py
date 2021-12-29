# [Quiz] face 객체를 얻어내는 과정을 좀 더 단순화하여 구현해보자.
# 1. 이미지를 grayscale로 읽고, 이를 이진화한 mask를 생성
# 2. mask를 delate하고, unmasking하여 백그라운만의 평균 값을 취함
# 3. mask를 침식팽창하여 노이즈를 제거한 객체 이미지 윤곽 mask를 생성
# 4. 윤곽 mask와 윤곽 unmask를 이용하여 face와 backgraound를 결합

import cv2 as cv
import numpy as np

img = cv.imread('face_with_noise.png')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, mask = cv.threshold(img_gray, 100, 255, cv.THRESH_BINARY)
unmask = cv.bitwise_not(mask)

# generate denoised images - delated face mask
mask_eroded_dilated = cv.dilate(cv.erode(mask, None, iterations=3), None, iterations=3)
mask_eroded_dilated_not = cv.bitwise_not(mask_eroded_dilated)
# unmask_eroded_dilated = cv.dilate(cv.erode(unmask, None, iterations=3), None, iterations=3)


face = cv.bitwise_and(img, img, mask=mask_eroded_dilated)
masked_bg = cv.bitwise_and(img, img, mask=unmask)
masked_bg_close = cv.erode(cv.dilate(masked_bg, None, iterations=6), None, iterations=6)
final_bg = cv.bitwise_and(masked_bg_close, masked_bg_close, mask=mask_eroded_dilated_not)
img_without_noise = cv.add(face, final_bg)

# face_without_noise = cv.imread('face_without_noise.png')
# print('Success =', np.array_equal(img_without_noise, face_without_noise))

cv.imshow('img', img)
# cv.imshow('img_gray', img_gray)
# cv.imshow('mask', mask)
# cv.imshow('mask_dilated', mask_dilated)
# cv.imshow('mask_eroded', mask_eroded)
# cv.imshow('mask_eroded_dilated', mask_eroded_dilated)
# cv.imshow('mask_eroded_dilated_not', mask_eroded_dilated_not)
# cv.imshow('face', face)
# cv.imshow('unmask_eroded_dilated', unmask_eroded_dilated)
cv.imshow('img_without_noise', img_without_noise)

cv.waitKey()