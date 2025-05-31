# core/drone_api.py

from dronekit import connect, VehicleMode

class DroneController:
    def __init__(self, connection_string="/dev/ttyAMA0", baud=57600):
        print("Connecting to drone...")
        self.vehicle = connect(connection_string, wait_ready=True, baud=baud)

    def get_altitude(self):
        return self.vehicle.location.global_relative_frame.alt

    def auto_rtl(self):
        self.vehicle.mode = VehicleMode("RTL")

    def force_land(self):
        self.vehicle.mode = VehicleMode("LAND")

    def continue_landing(self):
        # Placeholder: descending by 1m or keeping LAND
        self.vehicle.mode = VehicleMode("LAND")

    def set_loiter(self):
        self.vehicle.mode = VehicleMode("LOITER")
