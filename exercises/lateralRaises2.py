from exercise import *
import configparser
# from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play

# SOUNDPATH = "./exercises/beep1.wav"
SOUND_PATH1 = "exercises/sounds/right_hand_up.wav"
SOUND1 = AudioSegment.from_wav(SOUND_PATH1)


SOUND_PATH2 = "exercises/sounds/right_hand_down.wav"
SOUND2 = AudioSegment.from_wav(SOUND_PATH2)

class LateralRaises(Exercise) :
    def __init__(self ,rep_count) -> None:
        super().__init__()

        self.rep_count = int(rep_count)


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

        exercise_state = {
            'upstate' : 0,
            'downstate' : 1
        }
        
        self.params['right_elbow_angle'] = self.landmarkInfo.calculateAngle(16,14,12)
        self.params['left_elbow_angle'] = self.landmarkInfo.calculateAngle(15,13,11)
        self.params['right_shoulder_angle'] = self.landmarkInfo.calculateAngle(14,12,24)
        self.params['left_shoulder_angle'] = self.landmarkInfo.calculateAngle(13,11,23)

        state = exercise_state['upstate']

        if not state :
            # UPSTATE CODE 
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
                state = 1
                play(SOUND1)
            
            

        else :
            # DOWNSTATE CODE

            if self.params['right_elbow_angle'] > 150 and self.params['right_shoulder_angle'] < 20:
                self.params['right_hand_state'] = 0
            else :
                self.params['right_hand_state'] = 1
        
            if self.params['left_elbow_angle'] > 150 and self.params['left_shoulder_angle'] < 20:
                self.params['left_hand_state'] = 0
            else :
                self.params['left_hand_state'] = 1

            if not (self.params['left_hand_state'] and self.params['right_hand_state']) :
                self.params['both_hand_state'] = 1

            if (self.params['left_hand_state'] == 0) and (self.params['right_hand_state'] == 0) and (self.params['both_hand_state'] == 1) :
                # self.params['counter'] += 1
                self.params['both_hand_state'] = 0
                state = 0
                play(SOUND2)
            

        # if self.params['right_elbow_angle'] > 150 and self.params['right_shoulder_angle'] > 70:
        #     self.params['right_hand_state'] = 1
        # else :
        #     self.params['right_hand_state'] = 0
    
        # if self.params['left_elbow_angle'] > 150 and self.params['left_shoulder_angle'] > 70:
        #     self.params['left_hand_state'] = 1
        # else :
        #     self.params['left_hand_state'] = 0

        # if not (self.params['left_hand_state'] and self.params['right_hand_state']) :
        #     self.params['both_hand_state'] = 0


        # if self.params['left_hand_state'] and self.params['right_hand_state'] and (self.params['both_hand_state'] == 0) :
        #     self.params['counter'] += 1
        #     self.params['both_hand_state'] = 1
        #     play(SOUND)

        # if not (self.params['left_hand_state'] and self.params['right_hand_state']) and (self.params['both_hand_state'] == 1) :
        #     # self.params['counter'] += 1
        #     self.params['both_hand_state'] = 0
        #     play(SOUND)

        # if self.params['left_hand_state'] and not self.params['right_hand_state']


    def evaluate(self):
        self.calculateParams()

        

        if self.params['counter'] >= self.rep_count :
            return True


        return False


if __name__ == "__main__" :
    exe = LateralRaises()
    exe.evaluate()