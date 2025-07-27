#!../venv/bin/python

from device import AourusLEDController
import time

# Aorus I X570 PRO WIFI INFO
# idVendor           0x048d Integrated Technology Express, Inc.
# idProduct          0x8297 IT8297 RGB LED Controller

if __name__ == "__main__":
    r = 255
    g = 0
    b = 0
    aorus = AourusLEDController()
    aorus.open()  # Ensure the device is open.
    for idx in range(4):
        aorus.current_group_idx = idx
        aorus.color = (r, g, b)
        aorus.update()
    aorus.close()
