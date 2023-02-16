from mediapipe import solutions







class LandmarkInfo :
    def __init__(self,landmarks) -> None:
        self.landmarks = landmarks

    def displayLandmarksIndices(self) : 
        for i,landmark in enumerate(solutions.pose.PoseLandmark) :
            print(i,landmark)


