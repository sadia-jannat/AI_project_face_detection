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
    
    
while True:
    ret,frame=video.read()
    #framee=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face=facedetect.detectMultiScale(frame,1.3,5)
    for x,y,w,h in face:       
        count=count+1
        name='image/'+nameID+'/'+str(count)+'.jpg'
        print("create image ok.."+name)
        cv2.imwrite(name, frame[y:y+h,x:x+w]) 
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0, 255, 0),3)
    cv2.imshow("WindowFrame", frame)
    cv2.waitKey(1)
    if count>20:
        break

video.release()
cv2.destroyAllWindows()
    
    
