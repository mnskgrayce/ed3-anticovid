'''
	Motion detection using PIR on raspberry Pi
	http://www.electronicwings.com
'''
import RPi.GPIO as GPIO

PIR_input = 29				#read PIR Output
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)		#choose pin no. system
GPIO.setup(PIR_input, GPIO.IN)	


while True:
#when motion detected turn on LED
    if(GPIO.input(PIR_input)):
        print('no motion')
    else:
        print('motion')