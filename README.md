# AI_project_face_detection
All code written by python language.Use cv2,os,numpy as np,cv2.VideoCapture(0),frame=video.read(),detectMultiScale(gray_scale, 1.2, 4),webcam_video.read(),
cvtColor(video, cv2.COLOR_BGR2HSV),cv2.inRange(img, lower, upper),cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE),cv2.rectangle(video, (x, y), (x + w, y + h), (0, 0, 255), 3)
cv2.boundingRect(mask_contour),cascade.detectMultiScale(gray_scale, 1.2, 4).
Main: path = "haarcascade_frontalface_default.xml"
cv2.imshow("img", image)
cv2.waitKey(1)
Run the code use run icon option
