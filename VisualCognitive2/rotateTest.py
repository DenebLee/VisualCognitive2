import cv2
resized = cv2.imread("image/hat.png", cv2.IMREAD_GRAYSCALE)
height, width = resized.shape[:2]

matrix = cv2.getRotationMatrix2D((width / 2, height / 2), 45, 1)
resized = cv2.warpAffine(resized, matrix, (width, height), borderValue=255)

cv2.imshow("rot45", resized)
cv2.waitKey(0)