#!/usr/bin/python

# Library for MicroPi V2
# Developed by: SB Components & Hypersmart
# Project: micro:Pi

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
        # delay = time between steps (milliseconds)
        # Arguments: delay = time between steps in miliseconds
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
        print(input_state)
        if input_state == 1:
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


class Buzzer:

    def __init__(self):
        self.buzzer = pigpio.pi()
        self.buzzer.set_mode(16, pigpio.OUTPUT)

    def __del__(self):
        self.buzzer.stop()

    def start(self, freq, duty = 128):
        self.buzzer.set_PWM_frequency(16, freq)
        self.buzzer.set_PWM_dutycycle(16, duty)

    def stop(self):
        self.buzzer.set_PWM_dutycycle(16, 0)
        # self.buzzer.stop()

    def tone(self, f):

       frequencies = [10, 20, 40, 60, 80, 120, 170, 220, 280, 350, 420, 640, 690, 920, 1500, 2000]
       self.buzzer.set_PWM_frequency(16,frequencies[f%16])
       self.buzzer.set_PWM_dutycycle(16,128)



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

    def get_bit_number(self, value):
        if value <=0:
            return 0
        power = 128
        bit = 7
        while value < power:
           power = power // 2
           bit = bit -1
        return bit

    def set_color(self, led, red, green, blue):
        values = [0,5,25,45,65,85,105,125]
        r = values[self.get_bit_number(red%256)]
        g = values[self.get_bit_number(green%256)]
        b = values[self.get_bit_number(blue%256)]
        self.strip.setPixelColor(led %4, Color(r, g, b))
        self.strip.show()


class OLED:

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
        self.line = ["","","",""]


    def clear(self):

        self.display.begin()
        self.display.clear()
        self.draw.rectangle((0,0,127,63), outline=0, fill=0)
        self.display.display()

    def stats(self):

        IP = "IP:" + self.get_ip_address()
        self.setline(0,IP)
        cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
        CPU = subprocess.check_output(cmd, shell = True ).decode('ASCII')
        self.setline(1,CPU)
        cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'"
        MemUsage = subprocess.check_output(cmd, shell = True ).decode('ASCII')
        self.setline(2,MemUsage)
        cmd = "df -h | awk '$NF==\"/\"{printf \"Disk: %d/%dGB %s\", $3,$2,$5}'"
        Disk = subprocess.check_output(cmd, shell = True ).decode('ASCII')
        self.setline(3,Disk)

    def prestats(self):

        line0 = "searching for"
        line1 = "WiFI(2.4GHz)......"
        line2 = "check hotspot is on"
        line3 = "check instructions"
        self.setline(0, line0)
        self.setline(1, line1)
        self.setline(2, line2)
        self.setline(3, line3)
        IP = "IP:" + self.get_ip_address()


    def setline(self, line_number, str):

        if line_number >= 0 and line_number <= 3:
            self.clear()
            self.line[line_number] = str.rstrip("\n")
            self.draw.text((0,0), self.line[0] + "\n" + self.line[1] + "\n" + self.line[2] + "\n"+ self.line[3], font=self.font, fill=255)
            self.display.image(self.image)
            self.display.display()

    def get_ip_address(self):

        ip = "0.0.0.0"
        while len(ip) < 8:
            cmd = "hostname -I"
            ip = subprocess.check_output(cmd, shell = True ).decode('ASCII')
        return ip

    def __del__(self):
        # GPIO.cleanup()
        pass

class Buttons:

    def __init__(self):

        # GPIO.setmode(GPIO.BCM)
        self.pb1 = 26
        self.pb2 = 19

        # Set pin 26 and 19 to be an input pin and
        # set initial value to be pulled down
        GPIO.setup(self.pb1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.pb2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def setcallback(self, button1, button2):

        # Setup event on pin 37 and 35 rising edge
        GPIO.add_event_detect(self.pb1, GPIO.RISING, callback=button1)
        GPIO.add_event_detect(self.pb2, GPIO.RISING, callback=button2)

    def isPB1Pressed(self):
        return GPIO.input(self.pb1) == 0

    def isPB2Pressed(self):
        return GPIO.input(self.pb2) == 0


    def __del__(self):
        # GPIO.cleanup()
        pass


# ---------------Main------------

if __name__ == "__main__":
    print("Welcome to the microPi's library")
