import cv2
import numpy as np

img = cv2.imread('shape.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,bw = cv2.threshold(gray,230,255,cv2.THRESH_BINARY)
cv2.imshow("bw",bw)

contours,hierarchy = cv2.findContours(bw,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
	app = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
	x = app.ravel()[0]
	y = app.ravel()[1] - 4

	'''M = cv2.moments(cnt)
	x = int(M['m10']/M['m00'])
	y = int(M['m01']/M['m00'])'''

	if len(app) == 3:
		cv2.drawContours(img,[cnt],0,(0,255,255),0)
		cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
	
	elif len(app) == 4:
		x1 ,y1, w, h = cv2.boundingRect(app)
		frac = float(w)/h
		
		if frac >= 0.95 and frac <= 1.05:
			cv2.drawContours(img,[cnt],0,(0,255,0),0)
			cv2.putText(img, "square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
		elif frac < 0.95:
			cv2.drawContours(img,[cnt],0,(0,255,0),0)
			cv2.putText(img, "rhombus", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
		
		else:
			cv2.drawContours(img,[cnt],0,(0,255,0),0)
			cv2.putText(img, "rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
	
	elif 6<len(app)<15:
		cv2.drawContours(img,[cnt],0,(0,0,255),0)
		cv2.putText(img, "oval", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
	
	else:
		cv2.drawContours(img,[cnt],0,(255,0,0),0)
		cv2.putText(img, "Circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))


cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
