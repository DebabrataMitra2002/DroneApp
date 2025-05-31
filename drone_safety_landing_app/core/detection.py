import torch
from ultralytics import YOLO
import cv2

class ThreatDetector:
    def __init__(self, model_path):
        self.model = YOLO(model_path)

    def detect_threats(self, frame):
        results = self.model.predict(source=frame, conf=0.5, verbose=False)
        threats = []
        for result in results:
            for box in result.boxes:
                cls = int(box.cls.item())
                conf = box.conf.item()
                if conf > 0.5:
                    threats.append((cls, box.xyxy[0].tolist(), conf))
        return threats