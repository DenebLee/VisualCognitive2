# 이미지에서 잡음이 있을 때, 잡음을 제거하면 보통 edge가 제거된다.
# edge를 보존하면서 잡음을 제거하는 bilateral 필터을 알아보자.

import numpy as np
import cv2
import random

def noise_gaussian():
    src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)
    print(src.shape)
    print(src.size)

    if src is None:
        print('Image load failed!')
        return

    cv2.imshow('src', src)

    for stddev in [10, 20, 30]:
        noise = np.zeros(src.shape, np.int32)
        cv2.randn(noise, 0, stddev)

        dst = cv2.add(src, noise, dtype=cv2.CV_8UC1)

        desc = 'stddev = %d' % stddev
        cv2.putText(dst, desc, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                   1.0, 255, 1, cv2.LINE_AA)
        cv2.imshow('dst', dst)
        cv2.waitKey()

    cv2.destroyAllWindows()


# cv2.bilateralFilter(img, d=-1, sigmaColor, sigmaSpace) @1998
# - 에지 정보는 그대로 유지하면서 잡음만 제거하는 에지보전 잡음제거 필터. 7장 참고.
# - edgePreservingFilter에 비해 상당히 느려, 실시간서비스에는 사용되지 않는다.
# d: 필터의 size, 양수가 아닌 값을 주면 sigmaSapce로 자동계산한다.
# # sigmaColor: 픽셀값에 대한 가우시안 Var, sigmaSapce: 픽셀위치에 대한 가우시안 Var
def filter_bilateral():
    src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    noise = np.zeros(src.shape, np.int32)
    cv2.randn(noise, 0, 5)
    cv2.add(src, noise, src, dtype=cv2.CV_8UC1)

    # GaussianBlur(src, filter_size, sigmaX, sigmaY)
    dst1 = cv2.GaussianBlur(src, (0, 0), 5)
    dst2 = cv2.bilateralFilter(src, -1, 10, 5)
    
    cv2.imshow('src', src)
    cv2.imshow('dst1', dst1)
    cv2.imshow('dst2', dst2)
    cv2.waitKey()
    cv2.destroyAllWindows()


def filter_median():
    src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)
    start, end = 256, 261
    print(src[start:end, start:end])

    if src is None:
        print('Image load failed!')
        return

    # 검은색 또는 하얀색으로 전체 픽셀의 10%를 대체한 노이즈를 생성
    for i in range(0, int(src.size / 10)):
        x = random.randint(0, src.shape[1] - 1)
        y = random.randint(0, src.shape[0] - 1)
        src[x, y] = (i % 2) * 255

    dst1 = cv2.GaussianBlur(src, (0, 0), 1)
    # 출력결과 medianBlur는 src의 값을 잘 보존하고 있다.
    dst2 = cv2.medianBlur(src, 3)
    print(dst1[start:end, start:end])
    print(dst2[start:end, start:end])

    cv2.imshow('src', src)
    cv2.imshow('dst1', dst1)
    cv2.imshow('dst2', dst2)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    noise_gaussian()
    filter_bilateral()
    filter_median()

# [Quiz] leanna.bmp 파일을 grayscale로 읽고, 이에 대한 노이이즈를 추가한 후
# - 검은색 또는 하얀색으로 전체 픽셀의 10%를 대체한 노이즈를 numpy스럽게 생성
# medianBlur와 bilateral 필터를 각각 적용하여 가장 적절한 파라미터를 트랙바로 확인해보자.