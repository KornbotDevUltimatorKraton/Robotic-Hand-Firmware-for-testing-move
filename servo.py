#!/usr/bin/env python

# Author:Chanapai Chuadchum  <teslacoil358@gmail.com>
# Description: move a servo motor and Stepper motor for barrett hand 
# Dependencies: None

from nanpy import (ArduinoApi,SerialManager,Servo)    
import Tkinter 
from Tkinter import* 
import serial 
import cv2 # Computer vision system function for the robotic arm 
import time
Tk = Tkinter.Tk() 
Tk2 = Tkinter.Tk() 
Tk.geometry("1023x750") 
Tk2.geometry('640x480') 
#ser = serial.Serial("/dev/ttyUSB2",115200) # Serial communication for the sensor 
#ser1 = serial.Serial("/dev/ttyUSB0",115200) 
connection = SerialManager() 
a = ArduinoApi(connection=connection) 
Tk.title("Operating environment and Visionsystem reporter") # Operating control for the robotic arm 
Tk2.title("Mannual guild for robotic arm") #Mannual guild line for the robotic arm 
servo3e = Servo(3)
servo3u = Servo(4)
servo1u = Servo(5) 
servo1e = Servo(8)
servo2u = Servo(9) 
servo2e = Servo(10)  
a.pinMode(11,a.OUTPUT)
a.pinMode(12,a.OUTPUT)
a.pinMode(2,a.OUTPUT)
a.pinMode(6,a.OUTPUT)
a.digitalWrite(11,a.HIGH)
def StepperFoward(): 
 a.digitalWrite(2,a.LOW)
 for i in range (0,450,1):
     print (i)
     a.digitalWrite(12,a.HIGH)
     a.digitalWrite(6,a.HIGH)
     time.sleep(0.00002)
     a.digitalWrite(6,a.LOW)
     a.digitalWrite(12,a.LOW)
     time.sleep(0.00002)
time.sleep(0.1)
def StepperBackward(): 
 a.digitalWrite(11,a.LOW)
 a.digitalWrite(2,a.HIGH)
 for i in range (0,450,1):
     print(i)
     a.digitalWrite(12,a.HIGH)
     a.digitalWrite(6,a.HIGH)
     time.sleep(0.00002)
     a.digitalWrite(6,a.LOW)
     a.digitalWrite(12,a.LOW)
     time.sleep(0.00002)

 
for move in range (20,180,1):
    print(move) 
    #print(ser.readline()) 
    servo3e.write(10-move)
    servo3u.write(move)
    servo1u.write(4+move) 
    servo1e.write(5+move)
    servo2u.write(170-move) 
    servo2e.write(move) 
    time.sleep(0.01)
     
time.sleep(0.1)
StepperFoward()  
for move in range (180,19,-1): 
          print(move) 
        #  print(ser.readline()) 
          servo3e.write(move)
          servo3u.write(move)
          servo1u.write(4+move)
          servo1e.write(5+move)
          servo2u.write(180-move)
          servo2e.write(move)
          time.sleep(0.01)
          
time.sleep(0.1)
StepperBackward()  
Tk.mainloop() 
