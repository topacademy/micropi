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
    buzzer.start(294*2, 128)
    sleep(0.3)
    buzzer.stop()

    led =  LED()

    for i in range(4):
        led.set_color(i, i*63, 255, 255)
        sleep(0.5)
        led.set_color(i, 0,0,0)

if __name__ == "__main__":
    # execute only if run as a script
    main()

