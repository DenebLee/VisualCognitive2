# Non-photorealistic rendering(NPR) : 비사실적 렌더링 효과.
# https://www.learnopencv.com/non-photorealistic-rendering-using-opencv-python-c/
# - 컴퓨터 그래픽스의 한 영역으로 사실적인 렌더링 이외의 다양한 표현 양식을 다룬다.
# - 사실주의에 초점을 맞추었던 기존의 방식과는 달리,
# - NPR은 회화나 드로잉, 도해, 만화 같은 인공적인 양식에 영향을 받는다. 자
# - 주 등장하는 예로 만화 같은 그림을 묘사하는 비디오 게임이나 영화에서 사용하는 툰 셰이딩이 있다.

# 렌더링 방법은 크게 사실적 렌더링과 비사실적 렌더링으로 나눠 볼 수 있습니다.
# - 사실적 렌더링 : 트랜스 포머나 캐리비안의 해적과 같이 실제 영상과 구분이 되지 않는 영상을 생성 방법
# - 비사실적 렌더링 : 열혈강호 등 만화나 고흐의 해바라기 등의 유화, 동양의 수묵화 등처럼 그린 듯한 영상을 생성


import cv2 as cv

# cv2.bilateralFilter(img, d=-1, sigmaColor, sigmaSpace) @1998
# - 에지 정보는 그대로 유지하면서 잡음만 제거하는 에지보전 잡음제거 필터. 7장 참고.
# - edgePreservingFilter에 비해 상당히 느려, 실시간서비스에는 사용되지 않는다.
# d: 필터의 size, 양수가 아닌 값을 주면 sigmaSapce로 자동계산한다.
# # sigmaColor: 픽셀값에 대한 가우시안 Var, sigmaSapce: 픽셀위치에 대한 가우시안 Var
def on_bl_change(_):
	sigma_c = cv.getTrackbarPos('sigma_c', 'bilateral')
	sigma_s = cv.getTrackbarPos('sigma_s', 'bilateral')
	print('bilateral: sigma_c, sigma_s =', sigma_c, sigma_s)
	dst = cv.bilateralFilter(img, d=-1, sigmaColor=sigma_c, sigmaSpace=sigma_s)
	cv.imshow('bilateral', dst)

# cv2.edgePreservingFilter(src, flags=1, sigma_s=60, sigma_r=0.4) @2011
# - smoothing하면서도 edge를 보존하는 필터로 biliteral 필터보다 빠르다.
# - flags: 가장자리 보존 필터를 지정. RECURS_FILTER=1, NORMCONV_FILTER =2
# -- RECURS_FILTER가 3.5배 빠르나, stylizations 용도로는 sharpening이 좋은 2를 지정.
# - sigma_s : [0, 200]. 가우시안 Var로서 인접 픽셀과 가중평균할 kernel size를 결정.
# - sigma_r : (0, 1]. 픽셀과의 유사도를 측정할 가우시안 Var
def on_ep_change(_):
	sigma_s = cv.getTrackbarPos('sigma_s', 'edge_preserved')
	sigma_r = cv.getTrackbarPos('sigma_r', 'edge_preserved') * 0.01
	print('edge_preserved: sigma_s, sigma_r =', sigma_s, sigma_r)
	dst = cv.edgePreservingFilter(img, sigma_s=sigma_s, sigma_r=sigma_r)
	cv.imshow('edge_preserved', dst)

# cv2.detailEnhance(src, sigma_s=10, sigma_r=0.15)
# - 이미지에서 detail한 정보를 향상시켜, sharpeness가 증가된다.
def on_de_change(_):
	sigma_s = cv.getTrackbarPos('sigma_s', 'detail_enhanced')
	sigma_r = cv.getTrackbarPos('sigma_r', 'detail_enhanced') * 0.01
	print('detail_enhanced: sigma_s, sigma_r =', sigma_s, sigma_r)
	dst = cv.detailEnhance(img, sigma_s=sigma_s, sigma_r=sigma_r)
	cv.imshow('detail_enhanced', dst)

# gray, bgr = cv2.pencilSketch(src, sigma_s=60, sigma_r=0.07, shade_factor=0.05)
def on_ps_change(_):
	sigma_s = cv.getTrackbarPos('sigma_s', 'pencil_sketch')
	sigma_r = cv.getTrackbarPos('sigma_r', 'pencil_sketch') * 0.01
	print('pencil_sketch: sigma_s, sigma_r =', sigma_s, sigma_r)
	dst_gray, dst_color = cv.pencilSketch(img, sigma_s=sigma_s, sigma_r=sigma_r)
	cv.imshow('pencil_sketch', dst_color)
	cv.imshow('pencil_sketch_gray', dst_gray)

#
def on_st_change(_):
	sigma_s = cv.getTrackbarPos('sigma_s', 'stylization')
	sigma_r = cv.getTrackbarPos('sigma_r', 'stylization') * 0.01
	print('stylization: sigma_s, sigma_r =', sigma_s, sigma_r)
	dst = cv.stylization(img, sigma_s=sigma_s, sigma_r=sigma_r)
	cv.imshow('stylization', dst)


cv.namedWindow('bilateral')
cv.createTrackbar('sigma_c', 'bilateral', 10, 100, on_bl_change)
cv.createTrackbar('sigma_s', 'bilateral', 5, 100, on_bl_change)

cv.namedWindow('edge_preserved')
cv.createTrackbar('sigma_s', 'edge_preserved', 60, 60, on_ep_change)
cv.createTrackbar('sigma_r', 'edge_preserved', 40, 100, on_ep_change)

cv.namedWindow('detail_enhanced')
cv.createTrackbar('sigma_s', 'detail_enhanced', 10, 60, on_de_change)
cv.createTrackbar('sigma_r', 'detail_enhanced', 15, 100, on_de_change)

cv.namedWindow('pencil_sketch')
cv.createTrackbar('sigma_s', 'pencil_sketch', 60, 60, on_ps_change)
cv.createTrackbar('sigma_r', 'pencil_sketch', 20, 100, on_ps_change)

cv.namedWindow('stylization')
cv.createTrackbar('sigma_s', 'stylization', 60, 60, on_st_change)
cv.createTrackbar('sigma_r', 'stylization', 45, 100, on_st_change)

img = cv.imread('image/red-and-green-leavs-of-autumn-jpg.jpg')

cv.imshow('img', img)
on_bl_change(0)
on_ep_change(0)
on_de_change(0)
on_ps_change(0)
on_st_change(0)
cv.waitKey()