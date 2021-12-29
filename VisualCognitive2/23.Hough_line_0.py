# https://opencv-python.readthedocs.io/en/latest/doc/25.imageHoughLineTransform/imageHoughLineTransform.html
# 이미지에서 직선을 찾는 허프변환 알고리즘
# - y = ax + b => p = x sinC + y cosC
# - p: 원점에서 직선과의 거리
# - C: x축과 직선이 만나는 각도

import numpy as np
import cv2

# src = cv2.imread("road.jpg")
src = cv2.imread("road_small.jpg")
dst = src.copy()

# 전처리: gray 이미지에 대해 canny edge 검출기를 사용하여 edge를 검출
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# canny = cv2.Canny(gray, 1500, 5000, apertureSize = 5, L2gradient = True)
canny = cv2.Canny(gray, 1500, 3500, apertureSize = 5, L2gradient = True)
# canny = cv2.Canny(gray, 255, 450)

# cv2.HoughLines(검출이미지, 거리, 각도, 임계값, 거리 약수, 각도 약수, 최소 각도, 최대 각도)
# - 거리(p): 거리 정밀도. 픽셀 단위로서 0 ~ 1 사이의 값을 갖는다.
# - 각도(C): 각도 정밀도. radian 단위로서 1 ~ 180 도의 범위를 갖는다.
# - 직선 후보인 누산평면은 거리 x 각도의 차원을 갖는 2차원 히스토그램이며,
# - 이때 임계값(thresh)은 거리 각도에서 최소 교차 횟수를 지정한다.
# - 최소, 최대 각도에 의해 그려질 직선의 범위가 결정된다.
# - 출력된 lines는 (N, 1, 2)의 shape을 가지면 N은 검출된 직선의 수를 나타내며, 각 좌표값은 rho, theta를 나타낸다.
# lines = cv2.HoughLines(canny, 0.8, np.pi / 180, 150, srn = 100, stn = 200, min_theta = 0, max_theta = np.pi)
lines = cv2.HoughLines(canny, 0.8, np.pi / 180, 150, srn = 50, stn = 100, min_theta = 0, max_theta = np.pi)
# lines = cv2.HoughLines(canny, 0.8, np.pi / 180, 250)
print(lines.shape)

for i in lines:
    rho, theta = i[0][0], i[0][1]
    a, b = np.cos(theta), np.sin(theta)
    x0, y0 = a*rho, b*rho

    scale = src.shape[0] + src.shape[1]

    # x1 * np.cos(theta) + y1 * np.sin(thera) = rho
    x1 = int(x0 + scale * -b)
    y1 = int(y0 + scale * a)
    x2 = int(x0 - scale * -b)
    y2 = int(y0 - scale * a)

    cv2.line(dst, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv2.circle(dst, (x0, y0), 3, (255, 0, 0), 5, cv2.FILLED)

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()