
import comparison_of_image_with_encoding1 as facerec
import numpy as np
#import serial
import time
import sys
import cv2

#exe_time=time.time()+40
#sys.path.append('/usr/local/lib/python2.7/site-packages')

#Setup Communication path for arduino (In place of 'COM5' (windows) or ''/dev/tty.usbmodemxxx' (mac) put the port to which your arduino is connected)
#arduino = serial.Serial(port='/dev/ttyACM0', baudrate=9600)
#time.sleep(2)
print("Connected to Arduino...")

#importing the Haarcascade for face detection
face_cascade = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")
print("iam here hello")
#To capture the video stream from webcam.
cap = cv2.VideoCapture(0)
print("Getting camera image...")
#Read the captured image, convert it to Gray image and find faces
global cock
global a

a=0
#path="./images/pic1.jpg"
cock=0
fob=facerec.facedetect()
while 1:

    ret, img = cap.read()
    cv2.namedWindow('img', cv2.WINDOW_NORMAL)
    #cv2.resizeWindow('img', 500,500)
    # cv2.line(img,(500,250),(0,250),(0,255,0),1)
    # cv2.line(img,(250,0),(250,500),(0,255,0),1)
    # cv2.circle(img, (250, 250), 5, (255, 255, 255), -1)
    gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3)
    #fob=facerec.facedetect()

#detect the face and make a rectangle around it.
    for (x,y,w,h) in faces:
        #print(faces)
        no_face=faces.shape[0]
        #print(" i found "+str(no_face)+" faces in the image")
        try:
            if(cock==50):
                #cock=1
                fob.unknownface(img)
                fob.printname(no_face)
                del cock
                #clock=int(input())
                #cv2.imshow("image",img)
                #cv2.waitKey(0)
            cock+=1#(cock+1)%100
        except NameError: pass
#         if(time.time()>=exe_time):
#             fob.unknownface(img)
#             fob.printname()
#             exe_time=time.time()+120
#             
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)
        roi_gray  = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
            

        arr = {y:y+h, x:x+w}
#         print (arr)

#         print ('X :',x)
#         print ('Y :',y)
#         print ('x+w :' ,(x+w))
#         print ('y+h :' ,(y+h))

#  #Center of roi (Rectangle)
#         xx = int(x+(x+h)/2)
#         yy = int(y+(y+w)/2)
#         cv2.circle(img, (xx, yy), 5, (0, 255, 255), 2)
#         print (xx)
#         print (yy)
#         center = (xx,yy)

 # sending data to arduino
#         print("Center of Rectangle is :", center)
#         data = "X{0:d}Y{1:d}Z".format(xx, yy)
#         print(type(data))
#         print(type(data.encode()))
#         print ("output = '" +data+ "'")
#         arduino.write(data.encode())

#Display the stream.
    cv2.imshow('img',img)

#Hit 'Esc' to terminate execution
    k = cv2.waitKey(30) & 0xff
    if k == 27:
       break

#face.py
#Displaying face.py.

