# [Quiz] bilateral을 제외한 4개의 필터 중에 2개의 모든 쌍을 적용한 5개의 창을 만들고,
# 각 창에서 sigma_s, sigma_r을 trackbar를 이용하여 변화시킬 수 있도록 한다.

import cv2 as cv

def on_epde_change(_):
	sigma_s_ep = cv.getTrackbarPos('sigma_s_ep', 'edge_p and detail_e')
	sigma_r_ep = cv.getTrackbarPos('sigma_r_ep', 'edge_p and detail_e') * 0.01
	sigma_s_de = cv.getTrackbarPos('sigma_s_de', 'edge_p and detail_e')
	sigma_r_de = cv.getTrackbarPos('sigma_r_de', 'edge_p and detail_e') * 0.01
	print('edge_preserved: sigma_s, sigma_r =', sigma_s_ep, sigma_r_ep)
	print('detail_enhanced: sigma_s, sigma_r =', sigma_s_de, sigma_r_de)
	dst = cv.edgePreservingFilter(img, sigma_s=sigma_s_ep, sigma_r=sigma_r_ep)
	dst = cv.detailEnhance(dst, sigma_s=sigma_s_de, sigma_r=sigma_r_de)
	cv.imshow('edge_p and detail_e', dst)

def on_epps_change(_):
	sigma_s = cv.getTrackbarPos('sigma_s_ep', 'edge_p and pencil_sk')
	sigma_r = cv.getTrackbarPos('sigma_r_ep', 'edge_p and pencil_sk') * 0.01
	print('edge_preserved: sigma_s, sigma_r =', sigma_s, sigma_r)
	dst = cv.edgePreservingFilter(img, sigma_s=sigma_s, sigma_r=sigma_r)
	sigma_s = cv.getTrackbarPos('sigma_s_ps', 'edge_p and pencil_sk')
	sigma_r = cv.getTrackbarPos('sigma_r_ps', 'edge_p and pencil_sk') * 0.01
	print('pencil_sketch: sigma_s, sigma_r =', sigma_s, sigma_r)
	_, dst_color = cv.pencilSketch(dst, sigma_s=sigma_s, sigma_r=sigma_r)
	cv.imshow('edge_p and pencil_sk', dst_color)

def on_epst_change(_):
	sigma_s = cv.getTrackbarPos('sigma_s_ep', 'edge_p and style')
	sigma_r = cv.getTrackbarPos('sigma_r_ep', 'edge_p and style') * 0.01
	print('edge_preserved: sigma_s, sigma_r =', sigma_s, sigma_r)
	dst = cv.edgePreservingFilter(img, sigma_s=sigma_s, sigma_r=sigma_r)
	sigma_s = cv.getTrackbarPos('sigma_s_st', 'edge_p and style')
	sigma_r = cv.getTrackbarPos('sigma_r_st', 'edge_p and style') * 0.01
	print('stylization: sigma_s, sigma_r =', sigma_s, sigma_r)
	dst = cv.stylization(dst, sigma_s=sigma_s, sigma_r=sigma_r)
	cv.imshow('edge_p and style', dst)

def on_deps_change(_):
	sigma_s = cv.getTrackbarPos('sigma_s_de', 'detail_e and pencil_sk')
	sigma_r = cv.getTrackbarPos('sigma_r_de', 'detail_e and pencil_sk') * 0.01
	print('detail_enhanced: sigma_s, sigma_r =', sigma_s, sigma_r)
	dst = cv.detailEnhance(img, sigma_s=sigma_s, sigma_r=sigma_r)
	sigma_s = cv.getTrackbarPos('sigma_s_ps', 'detail_e and pencil_sk')
	sigma_r = cv.getTrackbarPos('sigma_r_ps', 'detail_e and pencil_sk') * 0.01
	print('pencil_sketch: sigma_s, sigma_r =', sigma_s, sigma_r)
	_, dst_color = cv.pencilSketch(dst, sigma_s=sigma_s, sigma_r=sigma_r)
	cv.imshow('detail_e and pencil_sk', dst_color)

def on_dest_change(_):
	sigma_s = cv.getTrackbarPos('sigma_s_de', 'detail_e and style')
	sigma_r = cv.getTrackbarPos('sigma_r_de', 'detail_e and style') * 0.01
	print('detail_enhanced: sigma_s, sigma_r =', sigma_s, sigma_r)
	dst = cv.detailEnhance(img, sigma_s=sigma_s, sigma_r=sigma_r)
	sigma_s = cv.getTrackbarPos('sigma_s_st', 'detail_e and style')
	sigma_r = cv.getTrackbarPos('sigma_r_st', 'detail_e and style') * 0.01
	print('stylization: sigma_s, sigma_r =', sigma_s, sigma_r)
	dst = cv.stylization(dst, sigma_s=sigma_s, sigma_r=sigma_r)
	cv.imshow('detail_e and style', dst)


def on_psst_change(_):
	sigma_s = cv.getTrackbarPos('sigma_s_ps', 'pencil_sk and style')
	sigma_r = cv.getTrackbarPos('sigma_r_ps', 'pencil_sk and style') * 0.01
	print('pencil_sketch: sigma_s, sigma_r =', sigma_s, sigma_r)
	_, dst_color = cv.pencilSketch(img, sigma_s=sigma_s, sigma_r=sigma_r)
	sigma_s = cv.getTrackbarPos('sigma_s_st', 'pencil_sk and style')
	sigma_r = cv.getTrackbarPos('sigma_r_st', 'pencil_sk and style') * 0.01
	print('stylization: sigma_s, sigma_r =', sigma_s, sigma_r)
	dst = cv.stylization(dst_color, sigma_s=sigma_s, sigma_r=sigma_r)
	cv.imshow('pencil_sk and style', dst)


cv.namedWindow('edge_p and detail_e')
cv.createTrackbar('sigma_s_ep', 'edge_p and detail_e', 60, 60, on_epde_change)
cv.createTrackbar('sigma_r_ep', 'edge_p and detail_e', 40, 100, on_epde_change)
cv.createTrackbar('sigma_s_de', 'edge_p and detail_e', 10, 60, on_epde_change)
cv.createTrackbar('sigma_r_de', 'edge_p and detail_e', 15, 100, on_epde_change)

cv.namedWindow('edge_p and pencil_sk')
cv.createTrackbar('sigma_s_ep', 'edge_p and pencil_sk', 60, 60, on_epps_change)
cv.createTrackbar('sigma_r_ep', 'edge_p and pencil_sk', 40, 100, on_epps_change)
cv.createTrackbar('sigma_s_ps', 'edge_p and pencil_sk', 60, 60, on_epps_change)
cv.createTrackbar('sigma_r_ps', 'edge_p and pencil_sk', 20, 100, on_epps_change)

cv.namedWindow('edge_p and style')
cv.createTrackbar('sigma_s_ep', 'edge_p and style', 60, 60, on_epst_change)
cv.createTrackbar('sigma_r_ep', 'edge_p and style', 40, 100, on_epst_change)
cv.createTrackbar('sigma_s_st', 'edge_p and style', 60, 60, on_epst_change)
cv.createTrackbar('sigma_r_st', 'edge_p and style', 45, 100, on_epst_change)

cv.namedWindow('detail_e and pencil_sk')
cv.createTrackbar('sigma_s_de', 'detail_e and pencil_sk', 10, 60, on_deps_change)
cv.createTrackbar('sigma_r_de', 'detail_e and pencil_sk', 15, 100, on_deps_change)
cv.createTrackbar('sigma_s_ps', 'detail_e and pencil_sk', 60, 60, on_deps_change)
cv.createTrackbar('sigma_r_ps', 'detail_e and pencil_sk', 20, 100, on_deps_change)

cv.namedWindow('detail_e and style')
cv.createTrackbar('sigma_s_de', 'detail_e and style', 10, 60, on_dest_change)
cv.createTrackbar('sigma_r_de', 'detail_e and style', 15, 100, on_dest_change)
cv.createTrackbar('sigma_s_st', 'detail_e and style', 60, 60, on_dest_change)
cv.createTrackbar('sigma_r_st', 'detail_e and style', 45, 100, on_dest_change)

cv.namedWindow('pencil_sk and style')
cv.createTrackbar('sigma_s_ps', 'pencil_sk and style', 60, 60, on_psst_change)
cv.createTrackbar('sigma_r_ps', 'pencil_sk and style', 20, 100, on_psst_change)
cv.createTrackbar('sigma_s_st', 'pencil_sk and style', 60, 60, on_psst_change)
cv.createTrackbar('sigma_r_st', 'pencil_sk and style', 45, 100, on_psst_change)

img = cv.imread('image/red-and-green-leavs-of-autumn-jpg.jpg')

cv.imshow('img', img)
on_epde_change(0)
on_epps_change(0)
on_epst_change(0)
on_deps_change(0)
on_dest_change(0)
on_psst_change(0)
cv.waitKey()