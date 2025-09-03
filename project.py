## SCREEN RECORDER USING OPENCV

!pip install pyautogui
import cv2
import pyautogui as p
import numpy as np

rs=p.size() ## create resolution

fn=input("Pls enter any file name and path") ## file name in which we store the recordings
fps=60.0 # frame rate
fourcc=cv2.VideoWriter_fourcc(*'XVID')
output=cv2.VideoWriter(fn,fourcc,fps,rs)

cv2.namedWindow("Live Recording",cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live Recording",(600,400))

while True:
    img=p.screenshot()
    f=np.array(img)
    f=cv2.cvtColor(f,cv2.COLOR_BGR2RGB)
    output.write(f)
    cv2.imshow("Live Recording",f)
    if cv2.waitKey(1)==ord("s"):
        break
cv2.destroyAllWindows()
output.release()


### BREAKING VIDEOS INTO MULTIPLE IMAGES(FRAME WISE) AND SAVING IT IN A FOLDER

## when we capture a video we capture multiple frames of the video. so we nned to break those frames an learn how to store them 
vidcap=cv2.VideoCapture("E:\hero.mp4")
ret,image=vidcap.read() ## Read the video
count=0
while True:
    if ret==True:
        cv2.imwrite("E:\\frames\\imgN%d.jpg"%count,image) ## the number of frames thats going to be read are captured here
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count**100))
        ret,image=vidcap.read()
        cv2.imshow("res",image)
        count+=1
        if cv2.waitKey(1)==ord("s"):
            break
            cv2.destroyAllWindows()
vidcap.release()
cv2.destroyAllWindows()
