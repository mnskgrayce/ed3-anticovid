#!/usr/bin/env python
 
import time
 
from grove.grove_relay import GroveRelay
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
count = 0
def main():
    global count
    # Grove - Ultrasonic Ranger connected to port D5
    sensor = GroveUltrasonicRanger(18)
 
    # Grove - Relay connected to port D16
    relay = GroveRelay(16)
 
    while True:
        distance = sensor.get_distance()
        print('{} cm'.format(distance))
        if (distance < 8):
            count += 1
            if (count == 4):
                print('ok')
                count = 0
        time.sleep(0.1)
 
if __name__ == '__main__':
    main()
