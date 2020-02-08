import cv2
import datetime

fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
video = cv2.VideoWriter('video'+ datetime.datetime.today().strftime("%Y%M%d%H%M%S") +'.mp4', fourcc, 20.0, (640, 480))

img = cv2.imread('image1.jpg')
# hight, width, depth = img.shape[:3]

for i in range(1, 700):
    # img = cv2.imread('image{0:03d}.png'.format(i+1))
    img = cv2.imread('./jpg_file/datas'+ str(i+1) +'.jpg')
    if img is None:
        print("can't read")
        break
    img = cv2.resize(img, (640,480))
    video.write(img)

video.release()
