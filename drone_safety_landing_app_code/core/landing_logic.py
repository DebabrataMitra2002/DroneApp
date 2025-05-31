import time

class LandingLogic:
    def __init__(self, drone_api, detector, logger):
        self.drone_api = drone_api
        self.detector = detector
        self.logger = logger

    def evaluate_landing_spot(self, frame, altitude):
        detections = self.detector.detect_threats(frame)
        threats = ['tree', 'person', 'water', 'rock']
        is_threat = any(d['name'] in threats and d['confidence'] > 0.5 for _, d in detections.iterrows())
        action = "Land" if not is_threat else "Auto RTL"
        self.logger.log_decision(altitude, action, len(detections))
        return action
