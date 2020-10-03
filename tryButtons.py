import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

sleepTime = .1

buttonPin1 = 37
buttonPin2 = 35

GPIO.setup(buttonPin1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttonPin2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
	if(GPIO.input(buttonPin1) == 0):
		print("Button 1 Pressed")
		sleep(sleepTime)
	if(GPIO.input(buttonPin2) == 0):
		print("Button 2 Pressed")
		sleep(sleepTime)

