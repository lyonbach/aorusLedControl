#!../venv/bin/python

from device import AourusLEDController
from color import Color
import time

# Aorus I X570 PRO WIFI INFO
# idVendor           0x048d Integrated Technology Express, Inc.
# idProduct          0x8297 IT8297 RGB LED Controller

RED = Color(255, 0, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)


if __name__ == "__main__":

    aorus = AourusLEDController()
    aorus.open()  # Ensure the device is open.
    aorus.set_color(GREEN)
    time.sleep(3)
    aorus.set_color(RED)
    time.sleep(3)
    aorus.set_color(BLUE)
    aorus.close()
