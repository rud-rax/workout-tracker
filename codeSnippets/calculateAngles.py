
import numpy as np

def calculateAngles2(landmarks , landmarklist : list) :

    a = landmarks[landmarklist[0]]
    b = landmarks[landmarklist[1]]
    c = landmarks[landmarklist[2]]


    return calculateAngles(a,b,c)

def calculateAngles(a,b,c) :


    a = np.array(a) # First
    b = np.array(b) # Mid
    c = np.array(c) # End
    
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
    
    if angle >180.0:
        angle = 360-angle
        
    return angle 