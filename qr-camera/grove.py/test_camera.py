# import the opencv library
import cv2
# libarry for grove sensor
import threading
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
import numpy as np
from pyzbar.pyzbar import decode
from gtts import gTTS
import os
#import libaary for local host
import requests
import socketio
import base64
  
# define a video capture object
vid = cv2.VideoCapture(0)
  
while(True):
    start = time.perf_counter()
    # Capture the video frame
    # by frame
    ret, img1 = vid.read()
    img = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
  
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
            print(check_in_data)
            # Drawing bonding box for the scanned QR code
            pts = np.array([barcode.polygon], np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(img, [pts], True, myColor, 5)
            pts2 = barcode.rect
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
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    finish = time.perf_counter()
    print(f'Finished in {round(finish-start,2)} second(s)')
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()