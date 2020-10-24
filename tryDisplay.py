from board import SCL, SDA
import busio
from oled_text import OledText
import subprocess

i2c = busio.I2C(SCL, SDA)
# Create the display, pass its pixel dimensions
oled = OledText(i2c, 128, 64)

def stats():

    cmd = "hostname -I | cut -d\' \' -f1"
    IP = subprocess.check_output(cmd, shell = True ).decode('ASCII')
    cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
    CPU = subprocess.check_output(cmd, shell = True ).decode('ASCII')
    cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'"
    MemUsage = subprocess.check_output(cmd, shell = True ).decode('ASCII')
    cmd = "df -h | awk '$NF==\"/\"{printf \"Disk: %d/%dGB %s\", $3,$2,$5}'"
    Disk = subprocess.check_output(cmd, shell = True ).decode('ASCII')

    # Write to the oled
    print(IP)
    oled.text("IP:" + IP, 1)  # Line 1
    oled.text(CPU, 2)  # Line 2
    oled.text(MemUsage, 3)  # Line 2
    oled.text(Disk, 4)  # Line 2
    oled.text("yyyygggg", 5)  # Line 2

stats()

