import cv2
import numpy as np

img=cv2.pyrDown(cv2.imread("/Users/chenxingyu/Desktop/PythonLearning/feature2.png", cv2.IMREAD_UNCHANGED))

ret,thresh=cv2.threshold(cv2.cvtColor(img.copy(),cv2.COLOR_BGR2GRAY),127,255,cv2.THRESH_BINARY);
image, contours, hier=cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
	x,y,w,h=cv2.boundingRect(c)
	cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

	rect=cv2.minAreaRect(c)

	box=cv2.boxPoints(rect)

	box=np.int0(box)

	cv2.drawContours(img,[box],0,(0,0,255),3)

	(x,y),radius=cv2.minEnclosingCircle(c)

	center=(int(x),int(y))
	radius=int(radius)

	img=cv2.circle(img,center,radius,(0,255,0),2)

	epsilon=0.01*cv2.arcLength(c,True)
	approx=cv2.approxPolyDP(c,epsilon,True)
	print approx
	cv2.drawContours(img,approx,-1,(0,0,255),3)
	
	hull=cv2.convexHull(c)
	print hull
	cv2.drawContours(img,hull,-1,(255,255,255),3)

cv2.drawContours(img, contours, -1, (255,0,0), 1)
cv2.imshow("contours",img)
cv2.waitKey()
cv2.destroyAllWindows()