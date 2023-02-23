from exercise import *
import configparser

class LateralRaises(Exercise) :
    def __init__(self) -> None:
        super().__init__()

        self.name = "Lateral Raises"

        self.connections = {
            (16,14),
            (14,12),
            (12,24),
            (15,13),
            (13,11),
            (11,23)
        }

        self.params = {
            "counter" : 0,
            "right_elbow_angle" : 0 ,
            "left_elbow_angle" : 0,
            "right_shoulder_angle" : 0,
            "left_shoulder_angle" : 0,
            "right_hand_state" : 0,
            "left_hand_state" : 0,
            "both_hand_state" : 0
        }

    def calculateParams(self) :
        self.params['right_elbow_angle'] = self.landmarkInfo.calculateAngle(16,14,12)
        self.params['left_elbow_angle'] = self.landmarkInfo.calculateAngle(15,13,11)
        self.params['right_shoulder_angle'] = self.landmarkInfo.calculateAngle(14,12,24)
        self.params['left_shoulder_angle'] = self.landmarkInfo.calculateAngle(13,11,23)

        if self.params['right_elbow_angle'] > 150 and self.params['right_shoulder_angle'] > 70:
            self.params['right_hand_state'] = 1
        else :
            self.params['right_hand_state'] = 0
    
        if self.params['left_elbow_angle'] > 150 and self.params['left_shoulder_angle'] > 70:
            self.params['left_hand_state'] = 1
        else :
            self.params['left_hand_state'] = 0

        if not (self.params['left_hand_state'] and self.params['right_hand_state']) :
            self.params['both_hand_state'] = 0


        if self.params['left_hand_state'] and self.params['right_hand_state'] and (self.params['both_hand_state'] == 0) :
            self.params['counter'] += 1
            self.params['both_hand_state'] = 1


    def evaluate(self):
        self.calculateParams()

        # for k in self.params.keys() :
        #     print(f"{k} {self.params[k]}",end = " - ")

        # print()
        state = 0 

        if self.params['counter'] == 10 :
            return True


        return False


if __name__ == "__main__" :
    exe = LateralRaises()
    exe.evaluate()