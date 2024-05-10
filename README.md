Real-time Face Detection and Counting with OpenCV and MediaPipe
----------------------------------

This Python project allows you to detect and count faces in real-time using your webcam. It leverages the power of OpenCV for computer vision tasks and MediaPipe's pre-trained face detection model for accurate face identification.


-------------------------------------
Features

Efficient Face Detection: Identifies faces in video frames with high accuracy, even under varying lighting conditions.

Real-time Processing: Processes video streams from your webcam for continuous face detection.

Visual Feedback: Provides clear visualization by drawing green circles around detected faces.

Face Count Display: Overlays the number of detected faces directly on the video frame.


------------------------------------
Benefits

Offers a simple and efficient solution for basic face detection tasks.

Provides a solid foundation for building more advanced face analysis applications like face recognition, emotion detection, or face tracking.

Easy-to-understand code makes it a valuable learning resource for those interested in computer vision.

---------------------------------------
Getting Started

Clone the repository:

git clone https://github.com/bennyd6/Counting-number-of-faces-in-the-frame-using-Computer-Vision.git

Make sure you have Python 3.x installed on your system. 

Then, install the necessary libraries using pip:

pip install opencv-python mediapipe

Run the script:

Navigate to the project directory in your terminal and execute the script:

python face_detection_counter.py

-------------------------------
Note: You might need to run the script with administrative privileges depending on your system configuration.

---------------------------------------------------
How it Works

The code utilizes two primary functions:


detect_faces(image): This function takes an image frame as input and performs the following tasks:


Converts the image to RGB format (required by MediaPipe's face detection model).

Detects faces using the pre-trained MediaPipe model.

Extracts bounding boxes for each detected face.

Returns a list containing the bounding box coordinates for identified faces.

main(): This function handles the overall program execution:

Opens the webcam to capture video frames.

Enters a loop that continuously reads frames from the webcam.

Calls the detect_faces function to identify faces in each frame.

Draws green circles around detected faces for visualization.

Calculates and displays the total number of faces on the frame.

Shows the processed frame with detected faces and face count.

Waits for a key press to exit the program (pressing 'q' terminates the program).

-----------------------------------------------------------

Extending the Project

This code provides a basic framework for face detection and counting. You can further enhance it by incorporating functionalities like:

Face Recognition: Train a model to recognize specific individuals based on their facial features.

Emotion Detection: Analyze facial expressions to detect emotions like happiness, sadness, or anger.

Face Tracking: Track the movement of faces across video frames for applications like gaze tracking.

Feel free to explore and experiment with the code to build more advanced face analysis applications based on your specific needs.
