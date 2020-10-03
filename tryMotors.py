import sys
sys.path.append("/home/pi/GekoHat")

import GekoHat
import time
import RPi.GPIO as GPIO

m1 = GekoHat.Motor("MOTOR1", 1)
m2 = GekoHat.Motor("MOTOR2", 1)

m1.forward(60)
m2.forward(60)
time.sleep(5)
m1.stop()
m2.stop()
time.sleep(1)
m1.reverse(50)
m2.reverse(50)
time.sleep(5)
m1.stop()
m2.stop()
#Reset ports used by motor program back to input mode
GPIO.cleanup()




