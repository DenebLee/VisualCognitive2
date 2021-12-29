# https://swprog.tistory.com/entry/Mathematical-morphology-%EB%AA%A8%ED%8F%B4%EB%A1%9C%EC%A7%80-%EC%97%B0%EC%82%B0
# morphology : erode(침식), dilate(팽창) 주로 이진 영상에서
# - 영상내 특정 객체의 형태를 변형하여 노이즈를 제거
# - 미세하게 검출된 작은 객체를 키우기 위한 용도로 사용
#
# Erode 연산 : 필터 내부의 가장 낮은(어두운) 값으로 변환(and) - 침식연산. 객체 영역의 외곽을 골고루 깎아 내는 연산
# Dilate 연산 : 필터 내부의 가장 높은(밝은) 값으로 변환(or) - 팽창연산. 객체 외곽을 확대하는 연산
# 두 연산은 순서에 따라 서로 다른 기능을 한다.:
# Erode > Dilate => Opening 연산 : 주로 작은 노이즈들을 제거.
# Dilate > Erode => Closing 연산 : 추출한 객체가 두개 이상의 작은 부분일 때, 이를 큰 객체로 합칠 때

import cv2 as cv
import numpy as np

mat = np.array([[0, 1, 2, 3],
				[4, 5, 6, 7],
				[8, 9, 8, 7],
				[6, 5, 4, 3]], np.uint8)
print('mat')
print(mat)

# 커널안의 모든 원소들을 이용
kernel = np.array([[1, 1, 1],
				   [1, 1, 1],
				   [1, 1, 1]], np.uint8)
print('kernel')
print(kernel)

# 커널의 0이 아닌 값이 가리키는 이웃 픽셀들의 최소값을 찾아 대체
# - 이때 위 커널은 mask 역할을 수행
# cv2.erode(src, kernel, dst, ancher=(-1,-1), iterations=1, borderType=CV_BORDER_REPLECT_101, borderValue)
# - iteration: erosion 반복횟수
eroded = cv.erode(mat, kernel)
print('eroded')
print(eroded)

# kernel = None 로 넣어주면 1로 채워진 3 by 3 커널이 자동으로 적용된다.
eroded = cv.erode(mat, None)
print(eroded)

print('\nmat')
print(mat)
# 나 자신과 상하좌우의 이웃값들 중에 최소값을 찾음
kernel = np.array([[0, 1, 0],
				   [1, 1, 1],
				   [0, 1, 0]], np.uint8)
print('kernel')
print(kernel)
eroded = cv.erode(mat, kernel)
print('eroded')
print(eroded)

# 침식한결과를 다시 침식
eroded_eroded = cv.erode(eroded, kernel)
print('eroded_eroded')
print(eroded_eroded)

# 위와 같은 결과
eroded_iterations2 = cv.erode(mat, kernel, iterations=2)
print('eroded_iterations2')
print(eroded_iterations2)

# [Quiz] cat 이미지에 erode를 1번 또는 2번 적용하여 그 결과를 화면에 출력한다.
img = cv.imread('cat.jpg', 0)

erod1 = cv.erode(img, kernel, iterations=1)
erod2 = cv.erode(img, kernel, iterations=2)

cv.imshow('cat', img)
cv.imshow('erod1', erod1)
cv.imshow('erod2', erod2)

cv.waitKey(0)
cv.destroyAllWindows()

# [Quiz] cat 컬러 이미지에 erode를 1번 또는 2번 적용하는데
# - HSV 공간에서 V만 적용하고, 다시 BGR로 변환하여 출력
# - BGR 공간에서 각각의 채널에 적용하고 이를 합쳐서 출력