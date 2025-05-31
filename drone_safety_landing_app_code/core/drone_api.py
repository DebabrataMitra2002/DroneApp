from dronekit import connect, VehicleMode

class DroneAPI:
    def __init__(self, connection_str):
        self.vehicle = connect(connection_str, wait_ready=True)

    def get_altitude(self):
        return self.vehicle.location.global_relative_frame.alt

    def set_mode(self, mode):
        self.vehicle.mode = VehicleMode(mode)

    def arm(self):
        self.vehicle.armed = True

    def disarm(self):
        self.vehicle.armed = False

    def is_armed(self):
        return self.vehicle.armed

    def land(self):
        self.set_mode("LAND")

    def rtl(self):
        self.set_mode("RTL")

    def loiter(self):
        self.set_mode("LOITER")