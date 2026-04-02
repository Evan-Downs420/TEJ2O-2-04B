"""
Created by: Evan
Created on: Apirl 2026
This module is a Micro:bit MicroPython program
"""

from microbit import *

# Show a happy face on start
display.clear()
display.show(Image.HAPPY)

while True:
    # Check if Button A is pressed
    if button_a.was_pressed():
        # Get the temperature
        temp = temperature()

        display.clear()
        # Scroll the temperature message
        # We use str(temp) to combine the number with the text
        display.scroll("The temperature is: " + str(temp) + "C.")

        # Show the happy face again after scrolling
        display.show(Image.HAPPY)

    # Small sleep to save power
    sleep(100)
