import cv2
import threading
import tkinter as tk
from PIL import Image, ImageTk

class VideoStream:
    def __init__(self, frame):
        self.cap = cv2.VideoCapture(0)
        self.label = tk.Label(frame)
        self.label.pack()
        self.running = True
        threading.Thread(target=self.update, daemon=True).start()

    def update(self):
        while self.running:
            ret, frame = self.cap.read()
            if ret:
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image = ImageTk.PhotoImage(Image.fromarray(image))
                self.label.config(image=image)
                self.label.image = image
