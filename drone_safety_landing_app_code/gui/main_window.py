import tkinter as tk
from gui.video_stream import VideoStream
from gui.map_widget import MapWidget
from gui.widgets import ControlButtons
from utils.altitude_utils import get_current_altitude

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Drone Safety Landing App")
        self.root.geometry("1280x720")

        self.video_frame = tk.Frame(self.root, width=640, height=480)
        self.video_frame.pack(side="left", padx=10, pady=10)
        self.video = VideoStream(self.video_frame)

        self.map_frame = tk.Frame(self.root, width=640, height=480)
        self.map_frame.pack(side="right", padx=10, pady=10)
        self.map = MapWidget(self.map_frame)

        self.controls_frame = tk.Frame(self.root)
        self.controls_frame.pack(side="bottom", fill="x", padx=10, pady=10)
        self.controls = ControlButtons(self.controls_frame, self)

        self.update_altitude()

    def update_altitude(self):
        altitude = get_current_altitude()
        self.root.title(f"Drone Safety Landing App - Altitude: {altitude:.2f}m")
        self.root.after(1000, self.update_altitude)


def launch_app():
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()