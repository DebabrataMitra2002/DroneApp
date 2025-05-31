def is_below_altitude_threshold(current_altitude, threshold=10):
    """
    Checks if the drone is below a given altitude (in meters).
    """
    return current_altitude <= threshold