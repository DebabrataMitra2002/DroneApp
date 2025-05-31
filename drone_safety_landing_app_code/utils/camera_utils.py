import cv2

def get_camera_stream(index=0):
    cap = cv2.VideoCapture(index)
    if not cap.isOpened():
        raise IOError("Cannot open camera")
    return cap

def read_frame(cap):
    ret, frame = cap.read()
    if not ret:
        return None
    return frame

def release_camera(cap):
    cap.release()
    cv2.destroyAllWindows()
