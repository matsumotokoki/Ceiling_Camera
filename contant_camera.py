import cv2
import time
import numpy as np
import datetime
import os

im_w = 640
im_h = 480
mtx = np.eye(3)   
dist = np.eye(1,8)
mtx[0,0] = 0.4686179 * im_w
mtx[1,1] = 0.6237603 * im_h
mtx[0,2] = 0.4733335 * im_w
mtx[1,2] = 0.4946764 * im_h
dist[0,0] = -42.0638128 
dist[0,1] = 517.4963412
dist[0,2] = 0.0007395
dist[0,3] = 0.0000672
dist[0,4] = 117.9034263
dist[0,5] = -41.7271568
dist[0,6] = 503.1987806
dist[0,7] = 294.3816648

camera = cv2.VideoCapture(0)
date = datetime.datetime.today().strftime("%Y%M%d%H%M")
dir_name = "jpg_file"+str(date)
os.mkdir(dir_name)
for i in range(700):
    print(str(i+1) + " times")
    return_value, image = camera.read()
    image = cv2.undistort(image,mtx,dist)
    cv2.imwrite('./' + dir_name +'/datas'+str(i)+'.jpg', image)
    time.sleep(1) 
del(camera)
