# Step1 : Reading a video 
# import cv2

# Path to your video file
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

#####################################################################################################################################

# Step3 : Writing and Saving video
# import cv2

# # Open the webcam (0 = default camera)
# cap = cv2.VideoCapture(0)

# # Check if camera opened successfully
# if not cap.isOpened():
#     print("Error: Cannot open webcam")
#     exit()

# # Get width and height of frames from the webcam
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# # Define video writer
# output_path = "webcam_output.mp4"
# fps = 30  # Frames per second
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # codec
# out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# # Optional: create resizable display window
# cv2.namedWindow("Webcam Stream", cv2.WINDOW_NORMAL)
# cv2.resizeWindow("Webcam Stream", 800, 600)  # just display smaller

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("Failed to grab frame")
#         break

#     # Show the video in a smaller window
#     cv2.imshow("Webcam Stream", frame)

#     # Write frame to video file
#     out.write(frame)

#     # Press 'q' to quit
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# out.release()
# cv2.destroyAllWindows()
# print(f"Video saved to {output_path}")

# Attention if you want to create a video from list of frame you should do this:

# frames = [...]  # Your list of frames

# # Get size from the first frame
# height, width, channels = frames[0].shape

# # Define VideoWriter
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter('output.mp4', fourcc, 30, (width, height))

# # Write frames
# for frame in frames:
#     out.write(frame)

# out.release()

