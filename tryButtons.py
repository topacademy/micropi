from micropi import Button
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
    print("Button PB2 pressed, so exiting program " + str(channel))

def main():
    global button1_pressed
    global button2_pressed

    b = Button(button1, button2)
    print("Press Button 1 to test, press Button 2 to exit")

    while not button2_pressed:
        sleep(1)

if __name__ == "__main__":
    # execute only if run as a script
    main()

