# https://www.pyimagesearch.com/2018/08/06/tracking-multiple-objects-with-opencv/
# https://www.learnopencv.com/object-tracking-using-opencv-cpp-python/
# https://bkshin.tistory.com/entry/OpenCV-32-%EA%B0%9D%EC%B2%B4-%EC%B6%94%EC%A0%81%EC%9D%84-%EC%9C%84%ED%95%9C-Tracking-API
# pip install opencv-contrib-python
# 1. 아무 키 누르고,
# 2. 스페이스 누르고
# 3. ESC 눌러 종료
# cv2.cv2 에러 발생시
# : pip uninstall opencv-contrib-python
# : pip install --upgrade opencv-contrib-python==4.0.0.21 --user

import cv2 as cv
import numpy as np

tracker_types = ['BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'MOSSE', 'CSRT']
tracker_type = tracker_types[5]
tracker = None

if tracker_type == 'BOOSTING':
	tracker = cv.TrackerBoosting_create()
elif tracker_type == 'MIL':
	tracker = cv.TrackerMIL_create()
elif tracker_type == 'KCF':
	tracker = cv.TrackerKCF_create()
elif tracker_type == 'TLD':
	tracker = cv.TrackerTLD_create()
elif tracker_type == 'MEDIANFLOW':
	tracker = cv.TrackerMedianFlow_create()
elif tracker_type == 'MOSSE':
	tracker = cv.TrackerMOSSE_create()
elif tracker_type == "CSRT":
	tracker = cv.TrackerCSRT_create()


video = cv.VideoCapture(0)

while True:
	ok, frame = video.read()
	if not ok: break
	cv.imshow('Tracking', frame)
	if cv.waitKey(1) != -1: break

# cv.selectROI(windowName, img, showCrosshair=True)
# - return: (x, y, w, h) using dragging mouse
bbox = cv.selectROI('Tracking', frame, showCrosshair=False)
print(bbox)

# Initialize tracker with first frame and bounding box
ok = tracker.init(frame, bbox)
print('tracker.init :', ok)

count = 0
fps = 0
t0 = cv.getTickCount()

while True:

	ok, frame = video.read()
	if not ok: break

	# Update tracker
	ok, bbox = tracker.update(frame)

	# Draw bounding box
	if ok:
		# Tracking success
		p1 = (int(bbox[0]), int(bbox[1]))
		p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
		cv.rectangle(frame, p1, p2, (0, 255, 0), 2)
	else:
		# Tracking failure
		cv.putText(frame, 'Tracking failure', (200, 240), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

	# Display tracker type on frame
	cv.putText(frame, tracker_type + " Tracker", (10, 60), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

	# Display FPS on frame
	cv.putText(frame, "FPS : " + str(int(fps)), (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

	# Display result
	cv.imshow('Tracking', frame)

	# Exit if ESC pressed
	if cv.waitKey(1) == 27: break

	count += 1
	if( count == 10 ):
		t = cv.getTickCount()
		time = (t-t0) / cv.getTickFrequency()
		fps = int(np.round(10/time))
		count = 0
		t0 = t

