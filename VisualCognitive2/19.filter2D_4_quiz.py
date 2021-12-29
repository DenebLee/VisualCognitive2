# color 영상에 Prewitt 커널을 적용해보고, 그 결과를 GRAYSCALE로 변화한 후 비교해보자.

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

# 부호를 바꾼 커널
kernel1_ = np.array([[1,  0,  -1],
                     [1,  0,  -1],
                     [1,  0,  -1]])
# horizontal border - src에 수직적 변화가 발생하면 이 값널 연산의 절대값이 커짐.
kernel2_ = np.array([[ 1,  1,  1],
                     [ 0,  0,  0],
                     [-1, -1, -1]])

dst1 = cv.filter2D(img, cv.CV_32F, kernel1)
dst2 = cv.filter2D(img, cv.CV_32F, kernel2)
dst1_ = cv.filter2D(img, cv.CV_32F, kernel1_)
dst2_ = cv.filter2D(img, cv.CV_32F, kernel2_)

# vertical and horizontal border detection
dst = cv.magnitude(dst1, dst2)
dst_ = cv.magnitude(dst1_, dst2_)


img = cv.imread('image/edge_test1.jpg')
BGR = cv.split(img)

cvt= []
cvt_= []
for c in BGR:
    dst_1 = cv.filter2D(c, cv.CV_32F, kernel1)
    dst_2 = cv.filter2D(c, cv.CV_32F, kernel2)
    dst_1_ = cv.filter2D(c, cv.CV_32F, kernel1_)
    dst_2_ = cv.filter2D(c, cv.CV_32F, kernel2_)

    # vertical and horizontal border detection
    tmp = cv.magnitude(dst_1, dst_2)
    tmp_ = cv.magnitude(dst_1_, dst_2_)
    cvt.append(tmp.astype(np.uint8))
    cvt_.append(tmp_.astype(np.uint8))

dst_col = cv.merge(cvt)
dst_col_ = cv.merge(cvt_)
print(dst_col.shape)
dst_gray = cv.cvtColor(dst_col, cv.COLOR_BGR2GRAY)
dst_gray_ = cv.cvtColor(dst_col_, cv.COLOR_BGR2GRAY)

# gradient의 부호 방향은 중요하지 않고, color 각각에 대한 edge를 구한 것이 더 정확하다.
cv.imshow('img', img)
cv.imshow('dst1', np.abs(dst1).astype(np.uint8))  # vertical edge
cv.imshow('dst2', np.abs(dst2).astype(np.uint8))  # horizontal edge
cv.imshow('dst', dst.astype(np.uint8))            # adjusted edge
cv.imshow('dst_col', dst_col.astype(np.uint8))            # colored edge
cv.imshow('dst_gray', dst_gray.astype(np.uint8))            # adjusted gray-scale edge
cv.imshow('dst1_', np.abs(dst1_).astype(np.uint8))  # vertical edge
cv.imshow('dst2_', np.abs(dst2_).astype(np.uint8))  # horizontal edge
cv.imshow('dst_', dst_.astype(np.uint8))            # adjusted edge
cv.imshow('dst_col_', dst_col_.astype(np.uint8))            # colored edge
cv.imshow('dst_gray_', dst_gray_.astype(np.uint8))
cv.waitKey()

