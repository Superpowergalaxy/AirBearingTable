#!/usr/bin/python
import RobotRaconteur as RR
RRN=RR.RobotRaconteurNode.s
#import threading
#import serial
import struct
import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient 
#os.system ("sudo pigpiod") #Launching GPIO library

time.sleep(1)
import pigpio #importing GPIO library
ESC1=4  #Connect the ESC in this GPIO pin 
ESC2=5
ESC3=6

pi = pigpio.pi();
pi.set_servo_pulsewidth(ESC1, 0)
pi.set_servo_pulsewidth(ESC2, 0)
pi.set_servo_pulsewidth(ESC3, 0) 
time.sleep(1)
# set motor constant
max_value = 2000 #change this if your ESC's max value is different or leave it be
min_value = 700  #change this if your ESC's min value is different or leave it be
stop_value = 1500


class create_impl(object):
    def __init__(self):
        self.ESC1speed = stop_value
        self.ESC2speed = stop_value
        self.ESC3speed = stop_value
        pi.set_servo_pulsewidth(ESC1, stop_value)
        pi.set_servo_pulsewidth(ESC2, stop_value)
        pi.set_servo_pulsewidth(ESC3, stop_value)
        print("wait for it, wiat for it")
        time.sleep(2)
        print("please be patient")
        time.sleep(2)
        print("started \n ESC1 = %d \n ESC1 = %d \n ESC1 = %d \n" %(velocity1 , velocity2 , velocity3) )


    def DriveSpeed(self, velocity1, velocity2,velocity3):
        self.ESC1speed = velocity1
        self.ESC2speed = velocity2
        self.ESC3speed = velocity3
        pi.set_servo_pulsewidth(ESC1, velocity1)
        pi.set_servo_pulsewidth(ESC2, velocity2)
        pi.set_servo_pulsewidth(ESC3, velocity3)
        print(" ESC1 = %d \n ESC1 = %d \n ESC1 = %d \n" %(velocity1 , velocity2 , velocity3) )

    def SpeedUp(self, velocity1, velocity2,velocity3):
        self.ESC1speed = self.ESC1speed + velocity1
        self.ESC2speed = self.ESC2speed + velocity2 
        self.ESC3speed = self.ESC3speed + velocity3
        pi.set_servo_pulsewidth(ESC1, velocity1)
        pi.set_servo_pulsewidth(ESC2, velocity2)
        pi.set_servo_pulsewidth(ESC3, velocity3)
        print(" ESC1 = %d \n ESC1 = %d \n ESC1 = %d \n" %(velocity1 , velocity2 , velocity3) )



    def __del__(self):
        pi.set_servo_pulsewidth(ESC1, stop_value)
        pi.set_servo_pulsewidth(ESC2, stop_value)
        pi.set_servo_pulsewidth(ESC3, stop_value)
        pi.set_servo_pulsewidth(ESC1, 0)
        pi.set_servo_pulsewidth(ESC2, 0)
        pi.set_servo_pulsewidth(ESC3, 0)
        time.sleep(1)




#Create and register a transport
t=RR.TcpTransport()
t.StartServer(52222)
RRN.RegisterTransport(t)

#Register the service type
RRN.RegisterServiceType(minimal_create_interface)

create_inst=create_impl()

#Register the service
RRN.RegisterService("MotorController","experimental.minimal_create.MotorController_obj",create_inst)

#Wait for program exit to quit
raw_input("Press enter to quit")