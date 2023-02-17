import configparser
import cv2
import mediapipe as mp

# Importing Pose Detection Module
from poseDetection import *

# Importing Landmarks Retrival Module
from landmarkInfo import *

# MEDIAPOSE DRAWING VARIABLES
MP_DRAWING_UTILS = mp.solutions.drawing_utils
DRAWING_SPEC_1 = MP_DRAWING_UTILS.DrawingSpec(color = (19, 0, 90) , thickness = 4 , circle_radius = 4)
DRAWING_SPEC_2 = MP_DRAWING_UTILS.DrawingSpec(color = (253, 255, 255) , thickness = 4 , circle_radius = 4)

# TEMPORARY GLOBAL VARIABLES USED FOR TESTING PURPOSES
CONNECTIONS = {
    (14,12),
    (16,14)
}

class VideoProcessing :
    '''
    Video Processing Module used for capturing video feed from the camera, and apply Pose Detection Models on it.
    '''

    def __init__(self) :

        pd = PoseDetectionModel()
        self.pose_model = pd.model

        self.landmarksInfo = LandmarkInfo()

        self.setVideoProcessingParams()

        self.image = None

    def setVideoProcessingParams(self) :
        '''
        Sets Video Processing Parameters specified in the config file.
        The path of the config file is specified in the global variable 'CONFIG_FILE_PATH'.
        '''

        configObj = configparser.ConfigParser()

        # SETS THE DEFAULT CONFIGURATIONS 
        configObj.read(CONFIG_FILE_PATH)

        video_processing_params =  configObj['VIDEO PROCESSING']

        self.feed_delay = int(video_processing_params['feed_delay'])
        self.feed_exit_key = video_processing_params['feed_exit_key']

    def capture(self,file = 0 ) :
        '''
        Starts capturing feed from the webcam or any videofile if specified.
        
        1st param - Path of videofile. By default set to '0' which starts the capturing live feed from the webcam.
        '''

        cap = cv2.VideoCapture(0)
        while cap.isOpened() : 
            ret,frame = cap.read()

            self.imagePreprocessing(frame)
            
            results = self.pose_model.process(self.image)

            try : 
                landmarks = results.pose_landmarks.landmark
           
                self.landmarksInfo.landmarks = landmarks
                # print(landmarks)
                print(self.landmarksInfo.calculateAngle(16,14,12))

            except AttributeError :
                print("No Landmarks found !")


            self.imageDisplayProcessing()

            # UNCOMMENT TO TEST WITH 'connections' VARIABLE FOR A SPECIFIC EXERCISE
            # self.plotLandmarks(landmarks , connections)

            # UNCOMMENT TO TEST WITH THE GLOBAL VARIABLE 'CONNECTIONS'
            self.plotLandmarks(results , CONNECTIONS)



            cv2.imshow("Camera Feed" , self.image)

            if cv2.waitKey(self.feed_delay) & 0xFF == ord(self.feed_exit_key) : 
                break

        cap.release()
        cv2.destroyAllWindows()

    def imagePreprocessing(self,frame) :
        '''
        Preprocessing of the frame before it is passed for Pose Detection.
        '''

        CVT_MODE = cv2.COLOR_BGR2RGB

        self.image = cv2.cvtColor(frame , CVT_MODE)
        self.image.flags.writeable = False


    def imageDisplayProcessing(self) :
        '''
        Image Processing of the image before it is displayed on the screen.
        Reverts back the preprocessing done to the frame after the Pose Detection process.
        '''
        CVT_MODE = cv2.COLOR_RGB2BGR

        self.image.flags.writeable = True
        self.image = cv2.cvtColor(self.image , CVT_MODE)


    def plotLandmarks(self,landmarks,connections) :
        '''
        Plots landmarks on the image.

        1st param : Landmarks to be plotted on then image.
        2nd param : Connections between landmarks.
        '''

        # print(landmarks)
        MP_DRAWING_UTILS.draw_landmarks(self.image , landmarks.pose_landmarks , connections , DRAWING_SPEC_1,DRAWING_SPEC_2)

