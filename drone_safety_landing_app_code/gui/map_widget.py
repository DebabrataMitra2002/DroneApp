import tkintermapview

class MapWidget:
    def __init__(self, frame):
        self.map_widget = tkintermapview.TkinterMapView(frame, width=640, height=480)
        self.map_widget.set_position(22.5726, 88.3639)  # Default to Kolkata
        self.map_widget.set_zoom(15)
        self.map_widget.pack()