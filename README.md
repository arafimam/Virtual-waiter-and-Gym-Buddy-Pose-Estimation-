This is a program created using mediapipe and openCV packages. 
Mediapipe solution to detect pose has 33 landmarks on different corners of the body. It is as showns: 
![Screenshot (919)](https://user-images.githubusercontent.com/86128944/127777627-e552f7a0-43b1-4d47-abab-3a33db051540.png)

Project video:
https://user-images.githubusercontent.com/86128944/127855667-95ba66f2-8318-44d2-a237-40f63ff397b9.mp4

Snapshots: 
![Screenshot (925)](https://user-images.githubusercontent.com/86128944/127856555-5ed4042b-1cf0-4aec-999f-8efc903bb369.png)

![Screenshot (926)](https://user-images.githubusercontent.com/86128944/127856570-1663a7e9-7db3-48af-954b-267b238b2dc4.png)

![Screenshot (927)](https://user-images.githubusercontent.com/86128944/127856623-4b7bc757-d78b-41a4-99cc-2c63b61e7f48.png)

![Screenshot (928)](https://user-images.githubusercontent.com/86128944/127856642-333a1488-63db-4e4c-8687-01ceaf0eeb0a.png)

![Screenshot (929)](https://user-images.githubusercontent.com/86128944/127856667-7998d3ff-1909-4afe-af13-05dc4df98eff.png)

Out of 33 landmarks 3 of the landmarks- left hip, left shoulder and left elbow are extracted (see info.txt to know about the process) and then the angle between them were computed. Using logical angle explanations waiter predictions are printed on the GUI open CV feature. 

This program will also work for any computer video by changing the .VideoCapture argument from 0 to the name of the video, ensuring the directory of the video is same as the directory of the project. 
To run this: 
1) Clone the video
2) open Python IDE (python 3.0+)
3) Download packages: opencv-python, numpy and mediapipe
4) press run

Future plans: add a speech recognition system instead of making the user type
