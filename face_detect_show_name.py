#if not work cv2.need install.command- pip install opencv-python
import cv2
import os
import numpy as np 


video=cv2.VideoCapture(0)

facedetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

count=0

nameID=str(input("Enter Your Name: ")).lower()

image_path='image/'+nameID

isExist=os.path.exists(image_path)

if isExist:
    print("Name is taken")
    nameID=str(input("Enter Your Name again: ")).lower()
else:
    os.makedirs(image_path) 


# Loop to capture webcam footage and display current image
while True:
    success,frame=video.read()
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    # Detecting faces
    face = facedetect.detectMultiScale(gray_scale, 1.2, 4)
    for (x,y,w,h) in face:       
        count=count+1
        name='image/'+nameID+'/'+str(count)+'.jpg'
        print("Create image successfully.\n Image name is: "+name)
        cv2.imwrite(name, frame[y:y+h,x:x+w]) 
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0, 255, 0),3)
       
    #cv2.imshow("WindowFrame", frame)
    cv2.imshow(nameID, frame)
    cv2.waitKey(1)
    if count>2:
        print("Name is taken"+"\n"+"name is:"+nameID)
        nameID=str(input("Enter name again: ")).lower()
        print("Enter 'stop' for close process if you want")
        
    if nameID=="stop":
        break

video.release()
cv2.destroyAllWindows()
#framee=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    
    