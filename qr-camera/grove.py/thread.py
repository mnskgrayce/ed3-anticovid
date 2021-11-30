import threading
# libarry for grove sensor
import time
from datetime import datetime
from seeed_dht import DHT
from grove.display.jhd1802 import JHD1802
from mraa import getGpioLookup
from grove.grove_mini_pir_motion_sensor import GroveMiniPIRMotionSensor
from grove.grove_moisture_sensor import GroveMoistureSensor
from grove.gpio import GPIO
import sys
from grove.button import Button
from grove.grove_ryb_led_button import GroveLedButton

start = time.perf_counter()
# Grove - Temperature&Humidity Sensor connected to port D5
motionSensor = GroveMiniPIRMotionSensor(5) 
# Grove - Moisture Sensor connected to port A0
moisture_sensor = GroveMoistureSensor(0)
# Grove - 16x2 LCD(White on Blue) connected to I2C port
lcd = JHD1802()
# Grove - Temperature&Humidity Sensor connected to port D22
temp_sensor = DHT('11', 22)
# Grove - LED Button connected to port D16
button = GroveLedButton(16)

def ledbutton():
    button.led.light(True)
    time.sleep(2)
    button.led.light(False)

def roomCondition():
    # Display Humiity and Temperture  
    humi, temp = temp_sensor.read()                             # read temperture and humidity data from sensor
    lcd.setCursor(0, 0)                                   
    lcd.write('Tem:{}C'.format(temp))          # write temperture to lcd
    lcd.setCursor(1, 0)
    lcd.write('Hum:{}%'.format(humi))             # write humididy to lcd

    # Display moisture
    mois = moisture_sensor.moisture
    if 0 <= mois and mois < 300:
        level = 'dry'
    elif 300 <= mois and mois < 600:
        level = 'moist'
    else:
        level = 'wet'
    lcd.setCursor(0, 8)
    lcd.write('Moi:{},{}'.format(mois, level))

def counting():
    global count
    
    count = 0
    value = 1
    while value != 0:
        count += 1
        print('count', count)
        time.sleep(1)
        if count == 10:
            lcd.clear()
            lcd.setCursor(0, 0)
            lcd.write('Total:{}'.format(count))
            # t1 = threading.Thread(target=buzzer)
            t2 = threading.Thread(target=ledbutton)
            # t1.start()
            t2.start()
            time.sleep(4)
            value = 0
            


# funtion for buzzer
class GroveRelay(GPIO):
    def __init__(self, pin):
        super(GroveRelay, self).__init__(pin, GPIO.OUT)
 
    def on(self):
        self.write(1)
 
    def off(self):
        self.write(0)

# Grove - Buzzeer connect to PWM port 12
relay = GroveRelay(12)

def buzzer():
    relay.on()
    time.sleep(1)
    relay.off()
    time.sleep(2)
    relay.on()
    time.sleep(1)
    relay.off()

# threads = []

# for _ in range(10):
#     t1 = threading.Thread(target=buzzer)
#     t1.start()
#     threads.append(t1)

# for thread in threads:
#     thread.join()




def main():
    while True:
        
        roomCondition()
        counting()
        t3 = threading.Thread(target=roomCondition)
        t4 = threading.Thread(target=counting)

        t3.start()
        t4.start()
        t3.join()
        t4.join()
        finish = time.perf_counter()
        print(f'Finished in {round(finish-start, 2)} second(s)')
        time.sleep(1)
 
if __name__ == '__main__':
    main()

# def do_something():
#    print('Sleeping 1 second...')
#     time.sleep(1)
#     print('Done Sleeping...')


# threads = []

# for _ in range(10):
#     t1 = threading.Thread(target=do_something)
#     t1.start()
#     threads.append(t1)

# for thread in threads:
#     thread.join()


# finish = time.perf_counter()

# print(f'Finished in {round(finish-start, 2)} second(s)') 
