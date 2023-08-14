import autonomous
import cv2 as cv
import numpy as np
import time
import threading
import Motor
    
def main():
    
    
    def thread1():
    
        auto.init_camera()
        auto.capture_camera()
        
    def thread2():
        
#         motor.gui_init()
        
        while True:
            #print(motor.stop_flag)
            if(motor.stop_flag == False):
                if auto.Lane_Offset > 15 and  auto.Lane_Offset <=30:
                    motor.right2()

                elif auto.Lane_Offset >30 and auto.Lane_Offset <=60:
                    motor.right2()
                elif auto.Lane_Offset >60:
                    motor.right3()
                elif auto.Lane_Offset >-30 and auto.Lane_Offset <=-15:
                    motor.left1()
                elif auto.Lane_Offset >-60 and auto.Lane_Offset <=-30:
                    motor.left2()
                elif auto.Lane_Offset <=-60:
                    motor.left3()
                else:
                    motor.forward()
            
                    
        
    def thread3():
        motor.gui_init()
        
    def thread4():
        
        timer = 0
        while True:
            print("LOG(",timer,") : [ VEHICLE STATUS =",motor.status,"] [ Lane error= ",auto.Lane_Offset,"]")
            time.sleep(0.1)
            timer = timer + 100
        
    Camera_resolution = (320,240)
    Frame_rate = 32
    Display_resolution = (1280,720)
    
    auto = autonomous.Autonomous(Camera_resolution,Frame_rate,Display_resolution)
    motor = Motor.Motor_driver()
    Thread1 = threading.Thread(target = thread1)
    Thread2 = threading.Thread(target = thread2)
    Thread3 = threading.Thread(target = thread3)
    Thread4 = threading.Thread(target = thread4)
    
    Thread1.start()
    Thread2.start()
    Thread3.start()
    Thread4.start()
    


        
    
    
        #     imag=cv.imread("road.jpg")
#     imag=cv.resize(imag,(320,240) , interpolation = cv.INTER_AREA)
# 
#     points1= [(0,180),(65,150),(150,150),(150,180)]
#     pointsdes1 = [(60,240),(60,0),(300,0),(300,240)]
#     points = np.float32(points1)
#     pointsdes = np.float32( pointsdes1)
#     histogramlane = np.zeros(320)
#     
#     auto.draw_roi(imag,points1)
#     matrix = cv.getPerspectiveTransform(points,pointsdes)
#     result = cv.warpPerspective(imag, matrix, (320,240)) 
#     auto.create_win("imagewin",imag)
#     auto.create_win("perspective",result)
# 
#     result = cv.cvtColor(result, cv.COLOR_BGR2GRAY)
#     auto.create_win("grayed",result)
#     
#     ret,thresholded = cv.threshold(result,180,255,cv.THRESH_BINARY)
#     auto.create_win("Thresholded",thresholded)
# 
#     #edge = cv.Canny(thresholded,100,500,4)
#     #cv.namedWindow("canny", cv.WINDOW_KEEPRATIO)
#     #cv.resizeWindow("canny", 640, 480)
#     #cv.imshow("canny",edge)
# 
#     thresholded = cv.cvtColor(thresholded, cv.COLOR_GRAY2BGR)
#     Lane_Offset = auto.lane_detection(histogramlane,thresholded) 
#     
#     imag = cv.putText(imag,"{}".format(Lane_Offset),(0,50),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,255),2, cv.LINE_AA)
# 
#     auto.create_win("imag2",imag)
    cv.waitKey(1)
    



if __name__ == "__main__":
    main()
    
