
# 🚀 Drone Safety Landing App Setup Guide (Raspberry Pi 5)

This guide walks you through setting up the Drone Safety Landing App on a **Raspberry Pi 5** step-by-step.

---

## 🧰 Prerequisites
- Raspberry Pi 5 with Raspberry Pi OS (64-bit recommended)
- Internet connection (WiFi or Ethernet)
- Camera module or USB webcam (optional but recommended)
- ZIP file: `drone_safety_landing_app.zip`

---

## ✅ Step 1: Update Raspberry Pi

```bash
sudo apt update && sudo apt upgrade -y
```

---

## ✅ Step 2: Install Required Packages

```bash
sudo apt install python3 python3-pip python3-venv -y
sudo apt install libatlas-base-dev libjpeg-dev zlib1g-dev                  libqtgui4 libqt4-test python3-tk ffmpeg unzip -y
```

---

## ✅ Step 3: Enable Camera (Optional)

```bash
sudo raspi-config
```

- Navigate to: **Interface Options > Camera > Enable**
- Then: `sudo reboot`

---

## ✅ Step 4: Unzip the Project

```bash
cd ~/Downloads  # Or wherever you saved the ZIP
unzip drone_safety_landing_app.zip
cd drone_safety_landing_app
```

---

## ✅ Step 5: Create and Activate Virtual Environment

```bash
python3 -m venv drone_env
source drone_env/bin/activate
```

---

## ✅ Step 6: Install Python Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## ✅ Step 7: Run the Application

```bash
python3 main.py
```

---

## 🛠️ (Optional) Step 8: Make AppImage Build Script Executable

```bash
chmod +x build_appimage.sh
./build_appimage.sh
```

---

## ✅ Done!
Your Drone Safety App is ready. Use it with live camera + threat detection + map view + drone actions.

Need help with boot on startup, MAVLink integration, or camera testing? Just ask!
