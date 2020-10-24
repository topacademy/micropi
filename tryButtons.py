from micropi import Button

def button1(channel):
    print("Button 1 " + str(channel))

def button2(channel):
    print("Button 2 " + str(channel))


b = Button(button1, button2)
