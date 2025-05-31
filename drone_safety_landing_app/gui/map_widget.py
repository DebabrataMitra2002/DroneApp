# gui/map_widget.py

import tkinter as tk
from tkintermapview import TkinterMapView

class MapWidget(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.map_view = TkinterMapView(self, width=600, height=700, corner_radius=0)
        self.map_view.pack(fill="both", expand=True)

        # Default location (can be overridden by drone GPS later)
        self.map_view.set_position(37.7749, -122.4194)  # San Francisco
        self.marker = None

    def update_location(self, lat, lon):
        if self.marker:
            self.marker.set_position(lat, lon)
        else:
            self.marker = self.map_view.set_marker(lat, lon, text="Drone")

        self.map_view.set_position(lat, lon)
