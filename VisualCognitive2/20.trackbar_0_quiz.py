# [Quiz] 19.filter2D_5_quiz 문제에서 weight factor를 track bar로 조절해보자.
# - kernel size는 3만 사용한다.
# - weight facotr가 실수이므로, 이를 정수로 처리할 수 있도록 해야 한다.

import cv2 as cv
import numpy as np

import cv2 as cv
import numpy as np

img = cv.imread('image/edge_test1.jpg', cv.IMREAD_GRAYSCALE)

# weighted vertical edge : n=3 then create (3, 3) kernel
def vKernel(w=2, n=3):
    k = np.zeros((n, n))
    for i in range(int((n-1)/2)):
        j = (n-1)/2 - 1 - i
        k[:,i] = -1*(0.5)**j
        k[:,-1-i] = 1*(0.5)**j

    k[int((n-1)/2), :] = k[int((n-1)/2), :]*w
    return k

# print(vKernel(w=3, n=9))

# weighted horizontal edge
def hKernel(w=2, n=3):
    k = np.zeros((n, n))
    for i in range(int((n-1)/2)):
        j = (n-1)/2 - 1 - i
        k[i,:] = -1*(0.5)**j
        k[-1-i,:] = 1*(0.5)**j

    k[:, int((n-1)/2)] = k[:, int((n-1)/2)]*w
    return k

# 트랙바의 값이 변할때마다 새로운 값이 val 로 넘어오며 호출된다.
def onwChange(val):
    global init_w
    init_w = val/10
    kernel1, kernel2 = vKernel(w=init_w, n=init_n), hKernel(w=init_w, n=init_n)
    dst1 = cv.filter2D(img, cv.CV_32F, kernel1)
    dst2 = cv.filter2D(img, cv.CV_32F, kernel2)
    # weighted adjusted edge
    dst = cv.magnitude(dst1, dst2)

    cv.imshow('img', dst.astype(np.uint8))

def onnChange(val):
    global init_n
    init_n = 2*val+1
    kernel1, kernel2 = vKernel(w=init_w, n=init_n), hKernel(w=init_w, n=init_n)
    dst1 = cv.filter2D(img, cv.CV_32F, kernel1)
    dst2 = cv.filter2D(img, cv.CV_32F, kernel2)
    # weighted adjusted edge
    dst = cv.magnitude(dst1, dst2)

    cv.imshow('img', dst.astype(np.uint8))

init_w, init_n = 20, 1
cv.namedWindow('img')
cv.imshow('img', img)

cv.createTrackbar('sobel w/10', 'img', init_w, 30, onwChange)
cv.createTrackbar('sobel (n-1)/2', 'img', init_n, 4, onnChange)
cv.waitKey()