import mediapipe as mp


mp_pose = mp.solutions.pose

for i,landmark in enumerate(mp_pose.PoseLandmark) :
    print(i,landmark)