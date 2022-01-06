#!/usr/bin/env python

'''
Contain functions to draw Bird Eye View for region of interest(ROI) and draw bounding boxes according to risk factor
for humans in a frame and draw lines between boxes according to risk factor between two humans. 
'''

__title__           = "plot.py"
__Version__         = "1.0"
__copyright__       = "Copyright 2020 , Social Distancing AI"
__license__         = "MIT"
__author__          = "Deepak Birla"
__email__           = "birla.deepak26@gmail.com"
__date__            = "2020/05/29"
__python_version__  = "3.5.2"

# imports
import cv2
import numpy as np

# Function to draw Bird Eye View for region of interest(ROI). Red, Yellow, Green points represents risk to human. 
# Red: High Risk
# Yellow: Low Risk
# Green: No Risk
red = (0, 0, 255)
green = (0, 255, 0)
yellow = (0, 255, 255)
black = (96, 96, 96)
sts_r1 = "Safety, No rule violation!"
sts_r2 = "Safety, No rule violation!"
c_sts_r1 = green
c_sts_r2 = green
rule1 = 0
rule2 = 0
action = 0
update_safe = 0


def bird_eye_view(frame, distances_mat, bottom_points, scale_w, scale_h, risk_count):
    global sts_r1
    global sts_r2
    global c_sts_r1
    global c_sts_r2
    global rule1
    global rule2
    global action
    timer = 0
    h = frame.shape[0]
    w = frame.shape[1]
    global red
    global green
    global yellow
    global black
    global update_safe

    blank_image = np.zeros((int(h * scale_h), int(w * scale_w), 3), np.uint8)
    blank_image[:] = black
    warped_pts = []
    r = []
    g = []
    y = []
    count_r = 0
    count_y = 0
    for i in range(len(distances_mat)):

        if distances_mat[i][2] == 0:
            if (distances_mat[i][0] not in r) and (distances_mat[i][0] not in g) and (distances_mat[i][0] not in y):
                r.append(distances_mat[i][0])
            if (distances_mat[i][1] not in r) and (distances_mat[i][1] not in g) and (distances_mat[i][1] not in y):
                r.append(distances_mat[i][1])

            blank_image = cv2.line(blank_image, (int(distances_mat[i][0][0] * scale_w), int(distances_mat[i][0][1] * scale_h)), (int(distances_mat[i][1][0] * scale_w), int(distances_mat[i][1][1]* scale_h)), red, 2)
            count_r += 1
        #print(count_r)
        if (count_r > 1) and (count_r < 5):
            rule1 = 1  # Rule 1 Violation
            sts_r1 = "Social Distance Detection!!!"
            c_sts_r1 = red
            print("Rule 1: ", sts_r1)
        else:
            sts_r1 = "Safety, No rule violation!"
            c_sts_r1 = green
        if count_r > 5:  # More Than 3 people gathering (above 5 connection) - High Risk
            rule2 = 1  # Rule 2 Violation
            sts_r2 = "Gathering Detection!!!"
            c_sts_r2 = red
            print("Rule 2: ", sts_r2)


    for i in range(len(distances_mat)):
                
        if distances_mat[i][2] == 1:
            if (distances_mat[i][0] not in r) and (distances_mat[i][0] not in g) and (distances_mat[i][0] not in y):
                y.append(distances_mat[i][0])
            if (distances_mat[i][1] not in r) and (distances_mat[i][1] not in g) and (distances_mat[i][1] not in y):
                y.append(distances_mat[i][1])
        
            blank_image = cv2.line(blank_image, (int(distances_mat[i][0][0] * scale_w), int(distances_mat[i][0][1] * scale_h)), (int(distances_mat[i][1][0] * scale_w), int(distances_mat[i][1][1]* scale_h)), yellow, 2)
            count_y += 1
            print("Count yellow: ", count_y)
        if (count_y > 4):  # More Than 3 people gathering (above 5 connection) - Low Risk
            print("Count yellow Warning: ", count_y)
            rule2 = 1  # Rule 2 Violation
            sts_r2 = "Warning - Gathering Detection!!!"
            c_sts_r2 = yellow
            update_safe = 0
            print("Rule 2: ", sts_r2)
        else:
            sts_r2 = sts_r2
            c_sts_r2 = c_sts_r2

    for i in range(len(distances_mat)):
        
        if distances_mat[i][2] == 2:
            if (distances_mat[i][0] not in r) and (distances_mat[i][0] not in g) and (distances_mat[i][0] not in y):
                g.append(distances_mat[i][0])
            if (distances_mat[i][1] not in r) and (distances_mat[i][1] not in g) and (distances_mat[i][1] not in y):
                g.append(distances_mat[i][1])
    
    for i in bottom_points:
        blank_image = cv2.circle(blank_image, (int(i[0]  * scale_w), int(i[1] * scale_h)), 5, green, 10)
        if len(list(bottom_points)) == 1:  # Only 1 green points
            update_safe = 1
        else:
            update_safe = 0

    for i in y:
        blank_image = cv2.circle(blank_image, (int(i[0]  * scale_w), int(i[1] * scale_h)), 5, yellow, 10)
    for i in r:
        blank_image = cv2.circle(blank_image, (int(i[0]  * scale_w), int(i[1] * scale_h)), 5, red, 10)
        
    pad = np.full((140,blank_image.shape[1],3), [32, 32, 32], dtype=np.uint8)
    cv2.putText(pad, "Bird-eye View", (40, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    #cv2.putText(pad, "-- LOW RISK : " + str(risk_count[1]) + " people", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)
    #cv2.putText(pad, "-- SAFE : " + str(risk_count[2]) + " people", (50,  80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
    blank_image = np.vstack((blank_image,pad))
    if (rule1 or rule2) == 1:
        timer += 1
        if timer == 60:  # Count 60 cycles for rules 1 & 2 violation
            action = 1  # If timer = 60 -> action 1
            print("Take Action: " ,action)
        else:
            action = 0
    return blank_image
    
# Function to draw bounding boxes according to risk factor for humans in a frame and draw lines between
# boxes according to risk factor between two humans.
# Red: High Risk
# Yellow: Low Risk
# Green: No Risk 
def social_distancing_view(frame, distances_mat, boxes, risk_count):
    global sts_r1
    global sts_r2
    global c_sts_r1
    global c_sts_r2
    global red
    global green
    global yellow
    global black
    global update_safe
    red = (0, 0, 255)
    green = (0, 255, 0)
    yellow = (0, 255, 255)
    
    for i in range(len(boxes)):

        x,y,w,h = boxes[i][:]
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),green,2)
                           
    for i in range(len(distances_mat)):

        per1 = distances_mat[i][0]
        per2 = distances_mat[i][1]
        closeness = distances_mat[i][2]
        
        if closeness == 1:
            x,y,w,h = per1[:]
            frame = cv2.rectangle(frame,(x,y),(x+w,y+h),yellow,2)
                
            x1,y1,w1,h1 = per2[:]
            frame = cv2.rectangle(frame,(x1,y1),(x1+w1,y1+h1),yellow,2)
                
            frame = cv2.line(frame, (int(x+w/2), int(y+h/2)), (int(x1+w1/2), int(y1+h1/2)),yellow, 2) 
            
    for i in range(len(distances_mat)):

        per1 = distances_mat[i][0]
        per2 = distances_mat[i][1]
        closeness = distances_mat[i][2]

        if closeness == 0:
            x,y,w,h = per1[:]
            frame = cv2.rectangle(frame,(x,y),(x+w,y+h),red,2)
                
            x1,y1,w1,h1 = per2[:]
            frame = cv2.rectangle(frame,(x1,y1),(x1+w1,y1+h1),red,2)
                
            frame = cv2.line(frame, (int(x+w/2), int(y+h/2)), (int(x1+w1/2), int(y1+h1/2)),red, 2)

    location = 360
    start_location = 35

    pad = np.full((140,frame.shape[1],3), [0, 0, 0], dtype=np.uint8)
    if update_safe == 1:
        sts_r1 = "Safety, No rule violation!"
        sts_r2 = "Safety, No rule violation!"
        c_sts = green
        cv2.putText(pad, "ROOM ANALYSIS:", (15, 40),cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 3)
        cv2.putText(pad, "- HIGH RISK : " + str(risk_count[0]) + " people", (location, start_location), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 1)
        cv2.putText(pad, "- LOW RISK : " + str(risk_count[1]) + " people", (location, start_location + 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 1)
        cv2.putText(pad, "- SAFE : " + "1" + " people", (location,  start_location + 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 1)
        cv2.putText(pad, "Rule 1: " + str(sts_r1), (15,70), cv2.FONT_HERSHEY_SIMPLEX, 0.6, c_sts_r1, 2)
        cv2.putText(pad, "Rule 2: " + str(sts_r2), (15, 95), cv2.FONT_HERSHEY_SIMPLEX, 0.6, c_sts_r2, 2)
        frame = np.vstack((frame, pad))
        update_safe = 0
        print("Rule 1: ", sts_r1)
        print("Rule 2: ", sts_r2)
    else:
        cv2.putText(pad, "ROOM ANALYSIS:", (15, 40),cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 3)
        cv2.putText(pad, "- HIGH RISK : " + str(risk_count[0]) + " people", (location, start_location), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 1)
        cv2.putText(pad, "- LOW RISK : " + str(risk_count[1]) + " people", (location, start_location + 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 1)
        cv2.putText(pad, "- SAFE : " + str(risk_count[2]) + " people", (location, start_location + 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 1)
        if(str(risk_count[0]) == "0"):
            sts_r1 = "Safety, No rule violation!"
            sts_r2 = "Safety, No rule violation!"
            c_sts_r1 = green
            c_sts_r2 = green
            print("Rule 1: ", sts_r1)
            print("Rule 2: ", sts_r2)

        cv2.putText(pad, "Rule 1: " + str(sts_r1), (15,70), cv2.FONT_HERSHEY_SIMPLEX, 0.6, c_sts_r1, 2)
        cv2.putText(pad, "Rule 2: " + str(sts_r2), (15, 95), cv2.FONT_HERSHEY_SIMPLEX, 0.6, c_sts_r2, 2)
        frame = np.vstack((frame, pad))
            
    return frame

