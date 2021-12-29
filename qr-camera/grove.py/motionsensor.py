import RPi.GPIO as GPIO1
import time
GPIO1.setwarnings(False)
GPIO1.setmode(GPIO1.BCM)
GPIO1.setup(17, GPIO1.IN)         #Read output from PIR motion sensor
GPIO1.setup(3, GPIO1.OUT)         #LED output pin
while True:
    i=GPIO1.input(17)
    if i==0:                 #When output from motion sensor is LOW
        print ("No intruders",i)
        GPIO1.output(3, 0)  #Turn OFF LED
        time.sleep(0.1)
    elif i==1:               #When output from motion sensor is HIGH
        print ("Intruder detected",i)
        GPIO1.output(3, 1)  #Turn ON LED
        time.sleep(0.1)
 