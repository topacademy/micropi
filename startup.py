from micropi import OLED, Buzzer, LED
from time import sleep

def main():

    oled = OLED()
    oled.stats()
    buzzer =  Buzzer()
    led =  LED()

    buzzer.start(588,128)
    led.set_color(0,255,0,0)
    sleep(0.3)
    led.set_color(0,0,0,0)

    buzzer.start(658,128)
    led.set_color(1,0,255,0)
    sleep(0.3)
    led.set_color(1,0,0,0)

    buzzer.start(1046,128)
    led.set_color(2,0,0,255)
    sleep(0.3)
    led.set_color(2,0,0,0)

    buzzer.start(522,128)
    led.set_color(3,255,255,255)
    sleep(0.3)
    led.set_color(3,0,0,0)

    buzzer.start(784,128)
    led.set_color(0,0,128,128)
    sleep(0.3)
    led.set_color(0,0,0,0)

    buzzer.stop()

if __name__ == "__main__":
    # execute only if run as a script
    main()
