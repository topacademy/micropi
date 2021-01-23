from micropi import OLED
from time import sleep

oled = OLED()

oled.setline(1, "searching for WiFi")
oled.setline(2, "please name, password")
oled.setline(3, "2.4GHz is switched on")

sleep(10)
