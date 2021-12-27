import socketio
import cv2
import base64
import time
import json

# constant variable 
ALARM_SOCIAL_DISTANCE = "alarm_distance"
SAFE_SOCIAL_DISTANCE = "safe_distance"

ALARM_PEOPLE_GATHERING = "alarm_gathering"
SAFE_PEOPLE_GATHERING = "safe_gathering"

sio = socketio.Client()
pTime = 0 

def read_json():
    f = open('package.json') # Opening JSON file
    data = json.load(f) # returns JSON object as a dictionary
    url = data['config']['myUrl'] # list
    f.close() # Closing file
    return url 

url = read_json()

@sio.event
def connect():
    print("I'm connected!")

@sio.event
def connect_error():
    print("The connection failed!")

@sio.event
def disconnect():
    print('disconnected from server')
try:
    sio.connect(url+':5000/')
except:
  print("Server error connection")

# define a video capture object
vid = cv2.VideoCapture(0)
while(True):
    cTime = time.time()
    fps = round(1 / (cTime - pTime))
    pTime = cTime

    x  =  1
    ret, img = vid.read()                     # get frame from webcam
    res, frame = cv2.imencode('.jpg', img,[cv2.IMWRITE_JPEG_QUALITY,80])    # from image to binary buffer
    data = base64.b64encode(frame)              # convert to base64 format

    # Video 
    sio.emit('videoVision', data)                      # send to server
    sio.emit('fpsMain', fps)                      # send to server

    # info social distance 
    social_distance = ALARM_SOCIAL_DISTANCE
    sio.emit('socialDistance', social_distance)
    
    # info people gathering 
    people_gathering  = ALARM_PEOPLE_GATHERING
    sio.emit('peopleGathering', people_gathering)

    