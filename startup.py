from micropi import OLED, Button, Buzzer, LED
from time import sleep

button1_pressed = False
button2_pressed = False

def button1(channel):
    global button1_pressed
    button1_pressed = True
    print("Button PB1 pressed " + str(channel))

def button2(channel):
    global button2_pressed
    button2_pressed = True
    print("Button PB2 pressed " + str(channel))

def main():
    global button1_pressed
    global button2_pressed

    oled = OLED()
    oled.stats()

    button = Button(button1, button2)
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
