# Traffic Signal Controller with Hand Gestures

A Python-based traffic signal controller system using hand gesture recognition powered by OpenCV and MediaPipe. This project detects hand gestures to dynamically control traffic signals for "Stop," "Go," and "Slow."

---

## Features
- Real-time hand gesture recognition using a webcam.
- Visual feedback on the screen for detected gestures.
- Control of Arduino-connected LEDs for traffic light simulation.
- Works with any standard webcam.

---

## How It Works
1. Detects hand gestures inside a predefined rectangle on the screen.
2. Based on the number of raised fingers:
   - **0 Fingers:** "Slow"
   - **1 Finger:** "Go"
   - **5 Fingers:** "Stop"
3. Optionally integrates with Arduino to physically simulate traffic signals.

---

## Modules Used
| Module         | Description                                                                                   | Link to Install                                                                 |
|----------------|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| `opencv-python`| Library for real-time computer vision.                                                        | [OpenCV](https://pypi.org/project/opencv-python/)                               |
| `mediapipe`    | Framework for building multimodal (e.g., face, hand) perception pipelines.                    | [MediaPipe](https://pypi.org/project/mediapipe/)                                |
| `trafficcontrol`| Custom module for Arduino LED integration (if applicable).                                   | **Local File** (Write and include the script `trafficcontrol.py`)               |

---

## Setup and Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/Traffic-Signal-Controller.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Traffic-Signal-Controller
    ```
3. Install the required modules:
    ```bash
    pip install opencv-python mediapipe
    ```
4. Connect your Arduino (optional) and ensure the `trafficcontrol.py` script is properly set up.

---

## Usage
1. Run the script:
    ```bash
    python traffic_signal_controller.py
    ```
2. Use your hand gestures to control the traffic signals:
   - Place your hand inside the green rectangle.
   - Raise fingers to signal "Stop," "Go," or "Slow."

---

## Author
Sam  
- [GitHub Profile](https://github.com/Abraham-Samuel470)

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments
- **OpenCV**: For enabling real-time computer vision.
- **MediaPipe**: For providing hand detection and gesture recognition capabilities.
