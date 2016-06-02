import numpy as np
import cv2
from matplotlib import pyplot as plt

img=cv2.imread('3.png')
mask=np.zeros(img.shape[:2],np.uint8)

bgdModel=np.zeros((1,65),np.float64)
fgdModel=np.zeros((1,65),np.float64)

rect=(20,50,1100,1100)
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)

mask2=np.where((mask==2)|(mask==0),0,1).astype('uint8')
img=img*mask2[:,:,np.newaxis]

plt.subplot(121),plt.imshow(img)
plt.title("grabcut"),plt.xticks([]),plt.yticks([])

plt.subplot(122),plt.imshow(cv2.cvtColor(cv2.imread('3.png'),cv2.COLOR_BGR2RGB))
plt.title("original"),plt.xticks([]),plt.yticks([])
plt.show()