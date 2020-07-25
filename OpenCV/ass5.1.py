import cv2
import numpy as np

rec = cv2.VideoCapture("lm.mp4")

while True:
	ret , frame = rec.read()
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	blur = cv2.GaussianBlur(gray,(3,3),0)
	ero = cv2.erode(blur, None, iterations=2)
	dil = cv2.dilate(ero, None, iterations=2)
	retu,bw = cv2.threshold(dil,127,255,cv2.THRESH_BINARY)
	'''cv2.imshow("bw",bw)
	if cv2.waitKey(40)==ord("q"):
		break
	'''
	contours,hierarchy = cv2.findContours(bw,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
	for cnt in contours:
		app = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
		area = cv2.contourArea(cnt)
		if 12<len(app)<17 and 5000<area<10000:
			x = app.ravel()[0]
			y = app.ravel()[1] - 4
			cv2.drawContours(frame,[cnt],0,(0,255,0),0)
			cv2.putText(frame, "Circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
			
	cv2.imshow("video",frame)
	if cv2.waitKey(50) == ord("q"):
		break
rec.release()
cv2.destroyAllWindows()