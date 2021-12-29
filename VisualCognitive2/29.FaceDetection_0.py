# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html
# https://github.com/opencv/opencv/tree/master/data/haarcascades
# https://thebook.io/006939/ch13/02-05/
# https://www.youtube.com/watch?v=WfdYYNamHZ8
# https://www.bogotobogo.com/python/OpenCV_Python/python_opencv3_Image_Object_Detection_Face_Detection_Haar_Cascade_Classifiers.php
import cv2 as cv

# cap = cv.VideoCapture(0)
# while True:
#    ret, frame = cap.read()
#    cv.imshow('frame', frame)
#    if cv.waitKey(1) != -1: break
# cv.imwrite('myface.jpg', frame)
# cap.release()

# 얼굴과 눈을 검출하는 classifiers
# xml_folder = 'C:/Users/USER/venv/computer-vision/Lib/site-packages/cv2/data/'
# face_cascade = cv.CascadeClassifier(xml_folder+'haarcascade_frontalface_default.xml')
# eye_cascade = cv.CascadeClassifier(xml_folder+'haarcascade_eye.xml')
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')

# img = cv.imread('myface.jpg')
img = cv.imread('image/face3.jpg')

# CascadeClassifier.detectMultiScale(img, scaleFactor, minNeighbors[, minSize, maxSize])
# - scaleFactor: 작은 박스에서 큰 박스로 검색 윈도우를 증가시키는 비율 (>1)
# - minNeighbors: 검출 객체 영역에서 중복 검출되어야 할 최소값. 최소 검출 횟수(기본 3)
faces = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5)
print('faces')
print(faces)

for (x, y, w, h) in faces:
    cv.rectangle(img, (x,y), (x+w,y+h), (255,0,0),2)
    roi = img[y:y+h, x:x+w] # get face sub region
    # detect eyes in the detected face region
    eyes = eye_cascade.detectMultiScale(roi, scaleFactor=1.1, minNeighbors=5)
    print('eyes')
    print(eyes)
    for (ex,ey,ew,eh) in eyes:
        cv.rectangle(roi, (ex,ey), (ex+ew, ey+eh), (0,255,0), 2)

cv.imshow('img', img)
cv.waitKey()