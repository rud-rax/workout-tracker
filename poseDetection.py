
import mediapipe as mp
import configparser

CONFIG_FILE_PATH = r"./config.ini"

        
class PoseDetectionModel :
    def __init__(self) :

        self.setPoseDetectionParams()
        
        self.model = mp.solutions.pose.Pose(min_detection_confidence = self.min_detection_confidence ,min_tracking_confidence = self.min_tracking_confidence)

    def setPoseDetectionParams(self):
        configObj = configparser.ConfigParser()
        configObj.read(CONFIG_FILE_PATH)
        
        pose_detection_params = configObj["POSE DETECTION"]

        self.min_detection_confidence = float(pose_detection_params['min_detection_confidence'])
        self.min_tracking_confidence = float(pose_detection_params['min_tracking_confidence'])


