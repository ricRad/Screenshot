import time, sys, cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
from PIL import ImageGrab
 
while True:
	time.sleep(0.5)
	t = str(time.time()).replace('.','-')
	tt = time.time()
	img = ImageGrab.grab()
	#img = img.resize((800,600))
	#plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
	#plt.show()
	img.save('poudou.png')
	cv_img = np.array(img)
	#cv_img = cv_img[:, :, ::-1]
	#print cv_img
	#cv.imwrite('ipk.jpg', cv_img)
	#cv.imshow('screen', cv_img)
	#cv.waitKey(15)
	print time.time() - tt

