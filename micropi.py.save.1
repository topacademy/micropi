#!/usr/bin/python

# Library for MicroPi V2
# Developed by: SB Components & Hypersmart
# Project: micro:Pi

import RPi.GPIO as GPIO
import pigpio
from rpi_ws281x import PixelStrip, Color
# from board import SCL, SDA
# import busio2 as busio
# from oled_text import OledText
import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont
import subprocess
import argparse
import time
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


class Motor:

    # Class to handle interaction with the motor pins
    # Supports redefinition of "forward" and "backward" depending on how motors
    # are connected
    # Use the supplied Motorshieldtest module to test the correct configuration
    # for your project.
    # Arguments:
    # motor = string motor pin label (i.e. "MOTOR1","MOTOR2","MOTOR3","MOTOR4")
    # identifying the pins to which the motor is connected.
    # config = int defines which pins control "forward" and "backward" movement

    motorpins = {"MOTOR4": {"config": {1: {"e": 12, "f": 8, "r": 7}, 2: {"e": 12, "f": 7, "r": 8}}, "arrow": 1},
                 "MOTOR3": {"config": {1: {"e": 21, "f": 9, "r": 11}, 2: {"e": 21, "f": 11, "r": 9}}, "arrow": 2},
                 "MOTOR2": {"config": {1: {"e": 25, "f": 24, "r": 23}, 2: {"e": 25, "f": 23, "r": 24}}, "arrow": 3},
                 "MOTOR1": {"config": {1: {"e": 17, "f": 22, "r": 27}, 2: {"e": 17, "f": 27, "r": 22}}, "arrow": 4}}

    def __init__(self, motor, config):

        self.testMode = False
        self.pins = self.motorpins[motor]["config"][config]
        GPIO.setup(self.pins['e'], GPIO.OUT)
        GPIO.setup(self.pins['f'], GPIO.OUT)
        GPIO.setup(self.pins['r'], GPIO.OUT)
        # 50 Hz frequency
        self.PWM = GPIO.PWM(self.pins['e'], 50)
        self.PWM.start(0)
        GPIO.output(self.pins['e'], GPIO.HIGH)
        GPIO.output(self.pins['f'], GPIO.LOW)
        GPIO.output(self.pins['r'], GPIO.LOW)

    def test(self, state):

        # Puts the motor into test mode
        # When in test mode the Arrow associated with the motor
        # receives power on "forward"
        # rather than the motor. Useful when testing your code.
        # Arguments:
        # state = boolean
        self.testMode = state

    def forward(self, speed):

        # Starts the motor turning in its configured "forward" direction.
        # Arguments:
        # speed = Duty Cycle Percentage from 0 to 100.
        # 0 - stop and 100 - maximum speed
        print("Forward")
        if self.testMode:
            print("arrow")
        else:
            self.PWM.ChangeDutyCycle(speed)
            GPIO.output(self.pins['f'], GPIO.HIGH)
            GPIO.output(self.pins['r'], GPIO.LOW)

    def reverse(self, speed):

        # Starts the motor turning in its configured "reverse" direction.
        # Arguments:
        # speed = Duty Cycle Percentage from 0 to 100.
        # 0 - stop and 100 - maximum speed
        print("Reverse")
        if self.testMode:
            print("Arrow")
        else:
            self.PWM.ChangeDutyCycle(speed)
            GPIO.output(self.pins['f'], GPIO.LOW)
            GPIO.output(self.pins['r'], GPIO.HIGH)

    def stop(self):

        # Stops power to the motor
        print("Stop")
        self.PWM.ChangeDutyCycle(0)
        GPIO.output(self.pins['f'], GPIO.LOW)
        GPIO.output(self.pins['r'], GPIO.LOW)

    def speed(self):

        # Control Speed of Motor
        pass


class LinkedMotors:

        # Links 2 or more motors together as a set.
        # This allows a single command to be used to control a
        # linked set of motors
        # e.g. For a 4x wheel vehicle this allows a single command
        # to make all 4 wheels go forward.
        # Starts the motor turning in its configured "forward" direction.
        # Arguments:
        # *motors = a list of Motor objects

    def __init__(self, *motors):

        self.motor = []
        for i in motors:
            print(i.pins)
            self.motor.append(i)

    def forward(self, speed):

        # Starts the motor turning in its configured "forward" direction.
        # Arguments:
        # speed = Duty Cycle Percentage from 0 to 100.
        # 0 - stop and 100 - maximum speed

        for i in range(len(self.motor)):
            self.motor[i].forward(speed)

    def reverse(self, speed):

        # Starts the motor turning in its configured "reverse" direction.
        # Arguments:
        # speed = Duty Cycle Percentage from 0 to 100.
        # 0 - stop and 100 - maximum speed

        for i in range(len(self.motor)):
            self.motor[i].reverse(speed)

    def stop(self):

        # Stops power to the motor

        for i in range(len(self.motor)):
            self.motor[i].stop()


class Stepper:

    # Defines stepper motor pins on the MotorShield
    # Arguments:
    # motor = stepper motor

    stepperpins = {"STEPPER1":{"en1": 17, "en2": 25, "c1": 27, "c2": 22, "c3": 24, "c4": 23},
                   "STEPPER2":{"en1": 21, "en2": 12, "c1": 9, "c2": 11, "c3": 8, "c4": 7}}

    def __init__(self, motor):
        self.config = self.stepperpins[motor]
        GPIO.output(self.config["en1"], GPIO.HIGH)
        GPIO.output(self.config["en2"], GPIO.HIGH)
        GPIO.output(self.config["c1"], GPIO.LOW)
        GPIO.output(self.config["c2"], GPIO.LOW)
        GPIO.output(self.config["c3"], GPIO.LOW)
        GPIO.output(self.config["c4"], GPIO.LOW)

        GPIO.output(self.config["en1"], GPIO.HIGH)
        GPIO.output(self.config["en2"], GPIO.HIGH)
        GPIO.output(self.config["c1"], GPIO.LOW)
        GPIO.output(self.config["c2"], GPIO.LOW)
        GPIO.output(self.config["c3"], GPIO.LOW)
        GPIO.output(self.config["c4"], GPIO.LOW)


    def setStep(self, w1, w2, w3, w4):

        # Set steps of Stepper Motor
        # Arguments
        # w1,w2,w3,w4 = Wire of Stepper Motor

        GPIO.output(self.config["c1"], w1)
        GPIO.output(self.config["c2"], w2)
        GPIO.output(self.config["c3"], w3)
        GPIO.output(self.config["c4"], w4)

    def forward(self, delay, steps):

        # Rotate Stepper motor in forward direction
        # delay = time between steps (milliseconds)                                                                                                                            Arguments:                                                                                                              delay = time between steps in miliseconds
        # steps = Number of Steps

        for i in range(0, steps):
            self.setStep(1, 0, 0, 0)
            time.sleep(delay)
            self.setStep(0, 1, 0, 0)
            time.sleep(delay)
            self.setStep(0, 0, 1, 0)
            time.sleep(delay)
            self.setStep(0, 0, 0, 1)
            time.sleep(delay)

    def backward(self, delay, steps):

        # Rotate Stepper motor in backward direction
        # Arguments:
        # delay = time between steps
        # steps = Number of Steps

        for i in range(0, steps):
            self.setStep(0, 0, 0, 1)
            time.sleep(delay)
            self.setStep(0, 0, 1, 0)
            time.sleep(delay)
            self.setStep(0, 1, 0, 0)
            time.sleep(delay)
            self.setStep(1, 0, 0, 0)
            time.sleep(delay)

    def stop(self):

        # Stops power to the motor

        print("Stop Stepper Motor")
        GPIO.output(self.config['c1'], GPIO.LOW)
        GPIO.output(self.config['c2'], GPIO.LOW)
        GPIO.output(self.config['c3'], GPIO.LOW)
        GPIO.output(self.config['c4'], GPIO.LOW)


class Sensor:

    # Defines a sensor connected to the sensor pins on the MotorShield
    # Arguments:
    # sensortype = string identifying which sensor is being configured.
    # i.e. "IR1", "IR2", "ULTRASONIC"
    # boundary = an integer specifying the minimum
    # distance at which the sensor
    # will return a Triggered response of True.

    Triggered = False

    def iRCheck(self):

        input_state = GPIO.input(self.config["echo"])
        if input_state is True:
            print("IR Sensor: Object Detected")
            self.Triggered = True
        else:
            self.Triggered = False

    def sonicCheck(self):

        # print("SonicCheck has been triggered")
        time.sleep(0.333)
        GPIO.output(self.config["trigger"], True)
        time.sleep(0.00001)
        GPIO.output(self.config["trigger"], False)
        start = time.time()
        while GPIO.input(self.config["echo"]) == 0:
            start = time.time()
        while GPIO.input(self.config["echo"]) == 1:
            stop = time.time()
        elapsed = stop-start
        measure = (elapsed * 34300)/2
        self.lastRead = measure
        if self.boundary > measure:
            print("Boundary breached")
            print(self.boundary)
            print(measure)
            self.Triggered = True
        else:
            self.Triggered = False

    sensorpins = {"IR1":{"echo":4,"check":iRCheck}, "IR2":{"echo":18, "check":iRCheck},
                      "ULTRASONIC":{"trigger": 5, "echo": 6, "check":sonicCheck}}

    def trigger(self):

        # Executes the relevant routine that activates and takes a
        # reading from the specified sensor.
        # If the specified "boundary" has been breached the Sensor's
        # Triggered attribute gets set to True.

        self.config["check"](self)
        print("Trigger Called")

    def __init__(self, sensortype, boundary):
        self.config = self.sensorpins[sensortype]
        self.boundary = boundary
        self.lastRead = 0
        if "trigger" in self.config:
            print("trigger")
            GPIO.setup(self.config["trigger"], GPIO.OUT)
        GPIO.setup(self.config["echo"], GPIO.IN)


class Arrow():

    # Defines an object for controlling one of the LED
    # arrows on the Motorshield.
    # Arguments:
    # which = integer label for each arrow.
    # The arrow number if arbitrary starting with:
    # 1 = Arrow closest to the Motorshield's power pins
    # and running clockwise round the board
    # 4 = Arrow closest to the motor pins.

    arrowpins = {1: 33, 2: 35, 3: 37, 4: 36}

    def __init__(self):

        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)

    def on(self):

        GPIO.output(self.pin, GPIO.HIGH)

    def off(self):

        GPIO.output(self.pin, GPIO.LOW)


class Buzzer:

    def __init__(self):
        self.buzzer = pigpio.pi()
        self.buzzer.set_mode(16, pigpio.OUTPUT)

    def start(self, freq, duty):
        self.buzzer.set_PWM_frequency(16, freq)
        self.buzzer.set_PWM_dutycycle(16, duty)

    def stop(self):
        self.buzzer.set_PWM_dutycycle(16, 0)
        self.buzzer.stop()


class LED:

    def __init__(self):

        # LED Strip configuration:
        # Number of LED pixels
        LED_COUNT = 4
        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0)
        LED_PIN = 10
        # LED signal frequency in hertz (usually 800khz)
        LED_FREQ_HZ = 800000
        # DMA channel to use for generating signal (try 10)
        LED_DMA = 10
        # Set to 0 for darkest and 255 for brightest
        LED_BRIGHTNESS = 100
        # True to invert the signal (when using NPN transistor level shift)
        LED_INVERT = False
        # set to '1' for GPIOs 13. 19, 41, 45 or 53
        LED_CHANNEL = 0
        # Create NeoPixel object with appropriate configuration.
        self.strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        # Intialize the library (must be called once before other functions).
        self.strip.begin()

    def set_color(self, led, red, green, blue):
        self.strip.setPixelColor(led, Color(red, green, blue))
        self.strip.show()


class  OLED:

    def __init__(self):
        # self.i2c = busio.I2C(SCL, SDA)
        # self.oled = OledText(self.i2c, 128, 64)
        self.display = Adafruit_SSD1306.SSD1306_128_64(rst=None)
        self.display.begin()
        self.display.clear()
        self.display.display()
        self.displayWidth = self.display.width
        self.displayHeight = self.display.height
        self.image = Image.new('1', (self.displayWidth, self.displayHeight))  # create graphics library image buffer
        self.draw = ImageDraw.Draw(self.image)  # create drawing object
        self.font = ImageFont.load_default()  # load and set default font

    # def text(self, str, line):
    #     self.oled.text(str, line)

    def stats(self):

        cmd = "hostname -I | cut -d\' \' -f1"
        IP = subprocess.check_output(cmd, shell = True ).decode('ASCII')
        cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
        CPU = subprocess.check_output(cmd, shell = True ).decode('ASCII')
        cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'"
        MemUsage = subprocess.check_output(cmd, shell = True ).decode('ASCII')
        cmd = "df -h | awk '$NF==\"/\"{printf \"Disk: %d/%dGB %s\", $3,$2,$5}'"
        Disk = subprocess.check_output(cmd, shell = True ).decode('ASCII')

        self.draw.text((0,0), "IP: " + IP + CPU + "\n" + MemUsage + "\n" + Disk, font=self.font, fill=255) 


        self.display.image(self.image)
        self.display.display()


    def __del__(self):                                                                                                          # Clean up                                                                                                              GPIO.cleanup() 
        GPIO.cleanup()

class Button:

    def pb1_callback(self, channel):
        print("Button 1 was pressed!")

    def pb2_callback(self, channel):
        print("Button 2 was pressed!")

    def __init__(self, button1, button2):

        # GPIO.setmode(GPIO.BOARD)
        # pb1 = 37
        # pb2 = 35
        pb1 = 26
        pb2 = 19
        # Set pin 37 and 35 to be an input pin and
        # set initial value to be pulled down
        GPIO.setup(pb1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(pb2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        # Setup event on pin 37 and 35 rising edge
        GPIO.add_event_detect(pb1, GPIO.RISING, callback=button1)
        GPIO.add_event_detect(pb2, GPIO.RISING, callback=button2)
        # Run until someone presses enter
        message = input("Press enter to quit\n\n")

    def __del__(self):
        # Clean up
        GPIO.cleanup()


# ---------------Main------------

if __name__ == "__main__":
    rgb = RGB()
    # buz=Buzzer()
    switch = button()
    rgb.set_color(1, 255, 0, 0)
    while 1:
        test = switch.read_button(2)
        print(test)
        sleep(1)
    # buz.set_buzzer(1000, 128)

