#!/usr/bin/env python3
import tkinter as tk
import serial
import time

class Motor_driver:
    
    def __init__(self):
        self.ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        self.ser.reset_input_buffer()
        self.f_speed = 0
        self.r_speed = 0
        self.stop_flag = True
    
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
        f = tk.Button(top_frame,text = "start",width = 10,command = self.start)
        f.pack()
        l = tk.Button(middle_frame,text = "left",width = 10,command = self.left)
        l.pack(side = tk.LEFT)
        s = tk.Button(middle_frame,text = "stop",width = 10,command = self.stop)
        s.pack(side = tk.LEFT)
        r = tk.Button(middle_frame,text = "right",width = 10,command = self.right)
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
        #self.f_speed = 2.55*self.var_for.get()
        self.f_speed = 100
        binary = "f:{speed}\n".format(speed = self.f_speed).encode('ascii')
        self.ser.write(binary)
        line = self.ser.readline().decode('utf-8').rstrip()
        print(line)
        #time.sleep(0)
        
    def stop(self):
        self.stop_flag = True
        self.ser.write(b"s:000\n")
        line = self.ser.readline().decode('utf-8').rstrip()
        print(line)
        time.sleep(0)
        
    def left(self):
        self.stop_flag = False
        self.ser.write(b"l:100\n")
        line = self.ser.readline().decode('utf-8').rstrip()
        print(line)
        #time.sleep(0)
        
    def right(self):
        self.stop_flag = False
        self.ser.write(b"r:100\n")
        line = self.ser.readline().decode('utf-8').rstrip()
        print(line)
        #time.sleep(0)
     
    
        

    

    
        
