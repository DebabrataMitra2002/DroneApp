# gui/main_window.py

import tkinter as tk
from gui.map_widget import MapWidget
from gui.video_stream import VideoStream
from gui.widgets import ControlPanel
from core.detection import ThreatDetector
from core.landing_logic import LandingManager
from core.logger import Logger
from core.drone_api import DroneController
from utils.altitude_utils import get_altitude

def run_main_app():
    root = tk.Tk()
    root.title("Drone Safety Landing App")
    root.geometry("1200x700")

    # Init core components
    logger = Logger()
    drone = DroneController()
    detector = ThreatDetector()
    manager = LandingManager(drone, logger)

    # Map and video
    map_widget = MapWidget(root)
    map_widget.pack(side="left", fill="both", expand=True)

    video_stream = VideoStream(
        root,
        detector=detector,
        on_threats_detected=lambda threats: manager.evaluate_landing(threats, get_altitude(drone))
    )
    video_stream.pack(side="top", fill="both", expand=True)

    # Controls
    control_panel = ControlPanel(root, manager)
    control_panel.pack(side="bottom", fill="x")

    root.mainloop()
