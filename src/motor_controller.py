import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)			
GPIO.setmode(GPIO.BOARD)

class Motor:
     
    def __init__(self,fl = (32,36,37),
                      fr = (12,40,38),
                      bl = (32,36,33),
                      br = (29,31,35)):
        
        self.state = False
        self.front_left = fl
        self.front_right = fr
        self.back_left = bl
        self.back_right = br
        
    def disp_pins(self):
        
        print("fl = ",self.front_left,", fr = ",self.front_right,
              ", bl = ",self.back_left,", br = ",self.back_right)
     
    def setup(self):
        
        GPIO.setup(self.front_right[0],GPIO.OUT)
        GPIO.setup(self.front_right[1],GPIO.OUT)
        GPIO.setup(self.front_right[2],GPIO.OUT)
        self.pfr_pwm = GPIO.PWM(self.front_right[0],1000)

        GPIO.setup(self.front_left[0],GPIO.OUT)
        GPIO.setup(self.front_left[1],GPIO.OUT)
        GPIO.setup(self.front_left[2],GPIO.OUT)
        self.pfl_pwm = GPIO.PWM(self.front_left[0],1000)

        GPIO.setup(self.back_left[0],GPIO.OUT)
        GPIO.setup(self.back_left[1],GPIO.OUT)
        GPIO.setup(self.back_left[2],GPIO.OUT)
        self.pbl_pwm = GPIO.PWM(self.back_left[0],1000)

        GPIO.setup(self.back_right[0],GPIO.OUT)
        GPIO.setup(self.back_right[1],GPIO.OUT)
        GPIO.setup(self.back_right[2],GPIO.OUT)
        self.pbr_pwm = GPIO.PWM(self.back_right[0],1000)
            
        print("Pins Initialized....!!")
        
    def forward(self,direction = "f",speed = 60,turn_speed = 60):
        
        self.pbr_pwm.start(0)
        self.pbr_pwm.ChangeDutyCycle(speed)
            
        self.pbl_pwm.start(0)
        self.pbl_pwm.ChangeDutyCycle(speed)
        
        GPIO.output(self.back_right[1],0)
        GPIO.output(self.back_right[2],1)
            
        GPIO.output(self.back_left[1],0)
        GPIO.output(self.back_left[2],1)
        
        self.state = True
        
        if direction == "f":
            
            self.pfr_pwm.start(0)
            self.pfr_pwm.ChangeDutyCycle(speed)
            
            self.pfl_pwm.start(0)
            self.pfl_pwm.ChangeDutyCycle(speed)
            
            GPIO.output(self.front_left[1],0)
            GPIO.output(self.front_left[2],1)
            
            GPIO.output(self.front_right[1],0)
            GPIO.output(self.front_right[2],1)  
        
        if direction == "r" or direction == "R":
            
            self.pfr_pwm.start(0)
            self.pfr_pwm.ChangeDutyCycle(turn_speed)
            GPIO.output(self.front_right[1],0)                   #turn clockwise
            GPIO.output(self.front_right[2],1)                   #
            
            self.pfl_pwm.start(0)
            self.pfl_pwm.ChangeDutyCycle(turn_speed)
            GPIO.output(self.front_left[1],1)                    #turn anticlockwise 
            GPIO.output(self.front_left[2],0)                    #
            
        if direction == "l" or direction == "L":
            
            self.pfr_pwm.start(0)
            self.pfr_pwm.ChangeDutyCycle(turn_speed)
            GPIO.output(self.front_right[1],1)                   #turn anticlockwise
            GPIO.output(self.front_right[2],0)                   #
            
            self.pfl_pwm.start(0)
            self.pfl_pwm.ChangeDutyCycle(turn_speed)
            GPIO.output(self.front_left[1],0)                    #turn clockwise 
            GPIO.output(self.front_left[2],1)                    # 
        
    def reverse(self,direction = "b",speed = 60,turn_speed = 60):
            
            self.pbr_pwm.start(0)
            self.pbr_pwm.ChangeDutyCycle(speed)
                
            self.pbl_pwm.start(0)
            self.pbl_pwm.ChangeDutyCycle(speed)
            
            GPIO.output(self.back_right[1],0)
            GPIO.output(self.back_right[2],1)
                
            GPIO.output(self.back_left[1],0)
            GPIO.output(self.back_left[2],1)
            
            self.state = True
            
            if direction == "b":
                
                self.pfr_pwm.start(0)
                self.pfr_pwm.ChangeDutyCycle(speed)
                
                self.pfl_pwm.start(0)
                self.pfl_pwm.ChangeDutyCycle(speed)
                
                GPIO.output(self.front_left[1],1)
                GPIO.output(self.front_left[2],0)
                
                GPIO.output(self.front_right[1],1)
                GPIO.output(self.front_right[2],0)  
            
            if direction == "r" or direction == "R":
                
                self.pfr_pwm.start(0)
                self.pfr_pwm.ChangeDutyCycle(turn_speed)
                GPIO.output(self.front_right[1],0)                   #turn clockwise
                GPIO.output(self.front_right[2],1)                   #
                
                pfl_pwm.start(0)
                pfl_pwm.ChangeDutyCycle(turn_speed)
                GPIO.output(self.front_left[1],1)                    #turn anticlockwise 
                GPIO.output(self.front_left[2],0)                    #
                
            if direction == "l" or direction == "L":
                
                self.pfr_pwm.start(0)
                self.pfr_pwm.ChangeDutyCycle(turn_speed)
                GPIO.output(self.front_right[1],1)                   #turn anticlockwise
                GPIO.output(self.front_right[2],0)                   #
                
                self.pfl_pwm.start(0)
                self.pfl_pwm.ChangeDutyCycle(turn_speed)
                GPIO.output(self.front_left[1],0)                    #turn clockwise 
                GPIO.output(self.front_left[2],1)                    # 
            
