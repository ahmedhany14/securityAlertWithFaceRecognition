import face_recognition
from ultralytics import YOLO
import os
import supervision as sv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PIL import Image, ImageTk


class Yolo_Model:

    def __init__(self):

        self.yolo = self.load_yolo()

    def load_yolo(self):
        return YOLO("yolov8l.pt")

    def yolo_analyze(self, outputs):

        objects = []

        for result in outputs:
            boxes = result.boxes.cpu().numpy()  # Boxes object for bounding box outputs
            for i in range(len(boxes)):
                # Extract the class ids
                class_id = int(boxes.cls[i])
                if class_id != 0:
                    continue
                # Extract the coordinates of the bounding box
                x1, y1, x2, y2 = boxes.xyxy[i]

                # Create a dictionary containing the class id, name, and coordinates
                properties = {
                    "corner1": (int(x1), int(y1)),
                    "corner2": (int(x2), int(y2)),
                }

                # Append the dictionary to the objects list
                objects.append(properties)

        # Return the list of objects
        return objects

    def detect_person(self, frame):

        resutls = self.yolo.predict(frame)

        detection = self.yolo_analyze(resutls)

        return detection

    pass


class face_recognition_Model:

    def __init__(self):
        self.known_faces = self.load_known_faces()
        self.unknown_faces = self.load_unknown_faces()

    def load_known_faces(self):
        url = "/home/hany_jr/Ai/securityAlertWithFaceRecognition/faces/known"
        images = os.listdir(url)

        return images

    def load_unknown_faces(self):
        url = "/home/hany_jr/Ai/securityAlertWithFaceRecognition/faces/unknown"
        images = os.listdir(url)

        return images

    def detect_face(self):

        known_path = "/home/hany_jr/Ai/securityAlertWithFaceRecognition/faces/known"
        unknown_path = "/home/hany_jr/Ai/securityAlertWithFaceRecognition/faces/unknown"

        unknow = []
        for un_img in self.unknown_faces:

            unknown_image = face_recognition.load_image_file(
                unknown_path + "/" + un_img
            )
            is_unknown = True
            for kn_img in self.known_faces:

                known_image = face_recognition.load_image_file(
                    known_path + "/" + kn_img
                )

                unknown_face_encoding = face_recognition.face_encodings(unknown_image)[
                    0
                ]
                known_face_encoding = face_recognition.face_encodings(known_image)[0]

                results = face_recognition.compare_faces(
                    [known_face_encoding], unknown_face_encoding
                )

                if results[0]:
                    is_unknown = False
                    continue
            if is_unknown:
                unknow.append(unknown_image)

        return unknow


yolo = Yolo_Model()

face_recognizer = face_recognition_Model()
