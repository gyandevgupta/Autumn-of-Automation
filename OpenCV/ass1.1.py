import cv2
gray = cv2.imread('sn.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow("gray img",gray)
ret,bw = cv2.threshold(gray, 127 , 255, cv2.THRESH_BINARY)
cv2.imshow(" b&w img",bw)
cv2.waitKey(0)
cv2.destroyAllWindows()
