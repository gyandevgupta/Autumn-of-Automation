import cv2
import numpy as np 

rec = cv2.VideoCapture(0)

while True:
	ret,frame = rec.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	blur = cv2.GaussianBlur(gray,(3,3),0)

	laplace = cv2.Laplacian(blur,-1,ksize=5)

	img_bit = cv2.bitwise_not(laplace)

	ret,sketch = cv2.threshold(img_bit,127,255,cv2.THRESH_BINARY)
	#sketch = cv2.Canny(img_bit,100,200)

	cv2.imshow("original",frame)
	cv2.imshow("sketch",sketch)

	if cv2.waitKey(1) == ord("q"):
		break

rec.release()
cv2.destroyAllWindows()