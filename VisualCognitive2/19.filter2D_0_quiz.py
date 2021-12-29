# 7장 filterig 참고
# [Quiz](12, 12) shape의 회색 이미지에 위와 같은 kernel을 적용하고,
# -  그 결과 이미지와 값을 출력하자.
import cv2 as cv
import numpy as np

img = np.full((12,12), 128, dtype=np.uint8)

# blurring 효과: 주위의 픽셀값과 평균
# kernel = np.full((3,3), 1./(3*3))
kernel = np.full((9,9), 1./(9*9))
print('kernel')
print(kernel)

img_filtered = cv.filter2D(img, -1, kernel)

# 원본과 출력 이미지의 모양과 데이터 타입이 같은 것을 확인
print(img.shape, img.dtype)
print(img_filtered.shape, img_filtered.dtype)
print(img_filtered)

cv.imshow('original', img)
cv.imshow('filtered', img_filtered)
cv.waitKey()