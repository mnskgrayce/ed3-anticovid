#!/usr/bin/env python
 
import time
 
from grove.grove_relay import GroveRelay
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
 
def main():
    # Grove - Ultrasonic Ranger connected to port D5
    sensor = GroveUltrasonicRanger(18)
 
    # Grove - Relay connected to port D16
    relay = GroveRelay(16)
 
    while True:
        distance = sensor.get_distance()
        print('{} cm'.format(distance))
        if (distance < 15):
            print('ok')
        time.sleep(1)
 
if __name__ == '__main__':
    main()


                # Display Humiity and Temperture  
        humi, temp = temp_sensor.read()                        # read temperture and humidity data from sensor
        mois = moisture_sensor.moisture
        lcd.clear()
        # write temp and humi to lcd
        lcd.setCursor(0, 0)                                   
        lcd.write('Tem:{}C'.format(temp))                      # write temperture to lcd
        lcd.setCursor(1, 0)
        lcd.write('Hum:{}%'.format(humi))                      # write humididy to lcd
        lcd.setCursor(0, 8)
        lcd.write('Moi:{}%'.format(mois))             # write moisture to lcd      
        lcd.setCursor(1, 8)                                # Write total people in room
        lcd.write('total:{}'.format(total))
        time.sleep(1)