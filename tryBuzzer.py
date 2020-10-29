from micropi import Buzzer
from time import sleep

b = Buzzer()
#b.start(1000,128)
#sleep(0.3)

# b.stop()

b.start(294*2,128)
sleep(0.3)

b.start(329*2,128)
sleep(0.3)

b.start(523*2,128)
sleep(0.3)

b.start(261*2,128)
sleep(0.3)

b.start(392*2,128)
sleep(0.3)

b.stop()
