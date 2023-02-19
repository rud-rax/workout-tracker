import sys
import os
from landmarkInfo import *

sys.path.insert(1,sys.path[0]+r"/..")

class ArmStretch :
    def __init__(self) -> None:
        self.name = "Arm Stretch"

        self.connections = {
            (14,12),
            (14,16)
        }

        self.landmarkInfo = LandmarkInfo()

        self.params = {
            'counter' : 0,
            'arm_state' : 0,
            'arm_angle' : 0
        }

    def evaluate(self) : 

        self.params['arm_angle'] = self.landmarkInfo.calculateAngle(12,14,16)

        print(self.params['arm_state'] , self.params['counter'] , self.params['arm_angle'])

        if self.params['arm_angle'] > 160 :
            self.params['arm_state'] = 0

        if self.params['arm_angle'] < 50 and self.params['arm_state'] == 0 :
            self.params['arm_state'] = 1
            self.params['counter'] += 1
            # print(self.params['counter'])

        if self.params['counter'] == 10 :
            return True
        return False      


if __name__ == "__main__" :
    print(os.listdir(sys.path[0]+"/.."))
    