import mediapipe as mp
import cv2 as cv
import numpy as np

def calculate_angle(a, b, c):
    a = np.array(a)  # First
    b = np.array(b)  # Mid
    c = np.array(c)  # End

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180.0:
        angle = 360 - angle

    return angle

capture=cv.VideoCapture(0)
count=0



mpPose=mp.solutions.pose
mpDrawings=mp.solutions.drawing_utils
hand_state=None

with mpPose.Pose(min_detection_confidence=0.5,min_tracking_confidence=0.5) as pose:
    while capture.isOpened():
        ret, frame = capture.read()

        image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = pose.process(image)
        # print (results.pose_landmarks)



        image.flags.writeable = True
        image = cv.cvtColor(image, cv.COLOR_RGB2BGR)

        try:
            landmarks = results.pose_landmarks.landmark
            # find x and y coordinate of 3 landmarks--for left side
            left_wrist = [landmarks[mpPose.PoseLandmark.LEFT_WRIST.value].x,
                          landmarks[mpPose.PoseLandmark.LEFT_WRIST.value].y]
            left_shoulder = [landmarks[mpPose.PoseLandmark.LEFT_SHOULDER.value].x,
                             landmarks[mpPose.PoseLandmark.LEFT_SHOULDER.value].y]
            left_elbow = [landmarks[mpPose.PoseLandmark.LEFT_ELBOW.value].x,
                          landmarks[mpPose.PoseLandmark.LEFT_ELBOW.value].y]

            # compute angle
            angle = calculate_angle(left_shoulder, left_elbow, left_wrist)

            cv.putText(image, str(angle),
                       tuple(np.multiply(left_elbow, [640, 480]).astype(int)),
                       cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 139), 2, cv.LINE_AA
                       )

            if angle>110 and hand_state==None:
                hand_state='raise your hand further'
            if angle<90 and angle >50 and hand_state=='raise your hand further':
                hand_state='a little bit more!!'
            if angle<=50 and hand_state=='a little bit more!!':
                hand_state="Perfect Rep!"
                count=count+1

            if angle < 90 and angle > 50 and hand_state=="Perfect Rep!":
                hand_state="Hands Down"
            if angle>110 and hand_state=="Hands Down":
                hand_state=None



        except:
            pass

        cv.rectangle(image, (0, 0), (700, 100), (245, 117, 16), -1)
        cv.putText(image, 'Gym Buddy ', (15, 25),
                   cv.FONT_HERSHEY_SIMPLEX, 1, (0, 150, 200), 2, cv.LINE_AA)
        cv.putText(image, hand_state,
                   (60, 60),
                   cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 150, 200), 2, cv.LINE_AA)
        cv.putText(image, "Count: "+str(count),
                   (85, 85),
                   cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 150, 200), 2, cv.LINE_AA)
        mpDrawings.draw_landmarks(image, results.pose_landmarks)
        cv.imshow("Gym Tracker", image)
        if cv.waitKey(10) & 0xFF == ord('q'):
            break
    capture.release()
    cv.destroyAllWindows



