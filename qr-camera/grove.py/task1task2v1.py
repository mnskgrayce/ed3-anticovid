#!/usr/bin/env python3
 
import time
from datetime import datetime
from seeed_dht import DHT
from grove.display.jhd1802 import JHD1802
from grove.grove_mini_pir_motion_sensor import GroveMiniPIRMotionSensor
#QR import
import cv2
import numpy as np
from pyzbar.pyzbar import decode
import time
from gtts import gTTS
import os
import requests

# Grove - Temperature&Humidity Sensor connected to port D5
motionSensor = GroveMiniPIRMotionSensor(5) 
# Grove - 16x2 LCD(White on Blue) connected to I2C port
lcd = JHD1802()
# Grove - Temperature&Humidity Sensor connected to port D5
sensor = DHT('11', 22)
People = 0
checkMotion = 0
pTime = 0
enter = 0
exit1 = 0
count = 0
valid = 2 #nueuture value
STEP_TIME = 150
language ="en"
dataFile_path = r"/home/pi/Documents/Hardware/grove.py/myDataFile.txt"
with open(dataFile_path, "r") as f:  # Open and read file
    myDataList = f.read().splitlines()  # Create the info array
# Function:
def check_in_list(name):
    file_path = r"/home/pi/Documents/Hardware/grove.py/check_in_list.txt"
    with open(file_path, "a") as f:  # Open and read file
        f.write(name+"\n")

def roomCondition():

    # Display Humiity and Temperture  
    humi, temp = sensor.read()
    lcd.setCursor(0, 0)
    lcd.write('temperature: {0:2}C'.format(temp))
    lcd.setCursor(1, 0)
    lcd.write('huminity: {0:5}%'.format(humi))
    # time.sleep(5)

    # Display date and time
    now = datetime.now()
    date = now.strftime("%d/%m/%Y")
    timenow = now.strftime("%H:%M:%S")
    lcd.setCursor(0, 0)
    lcd.write('date: {0:2}C'.format(date))
    lcd.setCursor(1, 0)
    lcd.write('time: {0:15}%'.format(timenow))
    # time.sleep(5)
    return humi, temp
def QRcheck():
    global pTime
    global enter
    global exit1
    global count
    global valid                # 0 = invalid, 1 = valid using for authorized and unauthorized
    valid = 2 # reset for next loop
    url = 'http://192.168.0.110:8000/motion/1'
    stsQRcam = 1     # QR cam status
    cap = cv2.VideoCapture(0)  # Camera Streaming
    while stsQRcam and count != STEP_TIME: #frequency 10Hz 0.1s for 1 count

        #success0, img0 = cap0.read()  # Capture image
        success, img = cap.read() # Capture image
        # Frame rate
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, f'FPS: {int(fps)}', (10, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

        for barcode in decode(img):  # Scan Barcode
            myData = barcode.data.decode('utf-8')
            currentTime = time.ctime()

            if myData in myDataList:  # Check on the list or not
                myOutput = 'Authorized'
                valid = 1
                myColor = (0, 255, 0)  # Green
                # Voice the welcome message
                myData = myData[0:(len(myData)-9)]  # Filter out the student ID for welcome message
                check_in_data = currentTime + '\tAuthorized\t\t' + myData
                check_in_list(check_in_data)
                stsQRcam = 0              
                if total < 5:
                    enter = enter + 1 
                else:
                    print('Room Full')
                    enter = enter
                print(check_in_data)
                # Drawing bonding box for the scanned QR code
                pts = np.array([barcode.polygon], np.int32)
                pts = pts.reshape((-1, 1, 2))
                cv2.polylines(img, [pts], True, myColor, 5)
                pts2 = barcode.rect
                # Voice message
                wel_mess = myData + " has entered the room!"
                # output_voice = gTTS(text=wel_mess, lang=language, slow=True)
                # output_voice.save("Welcome.mp3")
                # time.sleep(2)
                # os.system("start Welcome.mp3")
                # time.sleep(5)

            else:
                myOutput = 'Un-Authorized'
                valid = 0
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
        count += 1
        if count == STEP_TIME:
            print('dem')
            if valid == 0:
                exit1 = exit1
            if valid == 2:
                print('exit')
                exit1 += 1
                if total == 0:
                    exit1 = 0
        print("valid", valid)
        total = enter - exit1
        mydict = {
        'id':1,
        'total': total
        }
        
        response = requests.put(url, data = mydict)
        print('total =', total)
        print('enter =', enter)
        print('exit =', exit1)
        print('count =', count)
        
def on_detect():
    global count
    now = datetime.now()
    timenow = now.strftime("%H:%M:%S")
    print('Motion detected')
    QRcheck()
    count = 0
    
    # global People
    # global checkMotion
    # print("time ", timenow)
    # People += 1
    # print('People = {}'.format(People))

def main():
    global People
    global total
    url = 'http://192.168.0.110:8000/temp_sensor/1'    
    while True:
        humi, temp = roomCondition()
        print('start')
        motionSensor.on_detect = on_detect
        mydict = {
        'id':1,
        'temperature': temp,
        'humidity': humi
        }
        print('value: ', mydict)
        response = requests.put(url, data = mydict)
        # response = requests.put(url, data = mydict)
        # print(response)
        time.sleep(1)
 
if __name__ == '__main__':
    main()

# sudo chmod +x lesson_7.py
# sudo ./lesson_7.py
