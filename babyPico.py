# Currently this code will just endlessly send the letter "h". To stop, rename the file on Pico or Ctrl + C to stop the program using PuTTY.
# To get this working, install CircuitPython 10 (https://circuitpython.org/board/raspberry_pi_pico/) onto the specific Pico and then install
# the 10 library (https://circuitpython.org/libraries) for adafruit_hid. Copy that hid folder into the lib folder on the CIRCUITPY drive.
# I am using the Raspberry Pi Pico 2 W to be entirely clear.

import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices) # Initialize

time.sleep(5) # 5 second delay before executing program

while True:
    kbd.send(Keycode.H)
    time.sleep(5)