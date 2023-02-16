import configparser
import cv2
import mediapipe as mp
from poseDetection import *


class VideoProcessing :

    def __init__(self) :

        pd = PoseDetectionModel()
        self.pose_model = pd.model

        self.setVideoProcessingParams()

    def setVideoProcessingParams(self) :

        configObj = configparser.ConfigParser()
        configObj.read(CONFIG_FILE_PATH)
        video_processing_params =  configObj['VIDEO PROCESSING']


        self.feed_delay = int(video_processing_params['feed_delay'])
        self.feed_exit_key = video_processing_params['feed_exit_key']

    def capture(self) :

        cap = cv2.VideoCapture(0)
        while cap.isOpened() : 
            ret,frame = cap.read()

            image = self.imagePreprocessing(frame)
            
            results = self.pose_model.process(image)

            print(results)

            image = self.imageDisplayProcessing(image)

            cv2.imshow("Camera Feed" , image)

            if cv2.waitKey(self.feed_delay) & 0xFF == ord(self.feed_exit_key) : 
                break

        cap.release()
        cv2.destroyAllWindows()

    def imagePreprocessing(self,frame) :

        CVT_MODE = cv2.COLOR_BGR2RGB

        image = cv2.cvtColor(frame , CVT_MODE)
        image.flags.writeable = False
        return image

    def imageDisplayProcessing(self,image) :
        CVT_MODE = cv2.COLOR_RGB2BGR

        image.flags.writeable = True
        image = cv2.cvtColor(image , CVT_MODE)
        return image

