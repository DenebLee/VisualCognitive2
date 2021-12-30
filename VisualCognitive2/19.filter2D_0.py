# 7장 filterig 참고 : bluring - convolution 예제와 유사
# - 블러링은 거친 느낌의 입력 영상을 부드럽게 만드는 용도로 사용되기도 하고,
# - 혹은 입력 영상에 존재하는 잡음의 영향을 제거하는 전처리 과정으로도 사용됨

import cv2 as cv
import numpy as np

img = cv.imread('image/filter_blur.jpg')

# blurring 효과: 주위의 픽셀값과 평균
KSIZE = 3
kernel = np.full((KSIZE,KSIZE), 1./(KSIZE*KSIZE))
print('kernel')
print(kernel)

# -1은 원본 이미지와 같은 데이터 타입으로 출력이미지 생성
# cv2.filter2D(src, ddepth, kernel, anchor=None, delta=None, borderType=None) -> dst
# - opencv의 많은 필터들에 대한 generalized version.
# - src에 kernel로 convolution 연산을 수행한 후 그 결과를 dst로 반환
# • ddepth: dst의 depth
# --- unsigned char (CV_8U), signed char (CV_8S), unsigned short (CV_16U)
# • kernel: 2차원 커널. 채널마다 달리하려면 split으로 자른 후, 각각 적용해야 한다.
# • anchor: 고정점 위치. 기본은 (-1, -1)이며, 필터 중앙을 고정점으로 사용
# • delta: 추가적으로 더할 값. 기본 0
# • borderType: 가장자리 픽셀 확장 방식. 기본 BORDER_REFLECT_101
# • cv2.filter에서의 필수요소 체크확인
img_filtered = cv.filter2D(img, -1, kernel)

# 원본과 출력 이미지의 모양과 데이터 타입이 같은것을 확인
print(img.shape, img.dtype)
print(img_filtered.shape, img_filtered.dtype)

cv.imshow('original', img)
cv.imshow('filtered', img_filtered)
cv.waitKey()

# [Quiz](12, 12) shape의 회색 이미지에 위와 같은 kernel을 적용하고,
# -  그 결과 이미지와 값을 출력하자.
