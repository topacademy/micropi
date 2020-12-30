from micropi import PB2
from time import sleep

pb2 = PB2()

while True:
    print(PB2.isButtonPressed(pb2))
    sleep(0.2)
