# In this practice we want to detect different parts of human face with haarcascade models.
# each haarcascade model takes gray input image and gives the 4 point for bounding box as an output.
# Example: mouth_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_mcs_mouth.xml"), mouths = mouth_cascade.detectMultiScale(image, 1.5, 10)
# So the mouths is 4 points of bounding box for mouths.

# for this practis you should detects face, eyes, mouth, ears, nose using haarcascade models.
# for face and mouth it should be rectangle but for eyes, ears and nose it should be a circle
# use these models for detection: haarcascade_frontalface_default.xml, haarcascade_mcs_nose.xml, haarcascade_mcs_mouth.xml
# haarcascade_mcs_rightear.xml, haarcascade_mcs_leftear.xml, haarcascade_mcs_righteye.xml, haarcascade_mcs_lefteye.xml in the Haar directory.

# What are the last two arguments in mouths = mouth_cascade.detectMultiScale(image, 1.5, 10)?