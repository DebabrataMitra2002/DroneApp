# tests/test_detection.py

import cv2
from core.detection import ThreatDetector

def test_yolo_detection(image_path="models/test_image.jpg"):
    detector = ThreatDetector(model_path="models/yolov8n.pt")

    image = cv2.imread(image_path)
    if image is None:
        print("[ERROR] Test image not found.")
        return

    threats = detector.detect_threats(image)
    print(f"[INFO] Detected {len(threats)} threats.")

    for threat in threats:
        print(f" - Label: {threat['label']}, Confidence: {threat['confidence']:.2f}, BBox: {threat['bbox']}")

if __name__ == "__main__":
    test_yolo_detection()
