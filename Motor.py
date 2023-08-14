#!/usr/bin/env python3
import tkinter as tk
import RPi.GPIO as GPIO
import serial
import time

class Motor_driver:
    
    def __init__(self):
        
        self.stop_flag = True
        self.status = "STOP"
        self.D0=21
        self.D1=22
        self.D2=23
        self.D3=24

        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)			

        GPIO.setup(self.D0,GPIO.OUT)
        GPIO.setup(self.D1,GPIO.OUT)
        GPIO.setup(self.D2,GPIO.OUT)
        GPIO.setup(self.D3,GPIO.OUT)
        
        GPIO.output(self.D0,1)
        GPIO.output(self.D1,1)
            
        GPIO.output(self.D2,1)
        GPIO.output(self.D3,1)
        
    def start(self):
        self.stop_flag = False
        
    def gui_init(self):
        
        gui = tk.Tk()
        top_frame = tk.Frame(gui)
        top_frame.pack(side = tk.TOP)
        middle_frame = tk.Frame(gui)
        middle_frame.pack()
        bottom_frame = tk.Frame(gui)
        bottom_frame.pack(side = tk.BOTTOM)
        f = tk.Button(top_frame,text = "start",width = 10,command = self.forward)
        f.pack()
        l = tk.Button(middle_frame,text = "left",width = 10,command = self.left2)
        l.pack(side = tk.LEFT)
        s = tk.Button(middle_frame,text = "stop",width = 10,command = self.stop)
        s.pack(side = tk.LEFT)
        r = tk.Button(middle_frame,text = "right",width = 10,command = self.right3)
        r.pack(side = tk.LEFT)
        b = tk.Button(bottom_frame,text = "reverse",width = 10,command = self.reverse)
        b.pack()
        self.var_for = tk.DoubleVar()
        scale_for = tk.Scale(gui,variable = self.var_for)
        scale_for.pack()
        self.var_rev = tk.DoubleVar()
        scale_rev = tk.Scale(gui,variable = self.var_rev)
        scale_rev.pack()
        gui.mainloop()
        
    def reverse(self):
        self.stop_flag = False
        self.r_speed = 2.55*self.var_rev.get()
        binary = "b:{speed}\n".format(speed = self.r_speed).encode('ascii')
        self.ser.write(binary)
        line = self.ser.readline().decode('utf-8').rstrip()
        print(line)
        time.sleep(0)
        
    def forward(self):
        self.stop_flag = False
        self.status = "FORWARD"
        GPIO.output(self.D0,0)
        GPIO.output(self.D1,0)
            
        GPIO.output(self.D2,0)
        GPIO.output(self.D3,0)
        
        
    def stop(self):
        self.stop_flag = True
        self.status = "STOP"
        GPIO.output(self.D0,1)
        GPIO.output(self.D1,1)
            
        GPIO.output(self.D2,1)
        GPIO.output(self.D3,1)
     
        
    def right1(self):
        self.stop_flag = False
        self.status = "RIGHT1"
        GPIO.output(self.D0,1)
        GPIO.output(self.D1,0)
            
        GPIO.output(self.D2,0)
        GPIO.output(self.D3,0)
        
        #time.sleep(0)
        
    def right2(self):
        self.stop_flag = False
        self.status = "RIGHT2"
        GPIO.output(self.D0,0)
        GPIO.output(self.D1,1)
            
        GPIO.output(self.D2,0)
        GPIO.output(self.D3,0)
      
     
    def right3(self):
        self.stop_flag = False
        self.status = "RIGHT3"
        GPIO.output(self.D0,1)
        GPIO.output(self.D1,1)
            
        GPIO.output(self.D2,0)
        GPIO.output(self.D3,0)
       
        
    def left1(self):
        self.stop_flag = False
        self.status = "LEFT1"
        GPIO.output(self.D0,0)
        GPIO.output(self.D1,0)
            
        GPIO.output(self.D2,1)
        GPIO.output(self.D3,0)
      
        
    def left2(self):
        self.stop_flag = False
        self.status = "LEFT2"
        GPIO.output(self.D0,1)
        GPIO.output(self.D1,0)
            
        GPIO.output(self.D2,1)
        GPIO.output(self.D3,0)
    
        
    def left3(self):
        self.stop_flag = False
        self.status = "LEFT3"
        GPIO.output(self.D0,0)
        GPIO.output(self.D1,1)
            
        GPIO.output(self.D2,1)
        GPIO.output(self.D3,0)
     
    
        
