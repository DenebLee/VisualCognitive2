# Progressive Probabilistic Hough Transform
# 기본 Hough 변환을 최적화한 방식으로 확률적으로 일부 점에 대해서만 계산한다.

import numpy as np
import cv2

src = cv2.imread("road.jpg")
dst = src.copy()
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 1500, 5000, apertureSize = 5, L2gradient = True)

# lines = cv2.HoughLinesP(canny, 거리단위, 각도단위, 임계값, minLineLength, maxLineGap)
# - 확률적으로 선태하므로, thresh 값을 작게 주어야 한다.
# - minLineLength는 최소 선길이를 지정. 이보다 작인 선은 직선에서 제외
# - maxLineGap은 라인 간의 최대 허용 간격을 의미. 이보다 간격이 좁은 경우 직선으로 허용하지 않음.
# - 반환값은 (N, 1, 4)의 형태를 나타내면, 4의 각 좌표는 x1, y1, x2, y2의 직선값을 나타낸다.
lines = cv2.HoughLinesP(canny, 0.8, np.pi / 180, 90, minLineLength = 10, maxLineGap = 100)

for i in lines:
    cv2.line(dst, (i[0][0], i[0][1]), (i[0][2], i[0][3]), (0, 0, 255), 2)

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# [Quiz] bit_test.jpg 파일을 이용하여, line을 검출한다.