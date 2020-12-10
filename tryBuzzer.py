from micropi import Buzzer
from time import sleep

buzzer = Buzzer()

buzzer.start(588,128)
sleep(0.3)

buzzer.start(658,128)
sleep(0.3)

buzzer.start(1046,128)
sleep(0.3)

buzzer.start(522,128)
sleep(0.3)

buzzer.start(784,128)
sleep(0.3)

buzzer.stop()
