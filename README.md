# 🛸 Drone Safety Landing System

An intelligent drone landing system that analyzes real-time aerial footage to detect landing threats such as trees, water, or uneven terrain. It uses YOLOv8 object detection and triggers smart decisions like **Auto RTL**, **Loiter**, or **Force Land**, ensuring maximum landing safety.

---

## 📸 Key Features

- 🔍 Real-time camera feed with YOLO-based aerial threat detection
- 📉 Safety logic triggers only below 10m altitude
- 🧠 Auto-RTL if all zones are unsafe
- 🕹️ Manual override buttons:
  - Loiter
  - RTL
  - Force Land
- 🗺️ Integrated MapView using `tkintermapview`
- 📁 Threat and altitude logging to CSV
- 📦 Packaged as a portable `.AppImage` for Raspberry Pi 5

---

## 🧑‍💻 Demo

![Drone Safety App UI Screenshot](screenshot.png)

---

## 🚀 How to Run (Raspberry Pi 5)

### Step 1: Install Dependencies

```bash
sudo apt update
sudo apt install python3-opencv libatlas-base-dev libopenblas-dev libhdf5-dev
pip install ultralytics opencv-python pillow dronekit tkintermapview
```

> ✅ Recommended: Use YOLOv8n (nano) model for best performance on Raspberry Pi

---

### Step 2: Launch the App

```bash
python3 main.py
```

OR use the `.AppImage`:

```bash
chmod +x DroneSafeLanding.AppImage
./DroneSafeLanding.AppImage
```

---

## ⚙️ Build AppImage (Optional)

To create a `.AppImage` from source:

```bash
sudo apt install appimagetool pyinstaller
pyinstaller --onefile main.py --distpath AppDir/usr/bin
cd DroneSafeApp
appimagetool AppDir
```

---

## 🧾 CSV Logging

The app logs the following to `log.csv`:
- Altitude
- Threat type detected
- Decision taken (RTL / Force Land / Loiter)

---

## 🧠 Threat Detection Classes

Custom YOLO model trained to detect:
- 🌳 Trees
- 🌊 Water bodies
- ⚠️ Uneven or rocky land

> Want to train your own YOLO model? See: [`model_training.md`](model_training.md)

---

## 🛡️ Safety Enhancements

- Disables **Force Land** above 10m altitude
- Visual **altitude indicator** on-screen
- Smart decisions based on detected threat density

---

## 🧱 Tech Stack

- Python 3
- OpenCV
- Ultralytics YOLOv8
- Tkinter GUI + MapView
- DroneKit-Python
- AppImage (for packaging)

---

## 📂 Folder Structure

```
DroneSafeLanding/
├── main.py
├── model.pt
├── map_module.py
├── detection_module.py
├── controller.py
├── assets/
│   └── drone.png
├── log.csv
├── AppDir/
│   ├── AppRun
│   ├── drone.desktop
│   └── usr/bin/
│       └── run.sh
```

---

## 🙋 Author

**Debabrata Mitra**  
📧 debabratajv2019@gmail.com  
🔗 [GitHub @DebabrataMitra2002](https://github.com/DebabrataMitra2002)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
