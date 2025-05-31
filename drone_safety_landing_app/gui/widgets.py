# gui/widgets.py

import tkinter as tk

class ControlPanel(tk.Frame):
    def __init__(self, parent, landing_manager):
        super().__init__(parent)

        self.landing_manager = landing_manager

        self.force_land_btn = tk.Button(self, text="Force Land", bg="red", fg="white", command=self.landing_manager.force_land)
        self.force_land_btn.pack(side="left", padx=10, pady=10)

        self.rtl_btn = tk.Button(self, text="Return to Launch (RTL)", bg="orange", command=self.landing_manager.drone.auto_rtl)
        self.rtl_btn.pack(side="left", padx=10, pady=10)

        self.loiter_btn = tk.Button(self, text="Hold Loiter", bg="blue", fg="white", command=self.landing_manager.hold_loiter)
        self.loiter_btn.pack(side="left", padx=10, pady=10)
