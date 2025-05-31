# core/logger.py

import csv
import os
from datetime import datetime

class Logger:
    def __init__(self, log_dir="logs"):
        os.makedirs(log_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.log_path = os.path.join(log_dir, f"flight_log_{timestamp}.csv")

        with open(self.log_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Altitude", "Action"])

    def log_action(self, altitude: float, action: str):
        timestamp = datetime.now().isoformat()
        with open(self.log_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, altitude, action])
