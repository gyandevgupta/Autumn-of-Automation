import cv2
import numpy as np
#from matplotlib import pyplot as plt

img = cv2.imread("t.jpg")
rows,cols,ch = img.shape

#M are for translation , R are for rotation ,
#t for translated image , r for rotated image ,b for blur image 

M1 = np.float32([[1,0,100],[0,1,0]])
M2 = np.float32([[1,0,0],[0,1,50]])
M3 = np.float32([[1,0,-120],[0,1,0]])
M4 = np.float32([[1,0,0],[0,1,-150]])

R1 = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
R2 = cv2.getRotationMatrix2D((cols/2,rows/2),180,1)
R3 = cv2.getRotationMatrix2D((cols/2,rows/2),270,1)
R4 = cv2.getRotationMatrix2D((cols/2,rows/2),45,1)

t1 = cv2.warpAffine(img,M1,(cols,rows))
t2 = cv2.warpAffine(img,M2,(cols,rows))
t3 = cv2.warpAffine(img,M3,(cols,rows))
t4 = cv2.warpAffine(img,M4,(cols,rows))

r1 = cv2.warpAffine(img,R1,(cols,rows))
r2 = cv2.warpAffine(img,R2,(cols,rows))
r3 = cv2.warpAffine(img,R3,(cols,rows))
r4 = cv2.warpAffine(img,R4,(cols,rows))

#warp affine basically applies the matrix M onto the image
cv2.imshow('original', img)

cv2.imshow('t1',t1)
cv2.imshow('t2',t2)
cv2.imshow('t3',t3)
cv2.imshow('t4',t4)

cv2.imshow('r1',r1)
cv2.imshow('r2',r2)
cv2.imshow('r3',r3)
cv2.imshow('r4',r4)


b1 = cv2.blur(img,(3,3))
cv2.imshow("b1",b1)


kernel = np.ones((15,15),np.float32)/225
b2 = cv2.filter2D(img,-1,kernel)
cv2.imshow("b2",b2)


M5 = np.float32([[1,0,50],[0,1,-100]])
t5 = cv2.warpAffine(img,M5,(cols,rows))
R5 = cv2.getRotationMatrix2D((cols/2,rows/2),135,1)
r5 = cv2.warpAffine(t5,R5,(cols,rows))
mix = cv2.blur(r5,(3,3))

cv2.imshow("mix",mix)


'''titles = ["original","t1","t2","t3","t4","r1","r2","r3","r4","b1","b2","mix"]
images = [img,t1,t2,t3,t4,r1,r2,r3,r4,b1,b2,mix]

for i in range(12):
	plt.subplot(3,4,i+1),plt.imshow(images[i])
	plt.title(titles[i])
	plt.xticks([]),plt.yticks([])


plt.show()
'''
cv2.waitKey(0)
cv2.destroyAllWindows()