import torch
import cv2

class ThreatDetector:
    def __init__(self, model_path):
        self.model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path, force_reload=False)

    def detect_threats(self, frame):
        results = self.model(frame)
        return results.pandas().xyxy[0]  # Return detections as DataFrame
