from micropi import LED
from time import sleep

led = LED()

for i in range(4):
    led.set_color(i,i*63,255,255)
    sleep(.5)
    led.set_color(i, 0,0,0)

