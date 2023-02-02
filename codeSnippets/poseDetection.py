
import cv2
import mediapipe as mp
import numpy as np

mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils


MIN_DET_CONF = 0.5
MIN_TRK_COMF = 0.5

FEED_DELAY = 10
FEED_EXIT_KEY = "x"

# LANDMARK CONNECTIONS
MP_POSE_CONNECTIONS = {
    (0,2),
    (0,5),
    (9,10),
    (7,9),
    (8,10),
    (5,8),
    (2,7)


}

# DRAWING SPECS
DRW_SPEC1 = mp_drawing.DrawingSpec(color = (19, 0, 90) , thickness = 4 , circle_radius = 4)
DRW_SPEC2 = mp_drawing.DrawingSpec(color = (253, 255, 0) , thickness = 4 , circle_radius = 4)

LANDMARKS_DRAWING_STYLE = mp.solutions.drawing_styles.get_default_pose_landmarks_style()




with mp_pose.Pose(min_detection_confidence = MIN_DET_CONF, min_tracking_confidence = MIN_TRK_COMF) as pose :
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        # CAPTURE IMAGE FRAME FROM CAMERA
        ret,frame = cap.read()

        # IMAGE PREPROCESSING
        image = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        # MAKE POSE DETECTIONS
        results = pose.process(image)

        # CONVERT IMAGE BACK TO BGR FORMAT
        image.flags.writeable = True
        image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)

        # EXTRACT LANDMARKS
        try :
            landmarks = results.pose_landmarks.landmark
        except :
            pass

        # PLOT LANDMARKS
        mp_drawing.draw_landmarks(image , results.pose_landmarks , MP_POSE_CONNECTIONS , DRW_SPEC1 , DRW_SPEC2
        
        )

        # DISPLAY IMAGE FEED
        cv2.imshow("Camera Feed" , image)

        # PRESS 'x' TO EXIT
        if cv2.waitKey(FEED_DELAY) & 0xFF == ord(FEED_EXIT_KEY) :
            break

    cap.release()
    cv2.destroyAllWindows()