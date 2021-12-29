#!/usr/bin/env python3

# libarry for grove sensor
import threading                                                            # threading library
import time
import RPi.GPIO as GPIO1
from datetime import datetime
from seeed_dht import DHT                                                   # Temperature and humidity sensor library
# from grove.display.jhd1802 import JHD1802
from mraa import getGpioLookup
from grove.grove_mini_pir_motion_sensor import GroveMiniPIRMotionSensor     # Motion sensor library
from grove.grove_moisture_sensor import GroveMoistureSensor                 # Moisture sensor library
from grove.gpio import GPIO
import sys
from grove.button import Button
from grove.grove_ryb_led_button import GroveLedButton                       # LED button library
from grove.grove_relay import GroveRelay                                    # Relay library
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger             # Ultrasonic sensor library
# Opencv QR import libarry
import cv2                                                                  # OpenCV
import numpy as np
from pyzbar.pyzbar import decode                                            # QR scan
from gtts import gTTS
import os
#import libaary for local host
import requests
import socketio
import base64

GPIO1.setwarnings(False)
GPIO1.setmode(GPIO1.BCM)
GPIO1.setup(17, GPIO1.IN)         #Read output from PIR motion sensor

# Socket io 
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
sio.connect('http://192.168.50.46:4000/')                                   # Connect through Pi IP port 4000

# Function detecton on
def on_motion():
    i=GPIO1.input(17)
    if i==0:                 #When output from motion sensor is LOW
        print ("No intruders",i)
        time.sleep(0.1)
    elif i==1:               #When output from motion sensor is HIGH
        print ("Intruder detected",i)
        on_detect()
        time.sleep(0.1)
# Funtion for PWM of relay used for buzzer
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
# lcd = JHD1802()
# Grove - Temperature&Humidity Sensor connected to port D22
temp_sensor = DHT('11', 22)
# Grove - LED Button connected to port D16
button = GroveLedButton(16)
# Grove - Buzzer connect to PWM port 12
buzzer = GroveRelay(12)
# Grove - Ultrasonic Ranger connected to port D18
distance = GroveUltrasonicRanger(18)

# initialize value
lcd_state = 0                                                               # variable for display lcd state
time_motion = 0                                                             # variable for count on motion
pTime = 0                                                                   # varialbe for fps display
entering = 0                                                                # variable for counting enter the room
exiting = 0                                                                 # variable for counting exit the room
total = 0                                                                   # variable for total people in room
count_QR = 0                                                                # variable for counting time to scan QR
humi = 0                                                                    # variable for room condition
temp = 0
mois = 0
fps = 0
pre_distance = 0
current_distance = 0                                                                     # variable for fps QR camera
distant_count = 0                                                           # couting for stable ultrasonic
system_state = 0                                                            # initialize system state
button.led.light(False)                                                     # initialize for button led
myData = None

# Constant variable
TIME_QR = 150                                                              # Limit time for scaning QR
DISTANCE = 50                                                              # limit distance for ultrasonic measure
TIME_MOTION = 50                                                           # Limit time for motion

language ="en"  
dataFile_path = r"/home/pi/Documents/Hardware/grove.py/myDataFile.txt"     # storing data check in
with open(dataFile_path, "r") as f:                                        # Open and read file
    myDataList = f.read().splitlines()                                     # Create the info array

# Function for checking people in list:
def check_in_list(name):
    file_path = r"/home/pi/Documents/Hardware/grove.py/check_in_list.txt"  # people are allowed
    with open(file_path, "a") as f:                                        # Open and read file
        f.write(name+"\n")

# Funtion for buzzer QR valid, buzzing 2 times
def buzzer_valid():
    buzzer.on()
    time.sleep(0.3)
    buzzer.off()
    time.sleep(0.5)
    buzzer.on()
    time.sleep(0.3)
    buzzer.off()

# Function for buzzer room full reject QR, buzzer 3 times
def buzzer_reject():
    buzzer.on()
    time.sleep(0.3)
    buzzer.off()
    time.sleep(0.2)
    buzzer.on()
    time.sleep(0.3)
    buzzer.off()
    time.sleep(0.2)
    buzzer.on()
    time.sleep(0.3)
    buzzer.off()

# Funtion for buzzer indicating timeout, buzzer 1 time
def buzzer_timeout():
    buzzer.on()
    time.sleep(1)
    buzzer.off()
    
# Funtion for reading temperature and humidity
def roomCondition():
    global humi
    global temp
    global mois  
    humi, temp = temp_sensor.read()                                        # read temperture and humidity data from sensor
    mois = moisture_sensor.moisture
    time.sleep(1)

# Funtion for blinking led in invalid scan
def led_blink():
    button.led.light(True)
    time.sleep(0.5)
    button.led.light(False)
    time.sleep(0.5)
    button.led.light(True)
    time.sleep(0.5)
    button.led.light(False)

# Funtion for getting room condition
# def LCD_roomCondition():
#     global system_state                                                    # In/Out checking state
#     global humi
#     global temp
#     global mois
#     global total
#     global exiting
#     global entering
#     global fps
#     global lcd_state
#     if lcd_state == 0:                                                  # Room condition state
#         lcd.clear()
#         # write temp and humi to lcd
#         lcd.setCursor(0, 0)                                   
#         lcd.write('Tem:{}C'.format(temp))                                  # Write temperture to lcd
#         lcd.setCursor(1, 0)
#         lcd.write('Hum:{}%'.format(humi))                                  # Write humididy to lcd
#         lcd.setCursor(0, 8)
#         lcd.write('Moi:{}%'.format(mois))                                  # Write moisture to lcd      
#         lcd.setCursor(1, 8)                                                # Write total people in room
#         lcd.write('total:{}'.format(total))
#     elif lcd_state == 1:                                                # QR valid scan state
#         lcd.clear()
#         lcd.setCursor(0, 0)                                   
#         lcd.write('QR scan valid')
#         lcd.setCursor(1, 0)                                   
#         lcd.write('Enter the Room')
#         time.sleep(5)
#         lcd_state = 0
#         system_state = 0
#     elif lcd_state == 2:                                                # Room full state
#         lcd.clear()
#         lcd.setCursor(0, 0)                                   
#         lcd.write('room is full')
#         lcd.setCursor(1, 0)                                   
#         lcd.write('Enter rejected')
#         time.sleep(5)
#         lcd_state = 0
#     elif lcd_state == 3:                                                # QR invalid scan state
#         lcd.clear()
#         lcd.setCursor(0, 0)                                   
#         lcd.write('QR scan invalid')
#         lcd.setCursor(1, 0)                                   
#         lcd.write('Enter rejected')
#         time.sleep(5)
#         if lcd_state == 1:
#             lcd_state = 1
#         else:
#             lcd_state = 0
#     elif lcd_state == 4:                                                # Exit state
#         lcd.clear()
#         lcd.setCursor(0, 0)                                   
#         lcd.write('Exit the room')
#         time.sleep(5)
#         lcd_state = 0
#         system_state = 0 
#     elif lcd_state == 5:                                                # No QR scan state
#         lcd.clear()
#         lcd.setCursor(0, 0)                                   
#         lcd.write('No QR scan')
#         time.sleep(5)
#         lcd_state = 0

    # Sending data to UI through Socket IO
    sio.emit('sensor', {'temperature':temp, 'humidity':humi,'moisture':mois})  
    sio.emit('motion', {'total_people':total,  'people_in':entering, 'people_out':exiting})
    sio.emit('checkout',system_state)
    
# Function for notify room is full
def roomfull_on():
    # Notify room full by turning on off LED
    if total == 5:                                                         # If room full, red LED on, else off
        button.led.light(True)
    if total < 5:
        button.led.light(False)

# Funtion for socket io
def threadingforQR(img):
    res, frame = cv2.imencode('.jpg', img,[cv2.IMWRITE_JPEG_QUALITY,80])   # from image to binary buffer
    data = base64.b64encode(frame)                                         # convert to base64 format
    sio.emit('video', data)                                                # send to server

# Funtion for scaning QR
def QRcheck():
    # Set global variable
    global pTime                                                           # varialbe for fps display
    global entering                                                        # variable for counting enter the room
    global exiting                                                         # variable for counting exit the room
    global count_QR                                                        # variable for counting time to scan QR
    global total                                                           # variable for total people in rooom
    global entering                                                        # variable for counting enter the room
    global system_state
    global myData
    global fps
    global lcd_state
    
    stsQRcam = 1                                                           # QR cam status 1 = on, 0 = off
    cap = cv2.VideoCapture(0)                                              # Camera Streaming
    while stsQRcam and count_QR != TIME_QR:                                # Frequency 10Hz, 0.1s for 1 count  
        # Send img by socket
        success, img1 = cap.read()                                         # Capture real image from camera
        res, frame = cv2.imencode('.jpg', img1,[cv2.IMWRITE_JPEG_QUALITY,80]) # from image to binary buffer
        data = base64.b64encode(frame)                                     # convert to base64 format
        sio.emit('video', data)                                            # send to server
        img = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)                       # Convert the real imatge to the grayscale fo easy to scan

        # Frame rate
        cTime = time.time()
        fps = round(1 / (cTime - pTime))
        pTime = cTime

        # Checking QR in check list
        for barcode in decode(img):                                        # Scan Barcode
            myData = barcode.data.decode('utf-8')
            currentTime = time.ctime()
            if myData in myDataList:                                       # Check on the list or not
                myOutput = 'Authorized'
                myColor = (0, 255, 0)                                      # Green
                # Voice the welcome message
                myData = myData[0:(len(myData)-9)]                         # Filter out the student ID for welcome message
                check_in_data = currentTime + '\tAuthorized\t\t' + myData
                check_in_list(check_in_data)
                stsQRcam = 0              
                if total < 5:                                              # Check people in room less than 5
                    entering = entering + 1
                    t1 = threading.Thread(target=buzzer_valid)                # buzzer on
                    t1.start()                           
                    system_state = 1
                    lcd_state = 1
                else:                                                      # If there are 5 people in room already
                    t1 = threading.Thread(target=buzzer_reject)            # buzzer on
                    t1.start()  
                    entering = entering
                    system_state = 2
                    lcd_state = 2
                print(check_in_data)
                # Drawing bonding box for the scanned QR code
                pts = np.array([barcode.polygon], np.int32)
                pts = pts.reshape((-1, 1, 2))
                cv2.polylines(img, [pts], True, myColor, 5)
                pts2 = barcode.rect
            else:
                myOutput = 'Un-Authorized'
                myColor = (0, 0, 255)                                      # Red
                # Drawing bonding box for the scanned QR code
                pts = np.array([barcode.polygon], np.int32)
                pts = pts.reshape((-1, 1, 2))
                cv2.polylines(img, [pts], True, myColor, 5)
                pts2 = barcode.rect
                stsQRcam = 1
                check_in_data = currentTime + '\tUn-Authorized\t' + myData
                check_in_list(check_in_data)
                print(check_in_data)
                t2 = threading.Thread(target=led_blink)
                t2.start()
                system_state = 3
                lcd_state = 3
        count_QR += 1                                                       # counting for set time QR check 
        total = entering - exiting                                          # total people in room
        sio.emit('checkout',system_state)
        sio.emit('fps_qr', fps)                                             # Send fps to UI
        # print('Number of people in room: ', total)
        # print('People in: ', entering)
        # print('People out: ', exiting)
        # print('count: ', count_QR)
    # In case there is not any scan QR 
    if myData == None:
        system_state = 5
        lcd_state = 5
    myData = None

    if count_QR == TIME_QR:                                                 # If QR scan times out, buzzer on for 1s 
        t3 = threading.Thread(target=buzzer_timeout)
        t3.start()

# Function for Distance dectect
def measure():
    distance_detect = distance.get_distance()
    print('{} cm'.format(distance_detect))
    return distance_detect
# Funtion for motion sensor dectected
def on_detect():
    global time_motion 
    global flag                                                             # global variable
    global count_QR
    global exiting
    global total
    global entering
    global system_state
    global distant_count                                                    
    global lcd_state
    global current_distance
    global pre_distance
    if system_state == 3:                                                   # Invalid
        system_state = 0
        print('Invalidout')
    elif system_state == 2:                                                 # Room full
        system_state = 0
        print('Room full')
    elif system_state == 5:                                                 # No scan
        system_state = 0
        print('No scan')    
    elif system_state == 0 or system_state == 1 or system_state == 4:
        flag = 1
        system_state = 0
        sio.emit('checkout',system_state)
        print('Motion detected')                                            # print out whenever motion detected
        # turn on Ultra sonic sensor
        while flag != 0:
            distance_detect = measure()
            if current_distance == 1:
                pre_distance += current_distance
            elif current_distance == 0:
                pre_distance = 0
            print('pre_distance', pre_distance)
            # print('cur_distance', current_distance)
            time.sleep(0.2)
            if distance_detect < DISTANCE:                                 # if people in range -> run QR scan
                current_distance = 1
                distant_count += 1
                if pre_distance == 4:
                    distant_count = 0
                    pre_distance = 0
                    QRcheck()
                    flag = 0
            else:
                current_distance = 0                                                           # in case people exit the room
                time_motion += 1                                            # counting time for open ultra sonic
                if time_motion == TIME_MOTION:                              # Time limit for run ultra sonic
                    time_motion = 0
                    if total == 0:
                        exiting = exiting
                    else:
                        exiting += 1
                        system_state = 4  
                        lcd_state = 4
                    flag = 0
        total = entering - exiting                                          # total people in room
        roomfull_on()
        sio.emit('motion', {'total_people':total,  'people_in':entering, 'people_out':exiting})  # Send data inside room to UI
        sio.emit('checkout',system_state)
        count_QR = 0                                                        # Set time count back 0 for next loop

# Function detection on motion
# def motion_on():
#     motionSensor.on_detect = on_detect 
# main function
def main():    
    while True:
        on_motion()
        # roomCondition()
        # t4 = threading.Thread(target=LCD_roomCondition)
        # t4.start()
        # on_motion()
        # print('1')
        # t5 = threading.Thread(target=motion_on)
        # t5.start()                                                           # Motion on
 
if __name__ == '__main__':
    main() 