This is a program created using mediapipe and openCV packages. 
Mediapipe solution to detect pose has 33 landmarks on different corners of the body. It is as showns: 
![Screenshot (919)](https://user-images.githubusercontent.com/86128944/127777627-e552f7a0-43b1-4d47-abab-3a33db051540.png)

Landmarks were extracted and the angles between left_hip, left_shoulder and left_elbow are measured by the program. The results are shown below:

![Screenshot (916)](https://user-images.githubusercontent.com/86128944/127777668-e4f8ce07-a49d-4576-9d91-6f36149e376d.png)

![Screenshot (917)](https://user-images.githubusercontent.com/86128944/127777678-a6be2974-14c1-4220-b34a-d40a7ee18aa8.png)

This program will also work for any computer video by changing the .VideoCapture argument from 0 to the name of the video, ensuring the directory of the video is same as the directory of the project. 
To run this: 
1) Clone the video
2) open Python IDE (python 3.0+)
3) Download packages: opencv-python, numpy and mediapipe
4) press run

Future plans: to add a counter that will count the number of times hand were raised