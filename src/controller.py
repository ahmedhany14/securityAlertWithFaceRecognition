# import the all dependencies from the model and view

import cv2
import numpy as np
import time
import os
import time
import datetime
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

from model import *


class controller:

    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        pass

    def main(self):
        """
        In the main function i will start streaming the video from the camera
        """
        self.cap.open(0)

        if not self.cap.isOpened():
            raise Exception("Error: Camera not found")

        while True:
            result, frame = self.cap.read()

            frame = cv2.resize(frame, (0, 0), fx=0.75, fy=0.75)

            if not result:
                print("Error: Camera not found")
                break
            cv2.imshow("frame", frame)

            detected_images = self.yolo_analyze(frame)

            if detected_images != 0:

                someone_detected = self.face_recognition_analysis()

                if someone_detected:
                    self.send_messege(len(someone_detected))

                    break

                break

            if cv2.waitKey(1) == ord("q"):
                break
        return

    def crop_imge(self, frame, x1, y1, x2, y2):
        """
        This function will crop the image and save it to the disk
        """
        crop_img = frame[y1:y2, x1:x2]

        return crop_img

    def save_image_to_disk(self, image):

        url = "/home/hany_jr/Ai/securityAlertWithFaceRecognition/faces/unknown"

        for i in range(len(image)):
            cv2.imwrite(url + "/image" + str(i) + ".jpg", image[i])

        pass

    def yolo_analyze(self, frame):

        result = yolo.detect_person(frame)

        if len(result) > 0:
            """
            start to crop the image and save it to the disk
            and for each image saved, i will send it to the face recognition model
            """

            images = []
            for person in result:

                image = self.crop_imge(
                    frame,
                    person["corner1"][0],
                    person["corner1"][1],
                    person["corner2"][0],
                    person["corner2"][1],
                )
                images.append(image)

            self.save_image_to_disk(images)
            return 1

        return 0

    def face_recognition_analysis(self):
        """
        This function will check if the face is known or not
        """

        faces = face_recognizer.detect_face()

        print(faces)
        return faces

    def send_messege(self, detected_people):
        """
        This function will send a message to the owner of the house
        """
        data = {}
        # Open and read the JSON file

        with open(
            "/home/hany_jr/Ai/securityAlertWithFaceRecognition/data.json", "r"
        ) as file:
            data = json.load(file)

            email = data["from_email"]
            password = data["password"]
            to_email = data["to_email"]
            print(
                email,
                password,
            )
            # Email content
            subject = "Security Alert"
            body = (
                "There is an intruder in your house\nNumber of people detected: "
                + str(detected_people)
            )

            # Email server settings
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(email, password)

            # Email message
            message = f"Subject: {subject}\n\n{body}"

            # Send email
            server.sendmail(email, to_email, message)
            server.quit()
            return

        pass

    def delete_unknown_faces(self):
        """
        This function will delete all the unknown faces
        """

        url = "/home/hany_jr/Ai/securityAlertWithFaceRecognition/faces/unknown"

        for img in os.listdir(url):
            os.remove(url + "/" + img)
        pass


control = controller()
control.main()
