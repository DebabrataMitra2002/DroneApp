<<<<<<< HEAD
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
=======
To create a ready-made .AppImage build script for your drone safety landing application on a Raspberry Pi 5, we can set up an automated process. However, creating a native AppImage on the Raspberry Pi involves using a different architecture (ARM64), and the standard AppImage tool may not be directly available for ARM devices.

Here’s the process to create a .AppImage for Raspberry Pi 5:
Step 1: Install Necessary Tools
First, install the necessary tools:

bash
Copy code
sudo apt update
sudo apt install python3-pip python3-venv libatlas-base-dev libopenblas-dev libhdf5-dev appimagetool
You will also need PyInstaller for bundling your Python app into an executable:

bash
Copy code
pip install pyinstaller
Step 2: Set Up Your Project Directory
Here’s a basic directory structure for your drone safety landing application:

bash
Copy code
DroneSafeApp/
├── AppDir/
│   ├── usr/
│   │   ├── bin/
│   │   │   └── run.sh
│   │   └── lib/
│   └── AppRun
│   └── drone.png
│   └── drone.desktop
├── main.py
└── requirements.txt
Step 3: Create run.sh
Inside AppDir/usr/bin/run.sh, create a script to launch the app:

bash
Copy code
#!/bin/bash
cd "$(dirname "$0")"
python3 ../../../../main.py
Make it executable:

bash
Copy code
chmod +x DroneSafeApp/AppDir/usr/bin/run.sh
Step 4: Create AppRun
Inside AppDir/AppRun, create the following script:

bash
Copy code
#!/bin/bash
exec ./usr/bin/run.sh
Make it executable:

bash
Copy code
chmod +x DroneSafeApp/AppDir/AppRun
Step 5: Create .desktop File
Inside AppDir, create the drone.desktop file:

ini
Copy code
[Desktop Entry]
Type=Application
Name=Drone Safe Landing
Exec=run.sh
Icon=drone
Categories=Utility;
Place a drone.png image as your app icon in the AppDir folder.

Step 6: Bundle Python and Dependencies
Use PyInstaller to bundle your Python app and dependencies. Run the following command:

bash
Copy code
pyinstaller --onefile --distpath DroneSafeApp/AppDir/usr/bin main.py
This will create a bundled .bin executable for the app inside the usr/bin folder.

Step 7: Build AppImage
Navigate to your DroneSafeApp directory and run the following command to create your AppImage:

bash
Copy code
cd DroneSafeApp
appimagetool AppDir
This will generate a .AppImage file (e.g., DroneSafeLanding-x86_64.AppImage), which is a single executable file that can be run on a Raspberry Pi 5.

Step 8: Test the .AppImage
Once the .AppImage is created, you can test it:

bash
Copy code
chmod +x DroneSafeLanding-x86_64.AppImage
./DroneSafeLanding-x86_64.AppImage
This will launch the drone landing safety app with live camera feed and all functionality.

🌟 Summary:
The script bundles your Python app into an AppImage that can be executed directly on Raspberry Pi 5.

You can launch the application by clicking the .AppImage file.

If you're developing for ARM architecture, ensure the libraries and dependencies are ARM-compatible.
>>>>>>> 56b347ac5103c93db63c9e34f92339979237ca15
