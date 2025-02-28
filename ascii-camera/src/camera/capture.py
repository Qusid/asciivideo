# filepath: /ascii-camera/ascii-camera/src/camera/capture.py

import cv2

class CameraCapture:
    def __init__(self, camera_index=0):
        self.camera_index = camera_index
        self.cap = None

    def initialize_camera(self):
        self.cap = cv2.VideoCapture(self.camera_index)
        if not self.cap.isOpened():
            raise Exception("Could not open camera")

    def capture_frame(self):
        if self.cap is None:
            raise Exception("Camera not initialized")
        ret, frame = self.cap.read()
        if not ret:
            raise Exception("Could not read frame")
        return frame

    def release_camera(self):
        if self.cap is not None:
            self.cap.release()
            self.cap = None