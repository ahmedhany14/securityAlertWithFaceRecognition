# securityAlertWithFaceRecognition

<br />
<p align="center">

  <h3 align="center"> securityAlertWithFaceRecognition </h3>
</p>

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Description](#description)
- [Features](#features)
- [Packages and frameworks i used](#packages-and-frameworks-i-used)
- [Installing packages](#installing-packages)
- [Usage](#usage)
- [How It Works](#how-it-works)

## Description

This repository contains the implementation of a Security Alert System that utilizes YOLO (You Only Look Once) for object detection and Face Recognition for identifying individuals in a given frame. The system captures video input, detects people, recognizes faces, and sends alerts when an unauthorized individual is detected.

## Features

* **YOLO-based Object Detection** : Detects the presence of humans in real-time.
* **Face Recognition**: Identifies and verifies faces using a pre-trained face recognition model.
* **Alert System**: Sends an email when an unknown face is detected.
* **Real-time Video Processing**: Efficient video processing using YOLO for detection and face recognition.
* **Flexible Integration**: Can be integrated into various security setups for homes, offices, or restricted areas.

## Packages and frameworks i used

- [Python 3.x]()
- [numpy](https://keras.io/) for Algebra
- [pandas](https://pandas.pydata.org/docs/) for datasets
- [cv2](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html) For images
- [ultralytics](https://docs.ultralytics.com/guides/) For YOLO model
- [face_recognition] (https://pypi.org/project/face-recognition/) For detect the unknown faces
- [os](https://docs.python.org/3/library/os.html) For control the dirictories 


## Installing packages

**Clone the repository**

    git clone https://github.com/ahmedhany14/securityAlertWithFaceRecognition.git
    cd securityAlertWithFaceRecognition

**Create the conda environment**

    conda create -n securityAlerEnv python=3.12
    conda env list
    conda activate securityAlerEnv

**Install the required dependencies**

    pip install -r requirements.txt


## Usage 

    python controller.py

## How It Works

* **Video Capturing**

    1) By using cv2, The system will start capturing live video (from webcam or input video file),
    2) The system will take all frames and start the analysis

* **YOLO Detection**

    1) The YOLO model will take all the frames to detect people in the video frames.
    2) The model will provied us a bounding boxes around detected people are fed into the face recognition model.

* **Face Recognition**

    1) The system uses the *face_recognition* library, which applies deep learning to compare faces.
    2) Known faces (from a pre-configured database) are identified, and if an unknown face is found, an alert is triggered.

* **Alert System**

    1) The system sends an alert (email) when an unauthorized or unrecognized individual is detected.
