# trackbar : https://076923.github.io/posts/Python-opencv-35/
# - 트랙바란 스크롤 바의 하나로, 슬라이더 바의 형태를 갖고 있다
# - 트랙바는 일정 범위 내의 값을 변경할 때 사용하며, 적절한 임곗값을 찾거나 변경하기 위해 사용한다
# - OpenCV의 트랙바는 생성된 윈도우 창에 트랙바를 부착해 사용할 수 있다

import cv2 as cv
import numpy as np

# 트랙바의 값이 변할때마다 새로운 값이 val 로 넘어오며 호출된다.
def onChange(val):
    # 트랙바의 값을 얻을 수 있는 다른 방법
    pos = cv.getTrackbarPos('brightness', 'img')
    print(val, pos) # val 와 pos 의 값이 같음을 알 수 있다.
    img.fill(val)
    cv.imshow('img', img)


init_val = 128
img = np.full((480,640), init_val, np.uint8)
cv.namedWindow('img')
# createTrackbar(trackbarname, winname, init_val, max_val, TrackbarCallback, userdata)
# - brightness 라는 이름의 트랙바를 img 라는 이름의 창에 생성,
# - init_val 초기값. 이값은 onChange 함수의 인자로 전달됨. 정수형
# - 255는 최대값. 정수형이어야 한다.
# - onChange 함수를 콜백함수로 등록
# - userdata : 트랙바 콜백 함수에 전달할 데이터 인수
cv.createTrackbar('brightness', 'img', init_val, 255, onChange)

cv.imshow('img', img)
cv.waitKey()

# [Quiz] 19.filter2D_5_quiz 문제에서 weight factor를 track bar로 조절해보자.
# - kernel size는 3만 사용한다.
# - weight facotr가 실수이므로, 이를 정수로 처리할 수 있도록 해야 한다.
