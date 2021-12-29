# [Quiz] u, v에 for문이 numpy 스럽지 않아 매우 느리다. numpy 연산으로 처리하고,
# - radius, levels에 대해 trackbar은 나중에 적용하자.
# - numpy 연산시 항상 overflow, underflow를 조심해야 한다.
# - array의 각성분에 대한 lambda 함수의 성능차: https://stackoverflow.com/questions/35215161/most-efficient-way-to-map-function-over-numpy-array/35216364

import cv2 as cv
import numpy as np

def oil_painting_effect(src, radius, levels):
	dst = np.zeros(src.shape, src.dtype)
	# gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
	gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY).astype(np.int32) # for roiHist

	for i in range(src.shape[0]):
		print(i)
		for j in range(src.shape[1]):
			hist = np.zeros(levels) # 이웃하는 픽셀들의 히스토그램을 저장할 변수
			bgr_sum = np.zeros((levels,3)) # 이웃하는 픽셀들의 컬러값의 합을 저장할 변수
			# 이웃하는 모든 픽셀들을 방분하며 히스토그램과 각 구간의 컬러의 합을 계산
			roi = gray[max(i-radius, 0):i+radius+1, max(j-radius, 0):j+radius+1]
			roiBGR = src[max(i-radius, 0):i+radius+1, max(j-radius, 0):j+radius+1]

			# roiHist generate overflow. so, u must change type of gray
			roiHist = roi * levels // 256
			idx, freq = np.unique(roiHist, return_counts=True)
			for id, f in zip(idx, freq):
				hist[id] = f
				bgr_sum[id] = roiBGR.reshape((-1,3))[roiHist.ravel() == id].sum(axis=0)

			max_idx = np.argmax(hist)
			dst[i, j] = bgr_sum[max_idx] // hist[max_idx]

	return dst

img = cv.imread('image/red-and-green-leavs-of-autumn-jpg.jpg')

radius, levels = 4, 8
effect = oil_painting_effect(img, radius, levels)

cv.imshow('img', img)
cv.imshow('effect', effect)
cv.waitKey()

# [Quiz] np.histogram을 이용하여 작업속도를 개선해보자.