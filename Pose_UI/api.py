import keras
import tensorflow as tf
import numpy as np
from PIL import Image
import cv2
import mediapipe as mp
import matplotlib.pyplot as plt
from joblib import Parallel, delayed
import joblib
import os
import base64
import io

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

def predict(path):
    # Load SVM model
    svm_from_joblib = joblib.load('svm.pkl')

    try:
        # Load image and process pose landmarks
        img = cv2.imread(path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # Check if the image is blurry
        laplacian_var = cv2.Laplacian(img, cv2.CV_64F).var()
        if laplacian_var < 50:
            return None, "Image is too blurry. Please upload a clear image."

        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            # Convert the image to RGB and process it
            results = pose.process(img)

            # Check if pose landmarks are detected
            if results.pose_landmarks:
                # Extract pose landmarks and predict pose label
                landmarks = results.pose_landmarks.landmark
                temp = []
                for j in landmarks:
                    temp = temp + [j.x, j.y, j.z, j.visibility]
                pose_label = svm_from_joblib.predict([temp])[0]

                # Draw pose landmarks on image
                mp_drawing.draw_landmarks(img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=8, circle_radius=4),
                                          mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=8, circle_radius=4))

                # Convert image to base64-encoded string
                pil_img = Image.fromarray(img)
                buff = io.BytesIO()
                pil_img.save(buff, format="JPEG")
                encoded_string = base64.b64encode(buff.getvalue()).decode("utf-8")

                # Return pose label and base64-encoded image string
                return pose_label, encoded_string

            # Return None and message if pose landmarks are not detected
            return None, "Pose landmarks not detected. Please upload a clear image."

    # Return None and error message if there is an error with the image
    except cv2.error:
        return None, "Image is not clear or Blur Image. Please upload a clear image"
