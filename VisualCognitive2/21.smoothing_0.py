# blurring할 픽셀 주변을 따라, 인접 픽셀에 더 많은 가중치를 주는 weighted mean 커널을 사용한다.
# - 기본적으로 4sigma까지 사용하므로, 양방향과 0를 고려할 때, kernel size는 9를 많이 사용한다.

import cv2 as cv
import numpy as np

img = cv.imread('image/filter_blur.jpg')

rx, ry = 12, 6 # half kernel size
sx, sy =  6, 3 # VAR of Gaussian in x and y directions

# Create Gaussian Kernel
kernel = np.zeros((ry*2+1, rx*2+1), np.float32)
for i in range(kernel.shape[0]):
    for j in range(kernel.shape[1]):
        x = j - rx # x distance from the kernel center
        y = i - ry # y distance from the kernel center
        kernel[i,j] = np.exp(-(x*x)/(2*sx*sx)-(y*y)/(2*sy*sy))

cv.imshow('kernel', cv.resize(kernel, (400,200)))

kernel /= kernel.sum() # make the kernel sum 1
img_smoothed = cv.filter2D(img, -1, kernel)

# (rx*2+1, ry*2+1) is kernel size in x and y directions
# - GaussianBlur(img, ksize, sigmaX, sigmaY, borderType)
img_blurred = cv.GaussianBlur(img, (rx*2+1,ry*2+1), sigmaX=sx, sigmaY=sy)

# auto detect sigmax, sigmay from the kernel size
img_blurred_autosigma = cv.GaussianBlur(img, (rx*2+1,ry*2+1), 0)
img_blurred_auto33 = cv.GaussianBlur(img, (3,3), 0)

cv.imshow('original', img)
cv.imshow('smoothed', img_smoothed)
cv.imshow('GaussianBlurred', img_blurred)
cv.imshow('GaussianBlurredAutoSigma', img_blurred_autosigma)
cv.imshow('GaussianBlurredAuto33', img_blurred_auto33)

cv.waitKey()

# [Quiz] filter size를 (0,0)두고, sigmaX, sigmaY의 값을 1 ~ 10로 trackbar를 이용하여 조절하자.
# - filter size를 0으로 두면, sigma 값을 이용하여 자동으로 kernel size를 조정해준다.