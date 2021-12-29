# sharpening: 이미지에서 중심 픽셀과 주변픽셀과의 차를 두드러지게 나타냄.

import cv2 as cv
import numpy as np

img = cv.imread('image/filter_blur.jpg')

# 자신과 주위 픽셀간 차를 증폭. 왜 5를 사용했을까?
kernel = np.array([[ 0, -1,  0],
                   [-1,  5, -1],
                   [ 0, -1,  0]])
# kernel = np.array([[ 0, 1,  0],
#                    [ 1, -3, 1],
#                    [ 0, 1,  0]])

img_filtered = cv.filter2D(img, -1, kernel)

print(img.shape, img.dtype)
print(img_filtered.shape, img_filtered.dtype)

cv.imshow('original', img)
cv.imshow('filtered', img_filtered)
cv.waitKey()

# [Quiz] sharping kernel의 중심값(현재 5)을 변경할 때의 변화를 그려보자.
# - [3, 8] 까지 for 문으로 그 변화를 waitKey(1000)에 따라 변경해보자.
# - 현재 십자모양에서 대각선 모양의 커널과 사각 모양의 커널도 시도해본다.
# crossK = np.array([[ -1,  0,  -1],
#                    [  0,  5,   0],
#                    [ -1,  0,  -1]])
# rectgK = np.array([[ -1, -1,  -1],
#                    [ -1,  5,  -1],
#                    [ -1, -1,  -1]])
# - 각각의 이미지 변화 모양에 대해 putText로 그 변화값을 그려본다.