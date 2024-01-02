# Overview
This project presents a machine learning-based approach to human pose detection, utilizing keypoints extraction and ensemble methods. It aims to detect six different poses (Balancing, Inverted, Reclining, Sitting, Standing, and Wheel Poses) with high accuracy and applicability in various real-world scenarios like fitness tracking, sports analysis, and rehabilitation.

# Dataset
Dataset: A collection of images used for pose estimation.
Keypoints CSV: Pose landmarks extracted using MediaPipe, stored in CSV format.
Merged CSV: Aggregated data of all poses and a balanced dataset using sampling techniques.

# Files and Folders
Notebooks: Jupyter notebooks detailing the process.
Pose Detection before and after sampling.
Analysis using Ensemble Methods.
Real-Time Pose Detection Implementation.
User Interface: A dedicated folder containing UI elements and files.

# Real-Time Pose Detection
The implementation uses MediaPipe for pose detection and a trained SVM model for pose classification. The system is capable of processing real-time video feeds, accurately classifying poses, and providing immediate feedback.

# Methodology
Data collection and preprocessing.
Feature extraction using the MediaPipe pose detection model.
Application of machine learning algorithms (SVM, Random Forest, KNN, Bagging Classifier, Gradient Boosting Classifier) and ensemble methods.
Real-time pose detection implementation using MediaPipe and SVM.

# Results
The system demonstrates high performance in pose detection, achieving an accuracy of 92% with Ensemble methods. The real-time implementation can efficiently handle video processing with minimal latency, making it suitable for applications like fitness tracking and rehabilitation.
