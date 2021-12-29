# Prewitt edge detection : https://iskim3068.tistory.com/49
# - 소벨 마스크의 경우와 비슷하며, 응답시간이 다소 빠르다.
# - 다만, 소벨 마스크에 비해 밝기 변화에 대하여 비중이 약간 적게 준 관계로 에지가 덜 부각된다.
# - 대각선 방향 에지 보다 수직, 수평 방향 에지에 더 민감하게 반응한다.

import cv2 as cv
import numpy as np

img = cv.imread('image/edge_test1.jpg', cv.IMREAD_GRAYSCALE)

# vertical border - src에 수직적 변화가 발생하면 이 커널 연산의 절대값이 커짐.
kernel1 = np.array([[-1,  0,  1],
                    [-1,  0,  1],
                    [-1,  0,  1]])
# horizontal border - src에 수직적 변화가 발생하면 이 값널 연산의 절대값이 커짐.
kernel2 = np.array([[-1, -1, -1],
                    [ 0,  0,  0],
                    [ 1,  1,  1]])

dst1 = cv.filter2D(img, cv.CV_32F, kernel1)
dst2 = cv.filter2D(img, cv.CV_32F, kernel2)

# vertical and horizontal border detection
dst = cv.magnitude(dst1, dst2)

cv.imshow('img', img)
cv.imshow('dst1', np.abs(dst1).astype(np.uint8))  # vertical edge
cv.imshow('dst2', np.abs(dst2).astype(np.uint8))  # horizontal edge
cv.imshow('dst', dst.astype(np.uint8))            # adjusted edge
cv.waitKey()

# [Quiz]
# - kernel1/2의 부호 방향을 반대로 할 때, 이전과의 차이점을 비교해보자.
# - color 영상에 Prewitt 커널을 적용해보고, 그 결과를 GRAYSCALE로 변화한 후 비교해보자.