import sys
import os

from exercise import *

# from landmarkInfo import *

class legStretch(Exercise) :
    def __init__(self) -> None:

        Exercise.__init__(self)
         
        self.name = "leg Stretch"

        print(self.name)
        self.connections = {
            (24,26),
            (26,28)
        }
        self.params = {
            'counter' : 0,
            'leg_state' : 0,
            'leg_angle' : 0
        }
    def evaluate(self) : 

        self.params['leg_angle'] = self.landmarkInfo.calculateAngle(24,26,28)

        print(self.params['leg_state'] , self.params['counter'] , self.params['leg_angle'])

        if self.params['leg_angle'] > 160 :
            self.params['leg_state'] = 0

        if self.params['leg_angle'] < 50 and self.params['leg_state'] == 0 :
            self.params['leg_state'] = 1
            self.params['counter'] += 1
            # print(self.params['counter'])

        if self.params['counter'] == 10 :
            return True
        return False      


if __name__ == "__main__" :
    # print(os.listdir(sys.path[0]+"/.."))
    # exe = Exercise()
    # exe.evaluate()
    

    exe = legStretch()
    print(exe.landmarkInfo)