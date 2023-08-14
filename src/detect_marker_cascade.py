from PIL import Image
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import numpy as np
import time

CameraResolution = (640,480)
CameraFrameRate = 60
DisplayResolution = (1280,720)
Capture_Image = None
print("Initializing Camera...!!")
camera = PiCamera(resolution = CameraResolution)
camera.contrast = 0
camera.framerate = CameraFrameRate
rawCapture = PiRGBArray(camera,size = CameraResolution)
        # allow the camera to warmup
time.sleep(1)
print("Done...!!")

STOP = cv2.CascadeClassifier('data/stop.xml')
UTURN = cv2.CascadeClassifier('data/Uturn.xml')
#ZEBRA = cv2.CascadeClassifier('data/zebra.xml')


for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
            #grab the raw NumPy array representing the image, then initialize the timestamp  # and occupied/unoccupied text
            Capture_Image = frame.array
            # Source image
            gray = cv2.cvtColor(Capture_Image, cv2.COLOR_BGR2GRAY)
            cv2.namedWindow("Footage", cv2.WINDOW_KEEPRATIO)
            cv2.resizeWindow("Footage",640,480)
            cv2.imshow("Footage",Capture_Image)
            
            # image, reject levels level weights.
            
            stop = STOP.detectMultiScale(gray, scaleFactor=1.05,minSize=(24, 24), flags=cv2.CASCADE_SCALE_IMAGE)
            uturn = UTURN.detectMultiScale(gray, scaleFactor=1.05,minSize=(24, 24), flags=cv2.CASCADE_SCALE_IMAGE)
            #zebra = ZEBRA.detectMultiScale(gray, scaleFactor=1.05,minSize=(24, 24), flags=cv2.CASCADE_SCALE_IMAGE)
            print(stop,uturn)
            if (len(stop)):
                cv2.rectangle(Capture_Image, (stop[0][0], stop[0][1]), (stop[0][0] + stop[0][2], stop[0][1] + stop[0][3]), (255, 255, 0), 2)
                Capture_Image = cv2.putText(Capture_Image,"stop",(0,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,255),2, cv2.LINE_AA)
                cv2.imshow("Footage",Capture_Image)
             # clear the stream in preparation for the next frame
            if (len(uturn)>0):
                cv2.rectangle(Capture_Image, (uturn[0][0], uturn[0][1]), (uturn[0][0] + uturn[0][2], uturn[0][1] + uturn[0][3]), (255, 255, 0), 2)
                Capture_Image = cv2.putText(Capture_Image,"uturn",(0,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,255),2, cv2.LINE_AA)
                cv2.imshow("Footage",Capture_Image)
                
            if (0):
                cv2.rectangle(Capture_Image, (zebra[0][0], zebra[0][1]), (zebra[0][0] + zebra[0][2], zebra[0][1] + zebra[0][3]), (255, 255, 0), 2)
                Capture_Image = cv2.putText(Capture_Image,"zebra",(0,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,255),2, cv2.LINE_AA)
                cv2.imshow("Footage",Capture_Image)
            cv2.waitKey(1)
            rawCapture.truncate(0)
            