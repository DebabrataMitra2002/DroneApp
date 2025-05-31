# gui/video_stream.py

import tkinter as tk
from PIL import Image, ImageTk
import cv2
import threading

class VideoStream(tk.Label):
    def __init__(self, parent, detector, on_threats_detected, camera_index=0):
        super().__init__(parent)
        self.parent = parent
        self.detector = detector
        self.on_threats_detected = on_threats_detected
        self.cap = cv2.VideoCapture(camera_index)

        self.running = True
        self.update_thread = threading.Thread(target=self.update_frame, daemon=True)
        self.update_thread.start()

    def update_frame(self):
        while self.running:
            ret, frame = self.cap.read()
            if not ret:
                continue

            # Run threat detection
            threats = self.detector.detect_threats(frame)
            self.on_threats_detected(threats)

            # Draw boxes
            for t in threats:
                x1, y1, x2, y2 = t["bbox"]
                label = t["label"]
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                cv2.putText(frame, label, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

            # Convert to Tkinter-compatible image
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(rgb_frame)
            imgtk = ImageTk.PhotoImage(image=img)
            self.imgtk = imgtk
            self.config(image=self.imgtk)

    def stop(self):
        self.running = False
        self.cap.release()
