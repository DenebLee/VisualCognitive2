import cv2 as cv
import numpy as np

mat = np.array([[0, 1, 2, 3],
				[4, 5, 6, 7],
				[8, 9, 8, 7],
				[6, 5, 4, 3]], np.uint8)

print('mat')
print(mat)
# this uses all the neighbors in the kernel
kernel = np.array([[1, 1, 1],
				   [1, 1, 1],
				   [1, 1, 1]], np.uint8)
print('kernel')
print(kernel)
# find the maximum value in the neighbors indicated by the non-zero elements in the kernel
# cv2.dilate(src, kernel, dst, ancher=(-1,-1), iterations=1, borderType=CV_BORDER_REPLECT_101, borderValue)
# - iteration: erosion 반복횟수
dilated = cv.dilate(mat, kernel)
print('dilated')
print(dilated)

# kernel = None -> kernel = 3 by 3 filled with 1s
dilated = cv.dilate(mat, None)
print(dilated)

print('\nmat')
print(mat)
# this uses current pixel and only top, bottom, left, right neighbors
kernel = np.array([[0, 1, 0],
				   [1, 1, 1],
				   [0, 1, 0]], np.uint8)
print('kernel')
print(kernel)
dilated = cv.dilate(mat, kernel)
print('dilated')
print(dilated)

# dilate one more time
dilated_dilated = cv.dilate(dilated, kernel)
print('dilated_dilated')
print(dilated_dilated)

# the same result as above
dilated_iterations2 = cv.dilate(mat, kernel, iterations=2)
print('dilated_iterations2')
print(dilated_iterations2)

# [Qiuz] 고양이 이미지에 dilate 1회, 2회를 각각 적용해보고 출력하자.
img = cv.imread('cat.jpg', 0)

dilate1 = cv.dilate(img, kernel, iterations=1)
dilate2 = cv.dilate(img, kernel, iterations=2)

dilate1_ = cv.dilate(img, None, iterations=1)
dilate2_ = cv.dilate(img, None, iterations=2)

cv.imshow('cat', img)
cv.imshow('dilate1', dilate1)
cv.imshow('dilate2', dilate2)
cv.imshow('dilate1_', dilate1_)
cv.imshow('dilate2_', dilate2_)

cv.waitKey(0)
cv.destroyAllWindows()