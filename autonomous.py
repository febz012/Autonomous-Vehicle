from picamera.array import PiRGBArray
from picamera import PiCamera
import motor_controller as mc
import time
import cv2 as cv
import numpy as np

class Autonomous:
    
    
    def __init__(self,CameraResolution = (640,480),
                      CameraFrameRate = 60,
                      DisplayResolution = (1280,720),
                      fl = (32,36,37),
                      fr = (12,40,38),
                      bl = (32,36,33),
                      br = (29,31,35)):
        self.Capture_Image = None
        self.CameraResolution = CameraResolution
        self.CameraFrameRate = CameraFrameRate
        self.DisplayResolution = DisplayResolution
        self.motor = mc.Motor(fl,fr,bl,br)
        self.Lane_Offset = 0
        
    def init_camera(self):
        
        print("Initializing Camera...!!")
        self.camera = PiCamera(resolution = self.CameraResolution)
        self.camera.framerate = self.CameraFrameRate
        self.rawCapture = PiRGBArray(self.camera,size = self.CameraResolution)
        # allow the camera to warmup
        time.sleep(1)
        print("Done...!!")
        
    def capture_camera(self):
        # grab an image from the camera
        for frame in self.camera.capture_continuous(self.rawCapture, format="bgr", use_video_port=True):
            #grab the raw NumPy array representing the image, then initialize the timestamp  # and occupied/unoccupied text
            self.Capture_Image = frame.array
            #image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
#             cv.namedWindow("imagewin2", cv.WINDOW_KEEPRATIO)
#             cv.resizeWindow("imagewin2",self.DisplayResolution[0],self.DisplayResolution[1])
#             cv.imshow("imagewin2", self.Capture_Image)
            
            self.image_process()
            key = cv.waitKey(1) & 0xFF

            if key == ord('q'):
                #cv.destroyWindow("imagewin2")
                break
             # clear the stream in preparation for the next frame
            self.rawCapture.truncate(0)
            # if the `q` key was pressed, break from the loo
            

    def draw_roi(self,image,points,color = (0,0,255),thickness = 1):
        
        cv.line(image,points[0],points[1],color,thickness)
        cv.line(image,points[1],points[2],color,thickness)
        cv.line(image,points[2],points[3],color,thickness)
        cv.line(image,points[3],points[0],color,thickness)

    def lane_detection(self,histogramlane,thresholded):
        
        ROIlane = np.array([])
        histogramlane.resize(320)
        histogramlane[:] = 0
        
        for i in range(320):
            ROIlane = thresholded[140:240,i]
            ROIlane = ROIlane/255
            histogramlane[i] = np.sum(ROIlane)
            
        leftpos = np.argmax(histogramlane[0:130])
        rightpos = np.argmax(histogramlane[320:170:-1])             
        cv.line(thresholded,(leftpos,0),(leftpos,240),(0,255,0),2)
        cv.line(thresholded,(320-rightpos,0),(320-rightpos,240),(0,255,0),2)
        
        lanecenter = (320-rightpos+leftpos)//2
        #print("lanecenter",lanecenter)
        cv.line(thresholded,(lanecenter,0),(lanecenter,240),(0,0,255),2)
        framecenter = 160
        cv.line(thresholded,(framecenter,0),(framecenter,240),(255,0,0),2)
        self.create_win("thresholded1",thresholded)
        Lane_Offset = lanecenter-framecenter
        return Lane_Offset
        
    def create_win(self,name,image,win_size = (640,480)):
                      
        cv.namedWindow(name, cv.WINDOW_KEEPRATIO)
        cv.resizeWindow(name,win_size[0],win_size[1])
        cv.imshow(name,image)
    
    def image_process(self):
        
        imag=cv.resize(self.Capture_Image,(320,240) , interpolation = cv.INTER_AREA)


        points1= [(0,220),(20,180),(300,180),(320,220)]
        pointsdes1 = [(0,240),(0,0),(320,0),(320,240)]
        points = np.float32(points1)
        pointsdes = np.float32( pointsdes1)
        histogramlane = np.zeros(320)
        
        self.draw_roi(imag,points1)
        matrix = cv.getPerspectiveTransform(points,pointsdes)
        result = cv.warpPerspective(imag, matrix, (320,240)) 
#         self.create_win("imagewin",imag)
#         self.create_win("perspective",result)

        result = cv.cvtColor(result, cv.COLOR_BGR2GRAY)
        #self.create_win("grayed",result)
        
        ret,thresholded = cv.threshold(result,100,255,cv.THRESH_BINARY)
        #self.create_win("Thresholded",thresholded)

        #edge = cv.Canny(thresholded,100,500,4)
        #cv.namedWindow("canny", cv.WINDOW_KEEPRATIO)
        #cv.resizeWindow("canny", 640, 480)
        #cv.imshow("canny",edge)

        thresholded = cv.cvtColor(thresholded, cv.COLOR_GRAY2BGR)
        self.Lane_Offset = self.lane_detection(histogramlane,thresholded) 
        
        imag = cv.putText(imag,"{}".format(self.Lane_Offset),(0,50),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,255),2, cv.LINE_AA)

        self.create_win("imag2",imag)
        cv.waitKey(1)
