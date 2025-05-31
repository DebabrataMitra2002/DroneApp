import csv
from datetime import datetime

def initialize_csv(file_path):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Altitude", "Action", "Threat_Level"])

def log_data(file_path, altitude, action, threat_level):
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            altitude,
            action,
            threat_level
        ])