# import cv2
# import numpy as np

# step1: reading and illustrating images

# master_in_nature = 'IMG_0712.JPG'
# master_in_north = 'IMG_0468.jpg'
# img = cv2.imread(master_in_north)

# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# end of step1.



"""
One of the popular algorithms for facial detection is “haarcascade”.
 It is computationally less expensive, a fast algorithm, and gives high accuracy.


It works in four stages:

Haar-feature selection: A Haar-like feature consists of dark regions and light regions. 
It produces a single value by taking the difference of the sum of the intensities of the dark regions and the sum of the intensities of light regions. 
It is done to extract useful elements necessary for identifying an object. 


Creation of Integral Images: A given pixel in the integral image is the sum of all the pixels on the left and all the pixels above it. 
Since the process of extracting Haar-like features involves calculating the difference of dark and light rectangular regions, the introduction of Integral Images reduces the time needed to complete this task significantly.


AdaBoost Training: This algorithm selects the best features from all features. 
It combines multiple “weak classifiers” (best features) into one “strong classifier”. 
The generated “strong classifier” is basically the linear combination of all “weak classifiers”.


Cascade Classifier: It is a method for combining increasingly more complex classifiers like AdaBoost in a cascade which allows negative input (non-face) to be quickly discarded while spending more computation on promising or positive face-like regions. 
It significantly reduces the computation time and makes the process more efficient.
"""

# step2: face_detection

# master_in_nature = 'IMG_0712.JPG'
# master_in_north = 'IMG_0468.jpg'
# img = cv2.imread(master_in_nature)
# img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# ## build cascade classifier
# haar_cascade = cv2.CascadeClassifier('./Haar/haarcascade_frontalface_default.xml')
# ## detect face
# faces_rect = haar_cascade.detectMultiScale(img_gray, scaleFactor=1.3, minNeighbors=7)
# for (x, y, w, h) in faces_rect:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 0), thickness=10)
#     cv2.putText(img, "Master",(x, y-20), cv2.FONT_HERSHEY_SIMPLEX,3,(0,255,0), 5)

# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# end of step2.



# step3: reading and dispalying vidoes

"""
Syntax

cv2.VideoCapture(0): Means first camera or webcam.
cv2.VideoCapture(1):  Means second camera or webcam.
cv2.VideoCapture(“file name.mp4”): Means video file
"""

# # Create a VideoCapture object and read from input file 
# cap = cv2.VideoCapture('IMG_0894.MOV') 
  
# # Check if camera opened successfully 
# if (cap.isOpened()== False): 
#     print("Error opening video file") 
  
# # Read until video is completed 
# while(cap.isOpened()): 
      
# # Capture frame-by-frame 
#     ret, frame = cap.read() 
#     if ret == True: 
#     # Display the resulting frame 
#         cv2.imshow('Frame', frame) 
          
#     # Press Q on keyboard to exit 
#         if cv2.waitKey(1) & 0xFF == ord('q'): 
#             break
  
# # Break the loop 
#     else: 
#         break
  
# # When everything done, release 
# # the video capture object 
# cap.release() 
  
# # Closes all the frames 
# cv2.destroyAllWindows() 

# end of step3.


# step4: real-time face-detection

# Create a VideoCapture object and read from input file 
# cap = cv2.VideoCapture(0) 
# haar_cascade = cv2.CascadeClassifier('./Haar/haarcascade_frontalface_default.xml')
# # Check if camera opened successfully 
# if (cap.isOpened()== False): 
#     print("Error opening video file") 
  
# # Read until video is completed 
# while(cap.isOpened()): 
      
# # Capture frame-by-frame 
#     ret, frame = cap.read() 
#     if ret == True: 

#     # Display the resulting frame 
#         frame_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
#         faces_rect = haar_cascade.detectMultiScale(frame_gray, scaleFactor=1.3, minNeighbors=7)
#         for (x, y, w, h) in faces_rect:
#             cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
#             cv2.putText(frame, "Face",(x, y-20), cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255), 2)
#             cv2.imshow('image', frame)

          
#     # Press Q on keyboard to exit 
#         if cv2.waitKey(5) & 0xFF == ord('q'): 
#             break
  
# # Break the loop 
#     else: 
#         break
  
# # When everything done, release 
# # the video capture object 
# cap.release() 
  
# # Closes all the frames 
# cv2.destroyAllWindows() 

# end of step4.
























