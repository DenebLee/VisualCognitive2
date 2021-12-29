# Sobel edge detection : https://iskim3068.tistory.com/49
# - 소벨 마스크는 모든 방향의 에지를 추출한다.잡음에 강한 편이다.
# - 수직, 수평 에지 보다 대각선 방향 에지에 더 민감하게 반응한다.
# - 마스크가 커지면 에지는 두꺼워져서 선명하게 나타난다.
# - 반면에 명암값의 변화 구간이 촘촘하거나 복잡한 영상일 경우 효과가 낮다.

import cv2 as cv
import numpy as np

img = cv.imread('image/edge_test1.jpg', cv.IMREAD_GRAYSCALE)

# weighted vertical edge
kernel1 = np.array([[-1,  0,  1],
                    [-2,  0,  2],
                    [-1,  0,  1]])
# weighted horizontal edge
kernel2 = np.array([[-1, -2, -1],
                    [ 0,  0,  0],
                    [ 1,  2,  1]])

dst1 = cv.filter2D(img, cv.CV_32F, kernel1)
dst2 = cv.filter2D(img, cv.CV_32F, kernel2)
# weighted adjusted edge
dst = cv.magnitude(dst1, dst2)

cv.imshow('img', img)
cv.imshow('dst1', np.abs(dst1).astype(np.uint8))
cv.imshow('dst2', np.abs(dst2).astype(np.uint8))
cv.imshow('dst', dst.astype(np.uint8))
cv.waitKey()

# [Quiz] 다음과 같은 변화에서 그 결과를 확인해보자.
# 1. weight factor의 값을 [0.5, 1, 1.5, 2, 2.5] 변경하면서 그 효과를 출력해보자.
# 2. 커널 사이즈를 3, 5, 7 등으로 변화시켜보자.