# Canny edge detector with a trackbar
# [Quiz] GaussianBlurr를 적용한 이후, Canny를 사용한다.
# - 이때 커널 사이즈는 (0, 0)하고, sx=1을 디폴트로하고,
# - 이값을 0.1 ~ 2까지 변화시키는 트랙바를 추가하라.

import cv2 as cv

def onChangeThresh1(val):
	global thresh1, thresh2, edge
	thresh1 = val
	print('thresh1, thresh2 =', thresh1, thresh2)
	edge = cv.Canny(blur, thresh1, thresh2)
	cv.imshow('edge', edge)

def onChangeThresh2(val):
	global thresh1, thresh2, edge
	thresh2 = val
	print('thresh1, thresh2 =', thresh1, thresh2)
	edge = cv.Canny(blur, thresh1, thresh2)
	cv.imshow('edge', edge)

def onChangeSigmaX(val):
	global blur, edge, sx10
	sx10 = val
	print('thresh1, thresh2 =', thresh1, thresh2)
	blur = cv.GaussianBlur(img, (0, 0), sigmaX=sx10 / 10)
	edge = cv.Canny(blur, thresh1, thresh2)
	cv.imshow('edge', edge)


img = cv.imread('image/edge_test1.jpg', cv.IMREAD_COLOR)
sx10 = 10
blur = cv.GaussianBlur(img, (0,0), sigmaX=sx10/10)

thresh1 = 50
thresh2 = 120
cv.namedWindow('edge')
cv.createTrackbar('thresh1', 'edge', thresh1, 255, onChangeThresh1)
cv.createTrackbar('thresh2', 'edge', thresh2, 255, onChangeThresh2)
cv.createTrackbar('sx10', 'edge', sx10, 30, onChangeSigmaX)

edge = cv.Canny(blur, thresh1, thresh2)

cv.imshow('img', img)
cv.imshow('edge', edge)
cv.waitKey()