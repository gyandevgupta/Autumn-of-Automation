import cv2
import numpy as np 

img = cv2.imread("sn.jpg",cv2.IMREAD_GRAYSCALE)
#cv2.imshow("img",img)

blur = cv2.GaussianBlur(img,(3,3),0)

laplace = cv2.Laplacian(blur,-1,ksize=5)

img_bit = cv2.bitwise_not(laplace)

ret,sketch = cv2.threshold(img_bit,150,255,cv2.THRESH_BINARY)

img2 = cv2.imread("sn.jpg")

cv2.imshow("original",img2)
cv2.imshow("sketch",sketch)

cv2.waitKey(0)
cv2.destroyAllWindows()