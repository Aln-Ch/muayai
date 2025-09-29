import cv2
import mediapipe as mp
import tempfile
import streamlit as st

st.title("Muay Thai Technique Analyzer MVP")
st.write("Upload a video of your technique to get started.")

video = st.file_uploader("Upload a training clip", type=["mp4", "mov", "avi", "mpeg4"])

if video:
    # Save upload to a temp file
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(video.read())

    # Load video with OpenCV
    cap = cv2.VideoCapture(tfile.name)

    # Setup mediapipe
    mp_pose = mp.solutions.pose
    mp_drawing = mp.solutions.drawing_utils
    pose = mp_pose.Pose()

    stframe = st.empty()  # placeholder for video frames

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert frame to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(image)

        # Draw landmarks
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(
                image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS
            )

        # Convert back to BGR for Streamlit
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        stframe.image(image, channels="BGR")

    cap.release()
