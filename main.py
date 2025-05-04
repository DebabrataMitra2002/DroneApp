import cv2
import csv
import threading
from datetime import datetime
from tkinter import *
from PIL import Image, ImageTk
from ultralytics import YOLO
from dronekit import connect, VehicleMode
from tkintermapview import TkinterMapView

# Constants
SAFE_THRESHOLD = 10
UNSAFE_FRAME_LIMIT = 5
LOG_FILE = "threat_log.csv"

# Connect to drone
vehicle = connect('udp:127.0.0.1:14550', wait_ready=True)

# Load model
model = YOLO("models/best.pt")

class DroneSafeLandingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Drone Smart Landing System")

        self.unsafe_counter = 0

        # GUI Layout
        self.video_label = Label(root)
        self.video_label.pack()

        self.threat_label = Label(root, text="Threat Score: 0", font=("Arial", 14))
        self.threat_label.pack()

        self.altitude_label = Label(root, text="Altitude: -- m", font=("Arial", 14))
        self.altitude_label.pack()

        self.status_label = Label(root, text="Status: Monitoring", font=("Arial", 14), fg="blue")
        self.status_label.pack()

        # Buttons
        self.landing_btn = Button(root, text="Force Land", command=self.force_land, bg="red", fg="white")
        self.landing_btn.pack(pady=5)

        self.rtl_btn = Button(root, text="Return to Launch", command=self.return_to_launch, bg="blue", fg="white")
        self.rtl_btn.pack(pady=5)

        self.loiter_btn = Button(root, text="Loiter", command=self.loiter_mode, bg="orange", fg="white")
        self.loiter_btn.pack(pady=5)

        # Map View
        self.map_widget = TkinterMapView(root, width=600, height=400, corner_radius=0)
        self.map_widget.set_zoom(17)
        self.map_widget.pack()

        # Video
        self.capture = cv2.VideoCapture(0)
        self.update_video()

        self.init_log()

    def update_video(self):
        ret, frame = self.capture.read()
        if ret:
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(rgb)
            imgtk = ImageTk.PhotoImage(image=img)
            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)

            threading.Thread(target=self.process_frame, args=(frame.copy(),)).start()
        self.root.after(100, self.update_video)

    def process_frame(self, frame):
        try:
            alt = vehicle.location.global_relative_frame.alt
            self.altitude_label.config(text=f"Altitude: {alt:.2f} m")

            # Disable "Force Land" if altitude > 10
            if alt > 10:
                self.landing_btn.config(state=DISABLED)
                self.status_label.config(text=f"Altitude > 10m - Awaiting descent", fg="blue")
                return
            else:
                self.landing_btn.config(state=NORMAL)
        except:
            alt = -1
            self.altitude_label.config(text=f"Altitude: -- m")

        results = model(frame)
        boxes = results[0].boxes
        class_names = [results[0].names[int(cls)] for cls in boxes.cls]

        threat_score = self.calculate_score(class_names)
        self.threat_label.config(text=f"Threat Score: {threat_score}")

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        action = "Monitoring"

        if threat_score < SAFE_THRESHOLD:
            self.unsafe_counter = 0
            self.status_label.config(text="Status: Safe - Landing", fg="green")
            vehicle.mode = VehicleMode("LAND")
            action = "LAND"
        else:
            self.unsafe_counter += 1
            self.status_label.config(text=f"Status: Unsafe ({self.unsafe_counter})", fg="red")

            if self.unsafe_counter >= UNSAFE_FRAME_LIMIT:
                self.status_label.config(text="Status: Auto RTL", fg="orange")
                vehicle.mode = VehicleMode("RTL")
                action = "AUTO_RTL"
                self.unsafe_counter = 0

        self.log_data(now, class_names, threat_score, alt, action)
        self.update_map()

    def calculate_score(self, objects):
        weights = {
            'person': 10, 'car': 8, 'dog': 5,
            'tree': 7, 'water': 9, 'rock': 6, 'uneven': 6
        }
        return sum(weights.get(obj, 0) for obj in objects)

    def init_log(self):
        with open(LOG_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Timestamp", "Objects Detected", "Threat Score", "Altitude (m)", "Action"])

    def log_data(self, time, objects, score, alt, action):
        with open(LOG_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([time, ", ".join(objects), score, f"{alt:.2f}", action])

    def update_map(self):
        try:
            lat = vehicle.location.global_frame.lat
            lon = vehicle.location.global_frame.lon
            self.map_widget.set_position(lat, lon)
            self.map_widget.set_marker(lat, lon, text="Drone")
        except:
            pass

    def force_land(self):
        vehicle.mode = VehicleMode("LAND")
        self.status_label.config(text="Status: Forced Landing", fg="purple")
        self.log_data(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), [], 0, vehicle.location.global_relative_frame.alt, "FORCE_LAND")

    def return_to_launch(self):
        vehicle.mode = VehicleMode("RTL")
        self.status_label.config(text="Status: Manual RTL", fg="orange")
        self.log_data(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), [], 0, vehicle.location.global_relative_frame.alt, "MANUAL_RTL")

    def loiter_mode(self):
        vehicle.mode = VehicleMode("LOITER")
        self.status_label.config(text="Status: Loiter Mode", fg="orange")
        self.log_data(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), [], 0, vehicle.location.global_relative_frame.alt, "LOITER")

# Launch app
if __name__ == "__main__":
    root = Tk()
    app = DroneSafeLandingApp(root)
    root.mainloop()
