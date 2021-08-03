import mediapipe as mp
import cv2 as cv
import numpy as np
import time



# function find angle:
def calculate_angle(a, b, c):
    a = np.array(a)  # First
    b = np.array(b)  # Mid
    c = np.array(c)  # End

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180.0:
        angle = 360 - angle

    return angle

# create VideoCapture object for webcam
capture = cv.VideoCapture(0)

# use mediapipe framework of pose to detect pose
mpPose = mp.solutions.pose

# import drawing utilities
mpDrawing = mp.solutions.drawing_utils

# define state of hand
hand_state = None
count=0

print('Welcome to our virtual restruraunt')
print('Menu:'+'\n'+'Hot dog'+'\n'+'pizza'+'\n'+'burger')
text= input("Type what you want to order")
total_time=10
i=0
print("Please wait for 10 seconds until virtual waiter comes \n")
while i  != total_time:

    print(i+1)
    print('seconds')
    time.sleep(1)
    i=i+1


with mpPose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:

    while capture.isOpened():
        ret, frame = capture.read()
        # convert image to RGB
        image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = pose.process(image)

        # convert image back to BGR
        image.flags.writeable = True
        image = cv.cvtColor(image, cv.COLOR_RGB2BGR)

        # extract landmarks
        try:
            landmarks = results.pose_landmarks.landmark
            # find x and y coordinate of 3 landmarks--for left side
            left_hip = [landmarks[mpPose.PoseLandmark.LEFT_HIP.value].x,
                        landmarks[mpPose.PoseLandmark.LEFT_HIP.value].y]
            left_shoulder = [landmarks[mpPose.PoseLandmark.LEFT_SHOULDER.value].x,
                             landmarks[mpPose.PoseLandmark.LEFT_SHOULDER.value].y]
            left_elbow = [landmarks[mpPose.PoseLandmark.LEFT_ELBOW.value].x,
                          landmarks[mpPose.PoseLandmark.LEFT_ELBOW.value].y]

            # compute angle
            angle_left = calculate_angle(left_hip, left_shoulder, left_elbow)

            cv.putText(image, str(angle_left),
                       tuple(np.multiply(left_shoulder, [640, 480]).astype(int)),
                       cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 139), 2, cv.LINE_AA
                       )

            if angle_left >= 90:
                hand_state='you ordered:'+text
            if angle_left < 20 and hand_state==None:
                hand_state = 'Please raise hand so that we can find you'
            if angle_left >= 20 and angle_left < 90 and hand_state == 'Please raise hand so that we can find you':
                hand_state = "your left hand is moving up"
            if angle_left >= 20 and angle_left < 90 and hand_state == 'you ordered:'+text:
                hand_state = "We found you. Thanks!"
            if angle_left<20 and hand_state=="We found you. Thanks!":
                hand_state="Waiter will be here with you soon"

        except:
            pass

        # GUI VISUALS and OPERATIONS
        cv.rectangle(image, (0, 0), (700, 100), (245, 117, 16), -1)
        cv.putText(image, 'Virtual waiter: ', (15, 25),
                   cv.FONT_HERSHEY_SIMPLEX, 1, (0, 150, 200), 2, cv.LINE_AA)
        cv.putText(image, hand_state,
                   (60, 60),
                   cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 150, 200), 2, cv.LINE_AA)
        mpDrawing.draw_landmarks(image, results.pose_landmarks, mpPose.POSE_CONNECTIONS)

        cv.imshow("POSE_GUESS", image)
        if cv.waitKey(10) & 0xFF == ord('q'):
            break

    capture.release()
    cv.destroyAllWindows()
