import configparser
import cv2
import mediapipe as mp

# Importing Pose Detection Module
from poseDetection import *

# Importing Landmarks Retrival Module
from landmarkInfo import *

# MEDIAPOSE DRAWING VARIABLES
MP_DRAWING_UTILS = mp.solutions.drawing_utils
DRAWING_SPEC_1 = MP_DRAWING_UTILS.DrawingSpec(color = ( 19,   0,  90) , thickness = 4 , circle_radius = 4)
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

        # self.landmarksInfo = LandmarkInfo()

        self.setVideoProcessingParams()

        self.image = None
        self.results = None

        self.exercise = None

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
        
        cap = cv2.VideoCapture(file)
        endloop = False

        while cap.isOpened() : 
            ret,frame = cap.read()

            self.imagePreprocessing(frame)
            
            self.results = self.pose_model.process(self.image)

            try : 
                landmarks = self.results.pose_landmarks.landmark
                # print(landmarks)
                try : 
                    self.exercise.landmarkInfo.landmarks = landmarks
                    
                    # FOR TESTING PURPOSES
                    # print(landmarks)

                    # EVALUATE EXERCISE HERE
                    endloop = self.exercise.evaluate()

                    # PLOT LANDMARKS OR DISPLAY TEXT ON THE IMAGE
                    # self.imageModify([angle,(100,100)])
                    # self.imageModify([self.exercise.params['counter'] , (100,100)])
                    self.imageModify([self.exercise.params['counter'] , (100,100)] , [self.exercise.params['left_hand_state'] , (200,100)],[self.exercise.params['right_hand_state'] , (300,100)],[self.exercise.name , (100,200)] ,[self.exercise.rep_count , (100,300)])


                except Exception as e:
                    print(e)

            except AttributeError :
                print("No Landmarks found !")


            self.imageDisplayProcessing()

            cv2.imshow("Camera Feed" , self.image)

            if (cv2.waitKey(self.feed_delay) & 0xFF == ord(self.feed_exit_key)) or (endloop): 
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

    def imageModify(self,*args,display_landmarks = True) : 
        '''
        Plots landmarks and display text on the image.
        Text can be displayed on the image by passing one or more tuples in the form (TEXT, POSITION)
            - TEXT should be a string
            - POSITION should be a tuple in the form (x,y) where x and y are the coordinates to display the text for the image.
        '''

        if display_landmarks : 
            # UNCOMMENT TO TEST WITH 'connections' VARIABLE FOR A SPECIFIC EXERCISE
            self.plotLandmarks()

            # UNCOMMENT TO TEST WITH THE GLOBAL VARIABLE 'CONNECTIONS'
            # self.plotLandmarks(CONNECTIONS)

        for arg in args :
            # print(arg[0])
            self.putText(str(arg[0]),arg[1])


    def putText(self,text , position : tuple , font = cv2.FONT_HERSHEY_SIMPLEX , fontscale = 1, color : tuple = (255,0,0) , thickness = 2 , linetype = cv2.LINE_AA ) : 
        '''
        Display text on the image.

        1st param : Text to display.
        2nd param : Position to display on the image in the form of x and y coordinates. [x,y]
        3rd param : Font of the text.
        4th param : Scale of the text.
        5th param : Color of the text.
        6th param : Thickness of the text.
        7th param : LineType of the text.

        '''
        cv2.putText(self.image,text,position,font , fontscale,color ,thickness, linetype)


    def plotLandmarks(self) :
        '''
        Plots landmarks on the image.

        1st param : Landmarks to be plotted on then image.
        2nd param : Connections between landmarks.
        '''

        # print(landmarks)
        MP_DRAWING_UTILS.draw_landmarks(self.image , self.results.pose_landmarks , self.exercise.connections , DRAWING_SPEC_1,DRAWING_SPEC_2)



def testingEvaluate() : 
    # angle = self.landmarksInfo.calculateAngle(16,14,12)
    # print(angle)
    # angle = str(round(angle, 2))
    print("Evaluating Exercise !!!")