# Overview
This project presents a machine learning-based approach to human pose detection, leveraging keypoint extraction and ensemble methods. It accurately detects six different poses (Balancing, Inverted, Reclining, Sitting, Standing, and Wheel Poses) and is tailored for use in fitness tracking, sports analysis, and rehabilitation.

# Dataset
The dataset includes a series of images specifically used for pose estimation. The key steps in dataset preparation are:

## Keypoints CSV:
Extracted pose landmarks from images using MediaPipe, formatted as CSV. This crucial step involves processing each image to identify and record pose landmark data.

## Merged CSV: 
Aggregated data of all poses. Includes an original dataset and a balanced version, achieved through sampling techniques to ensure robustness in pose detection.

# Files and Folders
The project is organized into several key sections:

Pose Detection before and after sampling: Analyzing the impact of data balancing on pose detection.

Analysis using Machine Learning Models: Exploring various machine learning models and ensemble techniques for improved accuracy.

Real-Time Pose Detection Implementation: Demonstrating the application in a real-time scenario.

User Interface: Folder containing all UI-related elements and files, ensuring a user-friendly interaction with the system.

# Real-Time Pose Detection
The implementation uses MediaPipe for Key Feature Extraction and a trained SVM model for pose classification. The system is capable of processing real-time video feeds, accurately classifying poses, and providing immediate feedback.

# Methodology
Data Collection and Preprocessing: Gathering and preparing the image dataset for analysis.

Keypoint Extraction: Using MediaPipe for precise extraction of pose landmarks from each image in the dataset.

Model Application: Employing machine learning algorithms such as SVM, Random Forest, KNN, Bagging Classifier, and Gradient Boosting Classifier, along with ensemble methods for enhanced detection accuracy.

Real-Time Implementation: Combining MediaPipe and SVM for real-time pose detection and classification.

# Results
The system demonstrates a high performance in pose detection, achieving an accuracy of 92% with SVM and 91% with Ensemble methods. Its capability to efficiently handle video processing in real-time makes it an ideal solution for applications in fitness tracking and rehabilitation.
