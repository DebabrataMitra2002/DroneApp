import csv
from datetime import datetime

class CSVLogger:
    def __init__(self, filename="logs.csv"):
        self.filename = filename
        with open(self.filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Timestamp", "Altitude", "Action", "ThreatCount"])

    def log_decision(self, altitude, action, threat_count):
        with open(self.filename, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), altitude, action, threat_count])
