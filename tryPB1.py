
from micropi import PB1
from time import sleep

pb1 = PB1()
#button1_pressed = False
#button2_pressed = False

#def button1(channel):
#    global button1_pressed
#    button1_pressed = True
#    print("Button PB1 pressed")

#def button2(channel):
#    global button2_pressed
#    button2_pressed = True
#    print("Button PB2 pressed")

#button = Button(button1, button2)
#print("Press Button PB1 to test, press Button PB2 to exit")

#while not button2_pressed:
#    sleep(1)

while True:
    print(PB1.isButtonPressed(pb1))
    sleep(0.2)
