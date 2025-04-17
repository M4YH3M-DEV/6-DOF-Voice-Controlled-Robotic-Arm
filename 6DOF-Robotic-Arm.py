import time
import pyaudio
import json
import vosk
import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit
from ultralytics import YOLO
import cv2
import pyttsx3

# Debug Mode Toggle
DEBUG_MODE = True

# ServoKit Setup
kit = ServoKit(channels=16)

# Servo Pin Assignments
BASE_SERVO = 0
LIFT_SERVO = 1
CLENCH_SERVO = 2
WRIST_SERVO = 3
WRIST_ROTATE_SERVO = 4

# GPIO Setup
GPIO.setmode(GPIO.BCM)

# Vosk Voice Recognition Setup
model_path = "vosk-model-small-en-us-0.15"
samplerate = 16000
chunk_size = 1024
vosk_model = vosk.Model(model_path)
rec = vosk.KaldiRecognizer(vosk_model, samplerate)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=samplerate, input=True, frames_per_buffer=chunk_size)
stream.start_stream()

# TTS Engine Setup
engine = pyttsx3.init()

def speak(message):
    engine.say(message)
    engine.runAndWait()

# Debug Function
def debug_log(message):
    if DEBUG_MODE:
        print(f"[DEBUG] {message}")

# Smooth Servo Movement
def smooth_move(servo_index, target_angle, delay=0.01):
    current_angle = kit.servo[servo_index].angle or 90
    step = 1 if target_angle > current_angle else -1
    for angle in range(int(current_angle), int(target_angle) + step, step):
        kit.servo[servo_index].angle = angle
        time.sleep(delay)

# Move Arm Function
def move_arm(base_angle, lift_angle, wrist_angle, wrist_rotate_angle, clench_angle):
    smooth_move(BASE_SERVO, base_angle)
    smooth_move(LIFT_SERVO, lift_angle)
    smooth_move(WRIST_SERVO, wrist_angle)
    smooth_move(WRIST_ROTATE_SERVO, wrist_rotate_angle)
    smooth_move(CLENCH_SERVO, clench_angle)
    debug_log(f"Moving Arm -> Base: {base_angle}, Lift: {lift_angle}, Wrist: {wrist_angle}, Wrist Rotate: {wrist_rotate_angle}, Clench: {clench_angle}")

# Voice Command Function
def get_command():
    debug_log("Listening for command...")
    while True:
        data = stream.read(chunk_size)
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            command = result.get("text", "").lower()
            debug_log(f"Detected Command: {command}")
            return command

# Command Parsing
def parse_command(text):
    COMMANDS = {
        "pick up {color1} and put over {color2}": "pick_place",
        "rotate {color} 90 degrees": "rotate",
        "place {color1} parallel to {color2}": "parallel",
    }
    for template, action in COMMANDS.items():
        words = template.replace("{color1}", "").replace("{color2}", "").replace("{color}", "").split()
        if all(word in text for word in words):
            for color1 in ["red", "blue"]:
                for color2 in ["red", "blue"]:
                    if color1 in text and color2 in text and color1 != color2:
                        return action, {"color1": color1, "color2": color2}
            if "red" in text or "blue" in text:
                color = "red" if "red" in text else "blue"
                return action, {"color": color}
    return None, {}

# YOLO Object Detection
model = YOLO("yolov8n.pt")
cap = cv2.VideoCapture(0)

def detect_cubes():
    ret, frame = cap.read()
    results = model(frame)
    cubes = {}
    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            label = model.names[cls]
            x1, y1, x2, y2 = box.xyxy[0]
            center = ((x1 + x2) // 2, (y1 + y2) // 2)
            cubes[label] = center
    debug_log(f"Detected Cubes: {cubes}")
    return cubes

# Main Loop
while True:
    command = get_command()
    action, params = parse_command(command)

    if not action:
        speak("Sorry, I didn't understand.")
        continue

    speak(f"Executing {action} for {params}")
    cubes = detect_cubes()

    if action == "pick_place":
        move_arm(90, 60, 30, 0, 0)
        time.sleep(1)
        move_arm(90, 60, 30, 0, 30)
        time.sleep(1)
        move_arm(120, 30, 0, 0, 30)
        time.sleep(1)
        move_arm(120, 30, 0, 0, 0)
        speak("Task Completed")

    elif action == "parallel":
        move_arm(90, 50, 20, 0, 30)
        time.sleep(1)
        move_arm(90, 50, 20, 0, 0)
        speak("Cubes placed parallel")

    elif action == "rotate":
        move_arm(90, 60, 30, 0, 30)
        time.sleep(1)
        move_arm(90, 60, 30, 90, 30)
        time.sleep(1)
        move_arm(90, 60, 30, 90, 0)
        speak("Rotation complete")

    elif "exit" in command:
        speak("Shutting down")
        break

# Cleanup
stream.stop_stream()
stream.close()
p.terminate()
GPIO.cleanup()
cap.release()

