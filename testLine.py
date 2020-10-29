#!/usr/bin/python

import RPi.GPIO as GPIO
import pigpio
from rpi_ws281x import PixelStrip, Color
import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont
import subprocess
import argparse
import time
from time import sleep

GPIO.setmode(GPIO.BCM)

left_sensor = 4
right_sensor = 18

GPIO.setup(left_sensor, GPIO.IN)
GPIO.setup(right_sensor, GPIO.IN)

try:
	while True:
		if not GPIO.input(left_sensor):
			print("Robot is straying off to the right, move left captain!")
		elif not GPIO.input(right_sensor):
			print("Robot is straying off to the left, move right captain!")
		else:
			print("Following the line!")
		sleep(0.2)
except:
	GPIO.cleanup()
