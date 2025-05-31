# utils/camera_utils.py

import cv2

def get_available_cameras(max_devices=5):
    available = []
    for i in range(max_devices):
        cap = cv2.VideoCapture(i)
        if cap.read()[0]:
            available.append(i)
        cap.release()
    return available

def capture_image(camera_index=0, filename="capture.jpg"):
    cap = cv2.VideoCapture(camera_index)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(filename, frame)
    cap.release()
