from rpi_ws281x import PixelStrip, Color
import argparse
import time

# LED strip configuration:
LED_COUNT = 4         # Number of LED pixels.
#LED_PIN = 21          # GPIO pin connected to the pixels (18 uses PWM!).
LED_PIN = 10          # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 100  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

# Create NeoPixel object with appropriate configuration.
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
# Intialize the library (must be called once before other functions).
strip.begin()

# Pixel_forward
strip.setPixelColor(0, Color(255,0,0))
strip.setPixelColor(1, Color(0,0,0))
strip.setPixelColor(2, Color(0,0,0))
strip.setPixelColor(3, Color(0,0,0))
strip.show()
time.sleep(2)

# Pixel_reverse
strip.setPixelColor(0, Color(0,0,0))
strip.setPixelColor(1, Color(0,0,0))
strip.setPixelColor(2, Color(255,0,0))
strip.setPixelColor(3, Color(0,0,0))
strip.show()
time.sleep(2)

# Pixel_right
strip.setPixelColor(0, Color(0,0,0))
strip.setPixelColor(1, Color(0,255,0))
strip.setPixelColor(2, Color(0,0,0))
strip.setPixelColor(3, Color(0,0,0))
strip.show()
time.sleep(2)

# Pixel_left
strip.setPixelColor(0, Color(0,0,0))
strip.setPixelColor(1, Color(0,0,0))
strip.setPixelColor(2, Color(0,0,0))
strip.setPixelColor(3, Color(0,255,0))
strip.show()
time.sleep(2)

# Pixel_off
strip.setPixelColor(0, Color(0,0,0))
strip.setPixelColor(1, Color(0,0,0))
strip.setPixelColor(2, Color(0,0,0))
strip.setPixelColor(3, Color(0,0,0))
strip.show()
time.sleep(2)


