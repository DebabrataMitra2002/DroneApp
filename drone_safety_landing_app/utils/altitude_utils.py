# utils/altitude_utils.py

def get_altitude(drone):
    try:
        return drone.get_altitude()
    except Exception as e:
        print(f"[Altitude Error] {e}")
        return 0.0  # Safe fallback
