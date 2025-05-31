import tkinter as tk
from core.landing_logic import handle_safe_landing
from core.drone_api import send_rtl_command, send_loiter_command, force_land

class ControlButtons:
    def __init__(self, frame, main_window):
        self.frame = frame

        self.btn_land = tk.Button(frame, text="Force Land", command=force_land, bg="red", fg="white")
        self.btn_land.pack(side="left", padx=10)

        self.btn_rtl = tk.Button(frame, text="RTL", command=send_rtl_command)
        self.btn_rtl.pack(side="left", padx=10)

        self.btn_loiter = tk.Button(frame, text="Loiter", command=send_loiter_command)
        self.btn_loiter.pack(side="left", padx=10)

        self.btn_detect = tk.Button(frame, text="Detect Threats", command=handle_safe_landing)
        self.btn_detect.pack(side="left", padx=10)