#!/usr/bin/env python3

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
from grove.grove_relay import GroveRelay
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
# Opencv QR import libarry
import cv2
import numpy as np
from pyzbar.pyzbar import decode
from gtts import gTTS
import os
#import libaary for local host
import requests
import socketio
import base64


sio = socketio.Client()
@sio.event
def connect():
    print("I'm connected!")
@sio.event
def connect_error():
    print("The connection failed!")
@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://192.168.0.100:4000/')


# funtion for buzzer
class GroveRelay(GPIO):
    def __init__(self, pin):
        super(GroveRelay, self).__init__(pin, GPIO.OUT)
 
    def on(self):
        self.write(1)
 
    def off(self):
        self.write(0)

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
# Grove - Buzzeer connect to PWM port 12
relay = GroveRelay(12)
# Grove - Ultrasonic Ranger connected to port D18
distance = GroveUltrasonicRanger(18)

# initialize value
pTime = 0                                                  # varialbe for fps display
enter = 0                                                  # variable for counting enter the room
exit1 = 0                                                  # variable for counting exit the room
total = 0
count = 0                                                  # variable for counting time to scan QR
valid = 2                                                  # nueuture value
STEP_TIME = 150                                            # Limit time for scaning QR
language ="en"  
dataFile_path = r"/home/pi/Documents/Hardware/grove.py/myDataFile.txt"  # storing data check in
with open(dataFile_path, "r") as f:                        # Open and read file
    myDataList = f.read().splitlines()                     # Create the info array

# Function for checking people in list:
def check_in_list(name):
    file_path = r"/home/pi/Documents/Hardware/grove.py/check_in_list.txt" # people are allowed
    with open(file_path, "a") as f:                        # Open and read file
        f.write(name+"\n")

# Funtion for getting room condition
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

    # # Display date and time
    # now = datetime.now()                                   # read date and time from pi
    # date = now.strftime("%d/%m/%Y")
    # timenow = now.strftime("%H:%M:%S")
    # lcd.setCursor(0, 0)
    # lcd.write('date: {0:2}C'.format(date))
    # lcd.setCursor(1, 0)
    # lcd.write('time: {0:15}%'.format(timenow))
    return humi, temp, mois, level

# Funtion for scaning QR
def QRcheck():
    # Set global for variable
    global pTime                                           # varialbe for fps display
    global enter                                           # variable for counting enter the room
    global exit1                                           # variable for counting exit the room
    global count                                           # variable for counting time to scan QR
    global total
    global enter
    url = 'http://192.168.0.100:8000/motion/1'             # API
    stsQRcam = 1                                           # QR cam status 1 = on, 0 = off
    cap = cv2.VideoCapture(0)                              # Camera Streaming
    while stsQRcam and count != STEP_TIME:                 # Frequency 10Hz, 0.1s for 1 count
        #success0, img0 = cap0.read()  # Capture image

        # Send img by socket
        success, img1 = cap.read()                         # Capture real image from camera
        res, frame = cv2.imencode('.jpg', img1,[cv2.IMWRITE_JPEG_QUALITY,80]) # from image to binary buffer
        data = base64.b64encode(frame) # convert to base64 format
        sio.emit('video', data) # send to server

        img = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)       # Convert the real imatge to the grayscale fo easy to scan
        # Frame rate
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, f'FPS: {int(fps)}', (10, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

        for barcode in decode(img):                        # Scan Barcode
            myData = barcode.data.decode('utf-8')
            currentTime = time.ctime()

            if myData in myDataList:                       # Check on the list or not
                myOutput = 'Authorized'
                myColor = (0, 255, 0)                      # Green
                # Voice the welcome message
                myData = myData[0:(len(myData)-9)]         # Filter out the student ID for welcome message
                check_in_data = currentTime + '\tAuthorized\t\t' + myData
                check_in_list(check_in_data)
                stsQRcam = 0              
                if total < 5:                              # Check people in room less than 5
                    enter = enter + 1
                    relay.on()
                    time.sleep(0.5)
                    relay.off()                             # sua sua nha nha
                else:   
                    print('Room Full')
                    enter = enter
                    button.led.light(True)
                print(check_in_data)
                # Drawing bonding box for the scanned QR code
                pts = np.array([barcode.polygon], np.int32)
                pts = pts.reshape((-1, 1, 2))
                cv2.polylines(img, [pts], True, myColor, 5)
                pts2 = barcode.rect
                # Voice message
                wel_mess = myData + " has entered the room!"
            else:
                myOutput = 'Un-Authorized'
                myColor = (0, 0, 255)  # Red
                # Drawing bonding box for the scanned QR code
                pts = np.array([barcode.polygon], np.int32)
                pts = pts.reshape((-1, 1, 2))
                cv2.polylines(img, [pts], True, myColor, 5)
                pts2 = barcode.rect
                stsQRcam = 1
                check_in_data = currentTime + '\tUn-Authorized\t' + myData
                check_in_list(check_in_data)
                print(check_in_data)       
        count += 1                                          # counting for set time QR check 
        total = enter - exit1                              # total people in room
        lcd.setCursor(1, 8)
        lcd.write('room:{}'.format(total))
        # format total people in room for json 
        mydict = {
        'id':1,
        'total_people': total,
        'people_in': enter,
        'people_out': exit1
        }
        response = requests.put(url, data = mydict)      
        print('Number of people in room: ', total)
        print('People in: ', enter)
        print('People out: ', exit1)
        print('count: ', count)
        # print('QR_data', img)


# Function for Distance dectect
def measure():
    distance_detect = distance.get_distance()
    print('{} cm'.format(distance_detect))
    return distance_detect
# Funtion for motion sensor dectected
def on_detect():
    global count1 
    count1 = 0
    global value                                          # global variable
    global count
    global exit1
    global total
    global enter
    url = 'http://192.168.0.100:8000/motion/1'             # API
    value = 1
    print('Motion detected')                               # print out whenever motion detected
    button.led.light(False)                                # turn off led
    while value != 0:
        distance_detect = measure()
        time.sleep(0.5)
        if distance_detect < 50:
            QRcheck()
            value = 0
        else:
            count1 += 1
            print('count1', count1)
            if count1 == 30:
                count1 = 0
                if total == 0:
                    exit1 = exit1
                else:
                    exit1 += 1
                value = 0
                print('exit', exit1)
            # format total people in room for json 
    mydict = {
    'id':1,
    'total_people': total,
    'people_in': enter,
    'people_out': exit1
    }
    response = requests.put(url, data = mydict)
        # print('QR_data', img)
    #QRcheck()                                              # jump to QR check funtion
    count = 0                                              # Set time count back 0 for next loop

# main fruntion
def main():
    url = 'http://192.168.0.100:8000/temp_sensor/1'        # API
    while True:
        humi, temp, mois, level = roomCondition()          # Get value of humidity and temperter from room condition funtion
        motionSensor.on_detect = on_detect                 # Motion detected
        # Format for room condition on json
        mydict = {
        'id':1,
        'temperature': temp,
        'humidity': humi,
        'moisture': mois,
        'level_moisture': level
        }
        response = requests.put(url, data = mydict)
        time.sleep(1)
 
if __name__ == '__main__':
    main()