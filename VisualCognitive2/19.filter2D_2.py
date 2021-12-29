# Roberts edge detection : Gradient Method
# - https://m.blog.naver.com/PostView.nhn?blogId=laonple&logNo=220807656718&proxyReferer=https:%2F%2Fwww.google.com%2F
# - https://salkuma.wordpress.com/2014/03/11/opencv-data-type-%EC%A0%95%EB%A6%AC/

import cv2 as cv
import numpy as np

img = cv.imread('image/edge_test.jpg', cv.IMREAD_GRAYSCALE)

# 왼쪽 위에서 오른쪽 아래 방향으로의 변화를 감지 - 주름 정보가 사라고, 잎 줄기를 잘 감지
kernel1 = np.array([[-1,  0,  0],
                    [ 0,  1,  0],
                    [ 0,  0,  0]])

# 오른쪽 위에서 왼쪽 아래 방향으로의 변화를 감지 - 주름 정보를 감지하고, 잎 줄기를 정보가 사라짐
kernel2 = np.array([[ 0,  0, -1],
                    [ 0,  1,  0],
                    [ 0,  0,  0]])

dst1 = cv.filter2D(img, cv.CV_32F, kernel1) # 음수가 나올 수 있으므로 실수형으로 계산
dst2 = cv.filter2D(img, cv.CV_32F, kernel2)

# cv2.magnitude(a, b) : return np.sqrt(a**2, b**2)
dst = cv.magnitude(dst1, dst2) # 두방향으로 검출된 에지의 L2 similarity. 적절한 검출

cv.imshow('img', img)
cv.imshow('dst1', np.abs(dst1).astype(np.uint8)) # 절대값 변환후 8 bit로 형변환
cv.imshow('dst2', np.abs(dst2).astype(np.uint8))
cv.imshow('dst', dst.astype(np.uint8))
cv.waitKey()


# [Quiz] 아래와 같이 kernel3/4가 있을 때 어떤 결과가 나타나는 지 확인해보자.
# kernel3 = np.array([[ 0,  0,  0],
#                     [ 0,  1,  0],
#                     [-1,  0,  0]])
# kernel4 = np.array([[ 0,  0,  0],
#                     [ 0,  1,  0],
#                     [ 0,  0, -1]])