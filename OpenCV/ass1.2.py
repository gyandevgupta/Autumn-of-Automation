import cv2

rec = cv2.VideoCapture(0)   # rec ~ record

while True:
	ret,frame = rec.read()
	cv2.imshow("video",frame)
	if cv2.waitKey(1)==ord("q"):
		break

rec.release()
cv2.destroyAllWindows()

