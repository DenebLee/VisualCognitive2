# Roberts edge detection에서 잘못된 에지 검출 커널 예

import cv2 as cv
import numpy as np

kernel_diag0 = np.array([[-1,  0,  0],
                         [ 0,  1,  0],
                         [ 0,  0,  0]])

kernel_diag1 = np.array([[ 0,  0, -1],
                         [ 0,  1,  0],
                         [ 0,  0,  0]])

# 잘못된 커널
kernel_all_in_one0 = np.array([[-1,  0, -1],
                               [ 0,  2,  0],
                               [ 0,  0,  0]])

# 잘못된 커널
kernel_all_in_one1 = np.array([[ 0, -1,  0],
                               [-1,  4, -1],
                               [ 0, -1,  0]])

img = np.zeros((400,400), np.uint8)

# 픽셀값이 한번에 바뀌는것이 아니라 일정한 영역에서 바뀌는 실제와 흡사한 상황
j0, j1 = 200, 203
d = j1 - j0
# img의 201열에서 85, 202열에서 85
for j in range(j0, j1):
    img[:,j] = int(255*(j-j0)/d)

# 203열 부터는 255
img[:, j1:]	= 255
print(img[0, j0:j1+1])

# img = cv.imread('image/edge_test1.jpg', cv.IMREAD_GRAYSCALE)

dst_diag0 = cv.filter2D(img, cv.CV_32F, kernel_diag0)
dst_diag1 = cv.filter2D(img, cv.CV_32F, kernel_diag1)
dst_diag = cv.magnitude(dst_diag0, dst_diag1)

dst_all_in_one0 = cv.filter2D(img, cv.CV_32F, kernel_all_in_one0)
dst_all_in_one1 = cv.filter2D(img, cv.CV_32F, kernel_all_in_one1)
dst_diag_all_in = cv.magnitude(dst_all_in_one0, dst_all_in_one1)

cv.imshow('img', img)

# 올바르게 에지가 검출
cv.imshow('dst_diag', np.abs(dst_diag).astype(np.uint8))

# 엣지가 가장 강하게 검출되어야할 곳은 0 으로 나오고 그 좌우로 엣지가 두개 검출
# 잘못된 엣지 검출을 커널 예
cv.imshow('dst_all_in_one0', np.abs(dst_all_in_one0).astype(np.uint8))
cv.imshow('dst_all_in_one1', np.abs(dst_all_in_one1).astype(np.uint8))
cv.imshow('dst_diag_all_in', dst_diag_all_in.astype(np.uint8))
cv.waitKey()

# [Quiz] 올바른 edge 검출에서 np.abs대신 np.max(dst_diag, 0)을 사용한 결과는?