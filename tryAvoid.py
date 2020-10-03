import sys
sys.path.append("/home/pi/GekoHat")

from GekoHat import Motor
from GekoHat import Sensor
import time
import RPi.GPIO as GPIO

m1 = Motor("MOTOR1", 1)
m2 = Motor("MOTOR2", 1)
us = Sensor("ULTRASONIC", 10)

while True:
    m1.forward(60)
    m2.forward(60)
    us.sonicCheck()
    if(us.Triggered):
        print("obtruction detected")
        m1.stop()
        m2.stop()
        time.sleep(1)
        m1.reverse(50)
        m2.reverse(50)
        time.sleep(1)
        m1.stop()
        m2.stop()
        time.sleep(1)
        m1.forward(60)
        time.sleep(1)
#Reset ports used by motor program back to input mode
GPIO.cleanup()
