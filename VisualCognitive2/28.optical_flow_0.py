# https://leechamin.tistory.com/339
# https://www.ccoderun.ca/programming/doxygen/opencv/tutorial_js_lucas_kanade.html
# - optical flow는 물체나 카메라의 움짐임에 의해 발생하는
# - 연속된 프레임간의 차이에 의해 발생하는 물체의 이동패턴을 감지한다.
# - 가정: 픽셀의 채도는 연속된 프레임 사이에 일정하고, 인접 픽셀은 유사한 움직임을 갖는다.
# - 적용분야: 움직임에 따른 구조 분석, 비디오 압축, 비디오 화질 개선
# 1. cv2.goodFeaturesToTrack 함수를 이용하여 grayScale로 추적하기 좋은 코너를 찾는다.
# 2. cv2.calcOpticalFlowPyrLK(prev, curr, corners, ....)이용하여 tracking을 한다.

import cv2 as cv

img0 = cv.imread('optical-flow0.png')
img1 = cv.imread('optical-flow1.png')

img0_gray = cv.cvtColor(img0, cv.COLOR_BGR2GRAY)
img1_gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)

# params for goodFeaturesToTrack
feature_params = dict( maxCorners = 100,
                       qualityLevel = 0.3,
                       minDistance = 7,
                       blockSize = 7 )

# select points that are easy to track using optical flow : Shi-Tomasi corner detection
# - 사각형, 다이어몬드, X, + 형태의 커널을 이용하여 팽창, 침식을 통해 차영상으로 코너를 검출
# - 컴퓨터 비전에서 코너는 에지의 방향이 급격하게 변하는 부분을 일컫음
# corners = cv2.goodFeaturesToTrack(img, maxCorners, qualityLevel, minDistance, blockSize, ...)
# - maxCorners: 찾을 코너의 최대개수, - qualityLevel: 코너 판정을 위한 최소값
# - minDistance: 코너 간 최소 유클리디안 거리, - blockSize: 지역 특징점을 찾기위한 윈도우 사이즈
pts0 = cv.goodFeaturesToTrack(img0_gray, **feature_params)
print('pts0 :', pts0.shape, pts0.dtype)

# Parameters for lucas kanade optical flow
# winSize : kernel size
# maxLevel : maximum pyramid levels
# criteria : when to terminate the tracking algorithm
lk_params = dict( winSize  = (15,15),
                  maxLevel = 5,
                  criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))

# cv2.CalcOpticalFlowPyrLK(prev, curr, prevPts, currPts, winSize, maxLevel, criteria, flags)
# - calculate optical flow with prev image and curr image using Lucas-Kanade method
# -- pts1 : new points found in curr
# -- status : 광학흐름의 발생 유무. False이며, prev 코너를 curr에서 발견하지 못한 것.
# -- error : track error. 계산된 값이 주변 움직임에 비해서 값이 너무 튀는 경우 제거하는 용도로 사용
# - prev, curr: 현재와 이전의 흑백영상
# - prevPts, currPts: prev, curr의 corners
# - winSize: 코너를 탐색할 커널 윈도우의 size
# - maxLevel: 0-based maximal pyramid level number; if set to 0, pyramids are not used (single level)
# - criteria: 탐색 종료 기준. 반복 탐색 최대값, 탐색 윈도우의 이동위치의 최소값 등
pts1, status, error = cv.calcOpticalFlowPyrLK(img0_gray, img1_gray, pts0, None, **lk_params)

print('pts1 :', pts1.shape, pts1.dtype)       # prev에서 찾은 코너 pts0의 curr에서의 위치
print('status :', status.shape, status.dtype) # 광학흐름의 발생 유무
print('error :', error.shape, error.dtype)

# Select only success points
pts0_success = pts0[status==1]
pts1_success = pts1[status==1]

print('p0_success :', pts0_success.shape, pts0_success.dtype)
print('p1_success :', pts1_success.shape, pts1_success.dtype)

for p in pts0_success:
    cv.circle(img0, tuple(p), 3, (0,0,255))

for p in pts1_success:
    cv.circle(img1, tuple(p), 3, (0,255,0))

cv.imshow('img0', img0)
cv.imshow('img1', img1)
cv.waitKey()

# [Quiz] 실패한 코너를 파란색으로 img0, img1에 각각 그려보고, 실패한 이유를 확인해보자.
# Select only fail points
pts0_fail = pts0[status!=1]
pts1_fail = pts1[status!=1]

print('p0_fail :', pts0_fail.shape, pts0_fail.dtype)
print('p1_fail :', pts1_fail.shape, pts1_fail.dtype)
print(pts0_fail[0], pts0_fail[1])
print(pts1_fail[0], pts1_fail[1])

for p in pts0_fail:
    cv.circle(img0, tuple(p), 5, (255,0,0), 3)

for p in pts1_fail:
    cv.circle(img1, tuple(p), 5, (255,0,0), 3)

cv.imshow('img0', img0)
cv.imshow('img1', img1)
cv.waitKey()