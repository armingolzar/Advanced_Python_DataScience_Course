# Step1 : Reading a video 
# import cv2

# # Path to your video file
# video_path = "test_video.mp4"

# cv2.namedWindow("Video", cv2.WINDOW_NORMAL)

# # Resize the window (does not change frame resolution)
# cv2.resizeWindow("Video", 800, 600)  # width=800, height=600

# # Open the video file
# cap = cv2.VideoCapture(video_path)

# while cap.isOpened():
#     ret, frame = cap.read()  # Read a frame
#     if not ret:
#         break

#     cv2.imshow("Video", frame)  # Display the frame

#     # Press 'q' to exit
#     if cv2.waitKey(25) & 0xFF == ord('q'):   # cv2.waitKey(1) → the argument controls the delay in milliseconds. Smaller value = smoother streaming.
#         break

# cap.release()
# cv2.destroyAllWindows()


######################################################################################################

# # Step2 : Start streaming
# cap = cv2.VideoCapture(0)  # cv2.VideoCapture(0) → default webcam; you can use 1, 2, ... for other cameras.

# cv2.namedWindow("Webcam Stream", cv2.WINDOW_NORMAL)

# # Resize the window (does not change frame resolution)
# cv2.resizeWindow("Webcam Stream", 800, 600)  # width=800, height=600

# while True:
#     ret, frame = cap.read()  # Capture frame from camera
#     if not ret:
#         print("Failed to grab frame")
#         break

#     cv2.imshow("Webcam Stream", frame)  # Display the frame

#     # Press 'q' to exit
#     if cv2.waitKey(1) & 0xFF == ord('q'):   # cv2.waitKey(1) → the argument controls the delay in milliseconds. Smaller value = smoother streaming.
#         break

# cap.release()
# cv2.destroyAllWindows()


# Attention sometimes in windows when you read a video or stream the frames are rotated in this case use the code below befor showing the frame
# frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE) 