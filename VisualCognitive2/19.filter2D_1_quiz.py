# sharpening: 이미지에서 중심 픽셀과 주변픽셀과의 차를 두드러지게 나타냄.
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

import cv2 as cv
import numpy as np

img = cv.imread('image/filter_blur.jpg')

def plusK(cw):
    return np.array([[ 0, -1,  0],
                    [-1,  cw, -1],
                    [ 0, -1,  0]])
def crossK(cw):
    return np.array([[ -1,  0,  -1],
                    [  0,  cw,   0],
                    [ -1,  0,  -1]])
def rectgK(cw) :
    return np.array([[ -1, -1,  -1],
                    [ -1,  cw,  -1],
                    [ -1, -1,  -1]])

cv.imshow('original', img)

kernels = ['+', 'x', 'boxed']
for i, k in enumerate([plusK, crossK, rectgK]):
    for w in range(3, 10):
        kernel = k(w)
        img_filtered = cv.filter2D(img, -1, kernel)
        text = f"center weight {w} with {kernels[i]} kernel"
        cv.putText(img_filtered, text, (1, 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv.imshow('filtered', img_filtered)
        cv.waitKey(2000)

cv.waitKey()
cv.destroyAllWindows()