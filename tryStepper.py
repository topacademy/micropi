#A Python script to test motors, stepper motor
#********BEFORE RUNNING THIS, MUST sudo pigpiod !!******
#Can automate this with sudo systemctl enable pigpiod (or disable)

import sys
sys.path.append("/home/pi/MotorShield")

#import pigpio
import PiMotor
import time
import RPi.GPIO as GPIO

#First section:test stepper motor functions

#m1 = PiMotor.Motor("MOTOR1", 1)
#m2 = PiMotor.Motor("MOTOR2", 1)
m = PiMotor.Stepper("STEPPER2")
#motorAll = PiMotor.LinkedMotors(m1,m2)

# Rotate Stepper 1 0.004 = step time, 200 = number of steps
for i in range(2):
	m.forward(0.004,200)
	time.sleep(0.3)
	m.backward(0.004,200)
	time.sleep(0.3)

# Full speed forward, half speed reverse
#motorAll.forward(100)
#time.sleep(20)
#motorAll.stop()
#time.sleep(1)
#motorAll.reverse(50)
#time.sleep(20)
#motorAll.stop()
#Reset ports used by motor program back to input mode
GPIO.cleanup()




