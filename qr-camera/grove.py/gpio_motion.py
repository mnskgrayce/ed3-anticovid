#!/usr/bin/env python
 
import time
 
from grove.grove_relay import GroveRelay
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
 
def main():
    # Grove - Ultrasonic Ranger connected to port D5
    sensor = GroveUltrasonicRanger(18)
 

 
    while True:
        distance = sensor.get_distance()
        print('{} cm'.format(distance))
        cTime = time.time()
        currentTime = time.ctime()
        print('time', currentTime)
 
        time.sleep(0.2)
 
if __name__ == '__main__':
    main()