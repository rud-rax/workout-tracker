import cv2
import mediapipe as mp
import numpy as np
import os







mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

os.chdir(r"workout-tracker/images")

# For static images:
# IMAGE_FILES = os.listdir(r".")

IMAGE_FILES = []

for file in os.listdir("."):
    if os.path.isfile(file):
        IMAGE_FILES.append(file)

if not os.path.exists("tempImages") :

    os.mkdir("tempImages")



print("Files scanned : ",IMAGE_FILES)

BG_COLOR = (192, 192, 192) # gray
with mp_pose.Pose(
    static_image_mode=True,
    model_complexity=2,
    enable_segmentation=True,
    min_detection_confidence=0.5) as pose:
  for idx, file in enumerate(IMAGE_FILES):
    image = cv2.imread(file)
    # cv2.imshow("Orig",image)
    image_height, image_width, _ = image.shape
    # Convert the BGR image to RGB before processing.
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Process the image for landmark detection
    results = pose.process(image)

    

    if not results.pose_landmarks:
      continue
    # print(
    #     f'Nose coordinates: ('
    #     f'{results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x * image_width}, '
    #     f'{results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y * image_height})'
    # )

    annotated_image = image.copy()
    # Draw segmentation on the image.
    # To improve segmentation around boundaries, consider applying a joint
    # bilateral filter to "results.segmentation_mask" with "image".
    condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.1
    bg_image = np.zeros(image.shape, dtype=np.uint8)
    bg_image[:] = BG_COLOR
    annotated_image = np.where(condition, annotated_image, bg_image)

    # Display segmented image
    # cv2.imshow("Seg" , image)
    cv2.imwrite(r"tempImages/seg_"+str(file)+".png" , annotated_image)
    # Draw pose landmarks on the image.
    mp_drawing.draw_landmarks(
        annotated_image,
        results.pose_landmarks,
        mp_pose.POSE_CONNECTIONS,
        landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())


    cv2.imwrite(r"tempImages/annotated_" + str(file) + ".png", annotated_image)

    mp_drawing.draw_landmarks(
    image,
    results.pose_landmarks,
    mp_pose.POSE_CONNECTIONS,
    landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())

    image = cv2.cvtColor(image , cv2.COLOR_RGB2BGR)

    cv2.imwrite(r"tempImages/full_" + str(file) + ".png", image)
    # Plot pose world landmarks.
    # mp_drawing.plot_landmarks(
    #     results.pose_world_landmarks, mp_pose.POSE_CONNECTIONS)
