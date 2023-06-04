from exercise import *
import configparser

from pydub.playback import play
from sounds_variable import *
import time

class BicepCurls(Exercise):
    def __init__(self , rep_count = 10):
        super().__init__()

        self.name = "Bicep Curls"
        self.rep_count = int(rep_count)

        self.intro_done = False
        self.state = 0

        self.connections = {
            (16, 14),
            (14, 12),
            (12, 24),
            (15, 13),
            (13, 11),
            (11, 23),
        }

        self.params = {
            "counter": 0,
            "left_elbow_angle": 0,
            "right_elbow_angle": 0,
            "left_hand_state": 0,
            "right_hand_state": 0,
            "both_hand_state": 0
        }

        self.imageText = [[self.params['counter'] , (100,100)] , [self.params['left_hand_state'] , (200,100)],[self.params['right_hand_state'] , (300,100)],[self.name , (100,200)] ,[self.rep_count , (100,300)] ]

    def calculateParams(self):


        exercise_state = {
            'upstate' : 0,
            'downstate' : 1
        }

        self.params["left_elbow_angle"] = self.landmarkInfo.calculateAngle(15, 13, 11)
        self.params["right_elbow_angle"] = self.landmarkInfo.calculateAngle(16, 14, 12)

        if self.params["left_elbow_angle"] > 60:
            self.params["left_hand_state"] = 1
        else:
            self.params["left_hand_state"] = 0

        if self.params["right_elbow_angle"] > 60:
            self.params["right_hand_state"] = 1
        else:
            self.params["right_hand_state"] = 0

        if not (self.params["left_hand_state"] and self.params["right_hand_state"]):
            self.params["both_hand_state"] = 0

        if self.params["left_hand_state"] and self.params["right_hand_state"] and (self.params["both_hand_state"] == 0):
            self.params["counter"] += 1
            self.params["both_hand_state"] = 1
            play(COUNTER_SOUNDS[self.params['counter']])

            if self.params['counter'] == (self.rep_count // 2) :
                play(HALF_WAY_SOUND)

        self.imageText = [[self.params['counter'] , (100,100)] , [self.params['left_hand_state'] , (200,100)],[self.params['right_hand_state'] , (300,100)],[self.name , (100,200)] ,[self.rep_count , (100,300)] ]
        
    def evaluate(self):

        if not self.intro_done : 
            time.sleep(3)
            play(HANDS_STRAIGHT_SOUND)
            play(START_REP_COUNT_SOUND)
            self.intro_done = True

        self.calculateParams()

        state = 0
        if self.params["counter"] == self.rep_count:
            return True
        
        return False

if __name__ == "__main__":
    exe = BicepCurls(5)
    exe.evaluate()