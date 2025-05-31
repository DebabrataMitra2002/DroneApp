# core/landing_logic.py

from core.drone_api import DroneController
from core.logger import Logger
import time

class LandingManager:
    def __init__(self, drone: DroneController, logger: Logger):
        self.drone = drone
        self.logger = logger
        self.safe_threshold = 0  # No threat = safe

    def evaluate_landing(self, threats: list, altitude: float):
        if altitude > 10:
            return  # Safety logic only near ground

        if len(threats) > self.safe_threshold:
            self.logger.log_action(altitude, "Auto RTL: Unsafe Landing Zone")
            self.drone.auto_rtl()
        else:
            self.logger.log_action(altitude, "Safe Landing In Progress")
            self.drone.continue_landing()

    def force_land(self):
        self.logger.log_action(self.drone.get_altitude(), "Force Land Activated")
        self.drone.force_land()

    def hold_loiter(self):
        self.logger.log_action(self.drone.get_altitude(), "Loiter Mode")
        self.drone.set_loiter()
