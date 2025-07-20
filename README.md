# 6-DOF Voice-Controlled Robotic Arm with Vision Integration

![Logo](./6DOF-Banner(1)(1).png)

A highly interactive 6-DOF robotic arm controlled via voice commands and enhanced with object detection using a camera and YOLOv8. This project integrates speech recognition, computer vision, and robotic control using Raspberry Pi 5 and Python, aiming to create a smart and intuitive robotic system for real-world tasks.

## ✨ Features

🗣️ **Voice Command Integration**  
- Uses Vosk for offline speech recognition.  
- Custom command parsing: `"pick up red and put over blue"`, `"rotate red 90 degrees"`, `"place red parallel to blue"`, and more.

📷 **Live Camera Preview**  
- Real-time video feed using `cv2.imshow()` to monitor object positions and arm movements.  
- Runs on a separate thread to avoid blocking other operations.

🧠 **YOLOv8 Object Detection**  
- Detects and localizes colored cubes (e.g., red, blue) using YOLOv8 and OpenCV.  
- Extracts object positions to guide arm movements intelligently.

🎯 **Smooth & Precise Servo Control**  
- Controlled via `adafruit_servokit`, ensuring smooth transitions for all 6 joints.  
- Movement functions are incremental and smooth for precise control.

💾 **Motion Presets with JSON Config**  
- Save and load custom arm positions using `"save preset <name>"` and `"load preset <name>"` voice commands.  
- All presets are saved in a `config.json` file for persistence.

🛑 **Pause & Resume (Safety Override)**  
- Voice-controlled `"stop"` and `"resume"` commands to pause/resume all arm actions.  
- Prevents unexpected movements for safety and debugging.

🧵 **Multithreaded Design**  
- Camera feed, servo control, and voice recognition run concurrently using Python threads.

🔊 **Text-to-Speech Feedback**  
- The system speaks back using `pyttsx3`, confirming commands and task status for full interactivity.

---
## 🧠 System Requirements

- Raspberry Pi 5 (or any Linux-capable SBC with GPIO)
- Python 3.7+
- USB Camera
- Microphone
- 6-DOF Robotic Arm (PWM-compatible servos)

---

## 🧩 3D Printed Robotic Arm Model

You can download the STL file for the robotic arm design below:

[🧩 Download 3D Model (.stl)](Robotic%20Arm%203D%20Model%20v4.stl)

This model can be 3D printed and assembled for use with the Raspberry Pi-controlled voice-command system.

---

## 🛠️ Setup Instructions

1. **Clone the Repository**
    ```bash
    git clone https://github.com/M4YH3M-DEV/6-DOF-Voice-Controlled-Robotic-Arm.git
    cd 6-DOF-Voice-Controlled-Robotic-Arm
    ```

2. **Install Dependencies**
    ```bash
    sudo apt-get update
    sudo apt-get install python3-pyaudio python3-pip portaudio19-dev espeak
    pip3 install -r requirements.txt
    ```

3. **Download Vosk Model**
    ```bash
    wget https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
    unzip vosk-model-small-en-us-0.15.zip
    ```

4. **Run the Project**
    ```bash
    python3 main.py
    ```

---

## 🔤 Supported Voice Commands

| Command Example                             | Action                       |
|--------------------------------------------|------------------------------|
| `"pick up red and put over blue"`          | Pick and place cubes         |
| `"rotate red 90 degrees"`                  | Rotate a detected cube       |
| `"place red parallel to blue"`             | Align cubes side-by-side     |
| `"save preset <name>"`                     | Save current position        |
| `"load preset <name>"`                     | Load saved position          |
| `"stop"`                                   | Pause arm operations         |
| `"resume"`                                 | Resume arm operations        |
| `"exit"`                                   | Shutdown the system          |

---

## 📁 File Structure

6-DOF-Voice-Controlled-Robotic-Arm/

├── config.json                   # Preset storage

├── vosk-model-small-en-us-0.15/ # Vosk voice recognition model

├── main.py                      # Core logic and loop

├── requirements.txt             # Python dependencies

└── README.md                    # You're reading it!

---

## 📦 Dependencies

- `vosk`, `pyaudio`, `pyttsx3` – Voice recognition & TTS  
- `ultralytics` – YOLOv8 object detection  
- `opencv-python` – Camera input & processing  
- `adafruit-circuitpython-servokit` – Servo control  
- `RPi.GPIO` – Raspberry Pi GPIO handling  

---

## 🧪 Coming Soon

- Hand gesture control integration  
- Dynamic environment calibration  
- Autonomous operation mode (no voice needed)  
- Mobile app for manual override

---

## 👨‍💻 Author

Made with 💡 && 🧠 by [M4YH3M-DEV](https://github.com/M4YH3M-DEV)

---

## 📜 License

Licensed under the [Apache License 2.0](LICENSE).
