# 6-DOF Voice-Controlled Robotic Arm with Vision Integration

A highly interactive 6-DOF robotic arm controlled via voice commands and enhanced with object detection using a camera and YOLOv8. This project integrates speech recognition, computer vision, and robotic control using Raspberry Pi 5 and Python, aiming to create a smart and intuitive robotic system for real-world tasks.

## ✨ Features

- 🔊 **Voice-Controlled Interface**: Control the robotic arm using natural language voice commands (via Google Speech Recognition).
- 🧠 **AI-Powered Object Detection**: YOLOv8 integration for real-time object detection and tracking using a camera.
- 🦾 **6 Degrees of Freedom**: Precision control over each servo for complex and accurate movement.
- 🎮 **Manual Control Mode**: Use a keyboard input or physical joystick to manually control each joint.
- 🔁 **Autonomous Mode**: Automatically detect, target, and interact with objects based on pre-defined behaviors.
- 📷 **Camera Integration**: Visual feedback and object localization using a Pi Camera or USB webcam.
- 🌐 **Modular Architecture**: Easily expandable to include additional AI models, gesture control, or remote access.
- 💾 **Persistent Configs**: Save and load motion presets, positions, and sequences for repeatability.

## 🧰 Tech Stack

- **Hardware**: Raspberry Pi 5, 6 servo motors, camera module, mic
- **Languages**: Python 3
- **Libraries**:
  - `RPi.GPIO`, `time`, `speech_recognition`, `ultralytics`, `cv2` (OpenCV), `pyttsx3`, etc.
- **AI Models**: YOLOv8 for object detection

## 🛠️ Setup

1. Clone the repository
2. Install required Python packages
3. Connect the servo motors and camera
4. Run the main Python script to start the system

## 📜 License

Licensed under the [Apache License 2.0](LICENSE).
