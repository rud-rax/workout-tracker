import sys
import os

from exercise import *

# from landmarkInfo import *

class ArmStretch(Exercise) :
    def __init__(self) -> None:

        Exercise.__init__(self)
        
        self.name = "Arm Stretch"

        print(self.name)

        self.connections = {
            (14,12),
            (14,16)
        }

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
    # print(os.listdir(sys.path[0]+"/.."))
    # exe = Exercise()
    # exe.evaluate()
    

    exe = ArmStretch()
    print(exe.landmarkInfo)