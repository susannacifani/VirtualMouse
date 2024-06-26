# Webcam-Based Mouse Control

## Overview
This project implements a webcam-based mouse control system using computer vision techniques. The system tracks hand movements captured by the webcam and translates them into mouse movements on the screen. It allows users to interact with the computer without the need for a physical mouse.

## Features
- Real-time hand tracking: The system detects and tracks hand movements in real-time using computer vision algorithms.
- Mouse control: Hand movements are translated into mouse movements, allowing users to control the mouse cursor on the screen.
- Click and drag: Users can perform mouse clicks and drag operations using hand gestures.

## Requirements
- Python 3.8
- OpenCV
- Mediapipe
- Autopy

## Installation
1. Clone the repository to your local machine.
2. Install Python 3.8 if you haven't already.
3. Install the required dependencies using pip:  
      pip install opencv-python   
      pip install mediapipe  
4. Run the main script using Python:  
      python VirtualMouse.py  
6. Position your hand in front of the webcam. The system will track your hand movements and translate them into mouse movements on the screen.
7. Perform gestures to control the mouse cursor, click, and drag as needed.

## Hand Gestures
- Move: move the pointer by raising your index and middle fingers.
![move](https://github.com/susannacifani/VirtualMouse/assets/73530772/d2fd7405-3a7e-4495-982e-c80a8c435b23)

- Click: perform a click by quickly bringing your index and middle fingers together, and then immediately separating them.
![click](https://github.com/susannacifani/VirtualMouse/assets/73530772/06b3cf38-c840-421a-9401-90f70d345d1f)

  
- Drag and Drop: perform drag and drop actions by raising your index finger (drag) and then lowering it again (to drop).
![drag](https://github.com/susannacifani/VirtualMouse/assets/73530772/7044a8d9-4082-4972-9fd8-8fa3dccd6dc2)


