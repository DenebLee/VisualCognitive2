# [quiz] radius는 최대 7, levels = [5, 6, 7, 8, 9, 10]를 적용하여
# trackbar로 튜닝이 가능한 유화효과를 생성해보자.

import cv2 as cv
import numpy as np

def oil_painting_effect(src, radius, levels):
	dst = np.zeros(src.shape, src.dtype)
	# gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
	gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY).astype(np.int32) # for roiHist
	bins = np.linspace(0, levels, levels+1, dtype=np.int32)

	for i in range(src.shape[0]):
		for j in range(src.shape[1]):
			# hist = np.zeros(levels) # 이웃하는 픽셀들의 히스토그램을 저장할 변수
			bgr_sum = np.zeros((levels,3)) # 이웃하는 픽셀들의 컬러값의 합을 저장할 변수
			# 이웃하는 모든 픽셀들을 방분하며 히스토그램과 각 구간의 컬러의 합을 계산
			roi = gray[max(i-radius, 0):i+radius+1, max(j-radius, 0):j+radius+1]
			roiBGR = src[max(i-radius, 0):i+radius+1, max(j-radius, 0):j+radius+1]

			# roiHist generate overflow. so, u must change type of gray
			roiHist = roi * levels // 256
			freq, _ = np.histogram(roiHist, bins)
			maxIdx = np.argmax(freq)
			bgr_sum[maxIdx] = roiBGR.reshape((-1,3))[roiHist.ravel() == maxIdx].sum(axis=0)
			dst[i, j] = bgr_sum[maxIdx] // freq[maxIdx]

	return dst

img = cv.imread('image/red-and-green-leavs-of-autumn-jpg.jpg')

def on_effect_change(_):
	radius = cv.getTrackbarPos('radius', 'effect')
	levels = cv.getTrackbarPos('levels-5', 'effect') + 5
	print('effect: radius, levels =', radius, levels)
	effect = oil_painting_effect(img, radius, levels)
	print(f'effect: radius {radius}, levels {levels} image')
	cv.imshow('effect', effect)

radius, levels = 4, 8
effect = oil_painting_effect(img, radius, levels)

cv.imshow('img', img)
cv.imshow('effect', effect)
cv.createTrackbar('radius', 'effect', 4, 7, on_effect_change)
cv.createTrackbar('levels-5', 'effect', 3, 5, on_effect_change)

cv.waitKey()
