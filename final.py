import cv2
import mediapipe as mp

# Initialize MediaPipe Face Detection
mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.5)

# Function to detect faces and count them
def detect_faces(image):
    # Convert the image to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Detect faces in the image
    results = face_detection.process(image_rgb)
    
    faces = []
    
    # Check if any faces are detected
    if results.detections:
        for detection in results.detections:
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, _ = image.shape
            x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
            faces.append((x, y, w, h))
    
    return faces

# Function to capture video from webcam, detect faces, and draw circles around faces
def main():
    cap = cv2.VideoCapture(1)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Detect faces
        faces = detect_faces(frame)
        
        # Draw circles around faces
        for (x, y, w, h) in faces:
            center = (x + w // 2, y + h // 2)
            radius = min(w, h) // 2
            cv2.circle(frame, center, radius, (0, 255, 0), 2)
        
        # Display face count on the frame
        face_count = len(faces)
        cv2.putText(frame, f"No. of persons: {face_count}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        cv2.imshow('Face Detection', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
