#! /usr/bin/python
import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient 

time.sleep(1)
import pigpio #importing GPIO library
ESC=4  #Connect the ESC in this GPIO pin 

pi = pigpio.pi();
pi.set_servo_pulsewidth(ESC, 0) 

max_value = 2000 #change this if your ESC's max value is different or leave it be
min_value = 700  #change this if your ESC's min value is different or leave it be
stop_value = 1500


def calibrate():   #This is the auto calibration procedure of a normal ESC
        pi.set_servo_pulsewidth(ESC, stop_value)
        print("wait for it, wiat for it")
        time.sleep(2)
        print("please be patient")
        time.sleep(2)


def run():
	print "Starting press'x' to restart"
    time.sleep(1)
    speed = stop_value    # change your speed if you want to.... it should be between 700 - 2000
    print "Controls - a to decrease speed & d to increase speed OR q to decrease a lot of speed & e to increase a lot of speed"
    print "/n s for stop"
    while True:
        pi.set_servo_pulsewidth(ESC, speed)
        inp = raw_input()
        
        if inp == "q":
            speed -= 100    # decrementing the speed like hell
            print "speed = %d" % speed
        elif inp == "e":    
            speed += 100    # incrementing the speed like hell
            print "speed = %d" % speed
        elif inp == "d":
            speed += 10     # incrementing the speed 
            print "speed = %d" % speed
        elif inp == "a":
            speed -= 10     # decrementing the speed
            print "speed = %d" % speed
        elif inp == "s":
            stop()          #going for the stop function
            break
        else:
            print "WHAT DID I SAID!! Press a,q,d,e for speed and 's' for stop"


def stop(): #This will stop every action your Pi is performing for ESC ofcourse.
    pi.set_servo_pulsewidth(ESC, 0)
    pi.stop()


if __name__ == "__main__":
	calibrate()
	print("y is rightly calibrated, r to recalibrate ")
	while True:
		inp = raw_input()
		if inp == "y":
			break
		elif inp == "r":
			calibrate()
			print("y is rightly calibrated, R to recalibrate ");
		else:
			print " %s is not an option. \n only y and r accepted" % inp

	run()
