#!./venv/bin/python

from device import AorusLEDController
from color import *
import time

RAINBOW_COLORS = [
    Red(),
    Orange(),
    Yellow(),
    Green(),
    Blue(),
    Indigo(),
    Violet()
]

if __name__ == "__main__":
    aorus = AorusLEDController()
    aorus.open()  # Ensure the device is open.
    cycles = 10
    wait_time = 2
    for i in range(cycles):
        for color in RAINBOW_COLORS:
            aorus.set_color(color)
            time.sleep(wait_time)
        print(f"Time left: {(cycles - i)*wait_time*len(RAINBOW_COLORS) / 60.0}")

    aorus.set_color(White())
    time.sleep(3)
    aorus.set_color(Off())
    aorus.close()
