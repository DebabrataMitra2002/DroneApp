from ultralytics import YOLO

def export_dummy_model(output_path="models/best.pt"):
    # Use a pretrained tiny model as a dummy (YOLOv8n)
    model = YOLO("yolov8n.pt")  # Load small pretrained model
    model.export(format="pt")  # Export to PyTorch format

    # Copy to desired path
    import shutil
    shutil.move("yolov8n.pt", output_path)
    print(f"[INFO] Dummy model saved to: {output_path}")

if __name__ == "__main__":
    export_dummy_model()