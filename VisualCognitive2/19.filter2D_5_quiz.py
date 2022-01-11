# [Quiz] 다음과 같은 변화에서 결과 확인.
# 1. weight factor의 값을 [0.5, 1, 1.5, 2, 2.5] 변경하면서 그 효과를 출력
# 2. 커널 사이즈를 3, 5, 7 등으로 변화

import cv2 as cv
import numpy as np

img = cv.imread('image/edge_test1.jpg', cv.IMREAD_GRAYSCALE)

# weighted vertical edge: n filter size, w: anchor weight
def vKernel(n, w):
    k = np.zeros((n, n))
    for i in range(int((n-1)/2)):
        j = (n-1)/2 - 1 - i
        k[:,i] = -1*(0.5)**j
        k[:,-1-i] = 1*(0.5)**j

    k[int((n-1)/2), :] = k[int((n-1)/2), :]*w
    return k

print(vKernel(5, 2))

# weighted horizontal edge : n=3 then create (7, 7) kernel
def hKernel(n, w):
    k = np.zeros((n, n))
    for i in range(int((n-1)/2)):
        j = (n-1)/2 - 1 - i
        k[i,:] = -1*(0.5)**j
        k[-1-i,:] = 1*(0.5)**j

    k[:, int((n-1)/2)] = k[:, int((n-1)/2)]*w
    return k

cv.imshow('img', img)

for n in [3,5,7]:
    for w in [0.5, 1, 1.5, 2, 2.5]:
        kernel1, kernel2 = vKernel(n, w), hKernel(n, w)
        dst1 = cv.filter2D(img, cv.CV_32F, kernel1)
        dst2 = cv.filter2D(img, cv.CV_32F, kernel2)
        # weighted adjusted edge
        dst = cv.magnitude(dst1, dst2)
        text = f"center weight {round(w, 1)} with {n} kernel size"
        cv.putText(dst, text, (1, 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        cv.imshow('dst1', np.abs(dst1).astype(np.uint8))
        cv.imshow('dst2', np.abs(dst2).astype(np.uint8))
        cv.imshow('dst', dst.astype(np.uint8))
        cv.waitKey(1500)

# kernel size가 커지면 edge가 많이지고, weight가 커지면 edge가 굵어지는 특성을 알 수 있다.
