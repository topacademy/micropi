from micropiV2 import Buzzer
from time import sleep

b = Buzzer()
b.start(1000,128)
sleep(0.3)

b.stop()
