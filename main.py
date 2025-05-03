import streamlit as st
import cv2, time, numpy
from datetime import datetime

st.title("Motion Detector")
start = st.button("Start Camera")

# Activate camera in streamlit app
if start:
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(0)

    # Capture video
    while True:
        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # HUD
        # Get current time as datetime object
        now = datetime.now()
        # Print Day
        cv2.putText(img=frame, text=now.strftime("%A"), org=(30, 80),
                    fontFace=cv2.FONT_HERSHEY_PLAIN,
                    fontScale=3, color=(255, 255, 255),
                    thickness=2, lineType=cv2.LINE_AA)
        # Print Time
        cv2.putText(img=frame, text=now.strftime("%H:%M:%S"),
                    org=(30, 140),fontFace=cv2.FONT_HERSHEY_PLAIN,
                    fontScale=3, color=(255, 0, 0),
                    thickness=2, lineType=cv2.LINE_AA)


        # Preview frame
        streamlit_image.image(frame)




# Take the reference frame

# Check for differences

