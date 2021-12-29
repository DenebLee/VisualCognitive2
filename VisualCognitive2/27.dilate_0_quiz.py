# [Quiz] cat 컬러 이미지에 dilate를 1번 또는 2번 적용하는데
# - HSV 공간에서 V만 적용하고, 다시 BGR로 변환하여 출력
# - BGR 공간에서 각각의 채널에 적용하고 이를 합쳐서 출력

import cv2
import numpy as np

kernel = np.array([[0, 1, 0],
				   [1, 1, 1],
				   [0, 1, 0]], np.uint8)

img = cv2.imread('cat.jpg')

h, s, v = cv2.split(cv2.cvtColor(img, cv2.COLOR_BGR2HSV))
v1 = cv2.dilate(v, kernel, iterations=1)
v2 = cv2.dilate(v, kernel, iterations=2)
hsvDelate1 = cv2.cvtColor(cv2.merge([h,s,v1]), cv2.COLOR_HSV2BGR)
hsvDelate2 = cv2.cvtColor(cv2.merge([h,s,v2]), cv2.COLOR_HSV2BGR)

cv2.imshow('cat', img)
cv2.imshow('hsvDilate1', hsvDelate1)
cv2.imshow('hsvDilate2', hsvDelate2)

cv2.waitKey(0)

bgrDilate1, bgrDilate2 = [], []
for c in cv2.split(img):
	bgrDilate1.append(cv2.dilate(c, kernel, iterations=1))
	bgrDilate2.append(cv2.dilate(c, kernel, iterations=2))

bgrDilate1, bgrDilate2 = cv2.merge(bgrDilate1), cv2.merge(bgrDilate2)
cv2.imshow('bgrDilate1', bgrDilate1)
cv2.imshow('bgrDilate2', bgrDilate2)

cv2.waitKey(0)
cv2.destroyAllWindows()

# 밝기 정보를 유지하면서 noise를 효과적으로 제거하려면 HSV공간에서 V만 Dilate