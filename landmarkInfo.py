from mediapipe import solutions
import numpy as np

# TEMPORARY GLOBAL VARIABLES FOR TESTING PURPOSES
DEFAULT_LANDMARKS_1 = {5,0,2}



class LandmarkInfo :
    def __init__(self,landmarks = DEFAULT_LANDMARKS_1) -> None:
        self.landmarks = landmarks

    def displayLandmarksIndices(self) : 
        for i,landmark in enumerate(solutions.pose.PoseLandmark) :
            print(i,landmark)

    def calculateAngle(self, lnd1 , lnd2 , lnd3) :
        '''
        Calculate the angle between 3 landmarks.
        Landmarks should be specified in form [x,y].

        1st param : First Landmark.
        2nd param : Second Landmark. This is also the middle landmark.
        3rd param : Third Landmark.
        '''

        lnd1 = self.getLandmarkCoordinates(lnd1)
        lnd2 = self.getLandmarkCoordinates(lnd2)
        lnd3 = self.getLandmarkCoordinates(lnd3)

        lnd1 = np.array(lnd1)
        lnd2 = np.array(lnd2)
        lnd3 = np.array(lnd3)

        angle1 = np.arctan2(lnd3[1] - lnd2[1] , lnd3[0] - lnd2[0])
        angle2 = np.arctan2(lnd1[1] - lnd2[1] , lnd1[0] - lnd2[0])

        radians = angle1 - angle2
        angle = abs(radians * 180 / np.pi)

        if angle > 180 :
            angle = 360 - angle

        return angle

    def getLandmarkCoordinates(self,landmark) :
        # print(solutions.pose.PoseLandmark.LEFT_ELBOW.value)
        return self.landmarks[landmark].x , self.landmarks[landmark].y


if __name__ == "__main__" :
    li = LandmarkInfo()
    li.calculateAngle(5,0,2)