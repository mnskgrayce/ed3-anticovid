#!/usr/bin/env python
 
import time

 
from grove.button import Button
from grove.grove_ryb_led_button import GroveLedButton
 
def main():
    # Grove - LED Button connected to port D5
    button = GroveLedButton(16)
    
    button.led.light(True)
    time.sleep(1)
    button.led.light(False)
 

 
    # button.on_event = on_event
 
    while True:
            
        button.led.light(True)
        time.sleep(1)
        button.led.light(False)
        time.sleep(1)
 
if __name__ == '__main__':
    main()