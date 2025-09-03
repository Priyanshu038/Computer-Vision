### TO SHOWCASE THE VIDEO OPERATIONS USING OPENcv

import cv2
cap=cv2.VideoCapture("E:\\Rainy Day _short 30 sec animation_.mp4")
print(cap)

while True:
    ret,frame=cap.read() ## returns 2 values boolean and image
    frame=cv2.resize(frame,(700,450)) ## adjust the frames
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) ## this line of code is written only to chabge the frame to grayscale
    cv2.imshow("frame",frame)
    k=cv2.waitKey(10) ## 0 means static and 25 means the no of seconds in which the frames are passed
    if k==ord("s"): ## This is basically done to control the window
        break
cap.release()
cv2.destroyAllWindows()


### READING THE VIDEOS FROM THE WEBCAM AND SAVING IT IN THE MEMORY
import cv2
cap=cv2.VideoCapture(0)

fourcc=cv2.VideoWriter_fourcc(*"XVID") ## it contains 4 parameters: name,codec,fps,resolution
output=cv2.VideoWriter('E:\\output.avi',fourcc,20.0,(640,480)) ## 20 is the fps
print(cap)

while cap.isOpened():
    ret,frame=cap.read() ##  cap function returns 2 values boolean and image
    if ret==True:
         
         gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) ## this line of code is written only to chabge the frame to grayscale
         cv2.imshow("frame",frame)
         frame=cv2.flip(frame,0)
         cv2.imshow("gray",gray)
         output.write(frame) ## here we need to see the frame its right now color frame  the save will be done for the color frame only but if we want to save for the grayscale frame then we need to pass the gray and in the above foyrcc we need to change or add 0
        
        
         k=cv2.waitKey(100) ## 0 means static and 25 means the no of seconds in which the frames are passed
         if k==ord("s"): ## This is basically done to control the window
             break
        
   
cap.release()
output.release()
cv2.destroyAllWindows()

### VIDEO CAPTURE FROM DIFFERENT SOURCES

import cv2
camera="http://172.17.0.41:8080/video" ## this shows that the camera from the mobile or other device is connected
cap=cv2.VideoCapture(0)
cap.open(camera)

fourcc=cv2.VideoWriter_fourcc(*"XVID") ## it contains 4 parameters: name,codec,fps,resolution
output=cv2.VideoWriter('E:\\hero.mp4',fourcc,20.0,(640,480)) ## 20 is the fps
print(cap)

while cap.isOpened():
    ret,frame=cap.read() ##  cap function returns 2 values boolean and image
    if ret==True:
         frame=cv2.resize(frame,(700,700))
         
         #gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) ## this line of code is written only to chabge the frame to grayscale
         cv2.imshow("frame",frame)
       
         #cv2.imshow("gray",gray)
         output.write(frame) ## here we need to see the frame its right now color frame  the save will be done for the color frame only but if we want to save for the grayscale frame then we need to pass the gray and in the above foyrcc we need to change or add 0
        
        
         k=cv2.waitKey(100) ## 0 means static and 100 means the no of seconds in which the frames are passed
         if k==ord("s"): ## This is basically done to control the window
             break
        
   
cap.release()
output.release()
cv2.destroyAllWindows()

### VIDEO CAPTURE FROM YOUTUBE


import pafy ## this library
url="https://www.youtube.com/watch?v=d95PPykB2vE"
data=pafy.new(url)
data=data.getbest(preftype="mp4")
cap=cv2.VideoCapture(0)
cap.open(data.url)

fourcc=cv2.VideoWriter_fourcc(*"XVID") ## it contains 4 parameters: name,codec,fps,resolution
output=cv2.VideoWriter('E:\\hero.mp4',fourcc,20.0,(640,480)) ## 20 is the fps
print(cap)

while cap.isOpened():
    ret,frame=cap.read() ##  cap function returns 2 values boolean and image
    if ret==True:
         frame=cv2.resize(frame,(700,700))
         
         #gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) ## this line of code is written only to chabge the frame to grayscale
         cv2.imshow("frame",frame)
       
         #cv2.imshow("gray",gray)
         #output.write(frame) ## here we need to see the frame its right now color frame  the save will be done for the color frame only but if we want to save for the grayscale frame then we need to pass the gray and in the above foyrcc we need to change or add 0
        
        
         k=cv2.waitKey(100) ## 0 means static and 100 means the no of seconds in which the frames are passed
         if k==ord("s"): ## This is basically done to control the window
             break
        
   
cap.release()
output.release()
cv2.destroyAllWindows()
