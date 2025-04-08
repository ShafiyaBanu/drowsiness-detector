# drowsiness-detector
Drowsiness Detector is a Python-based computer vision project that monitors driver alertness in real time. Using OpenCV and Haar cascade classifiers, it tracks eye movements and triggers an alarm when signs of drowsiness are detected. The goal is to reduce road accidents caused by driver fatigue.

## Features

* Real-time face, eye, and mouth detection
* Detects drowsiness through prolonged eye closure
* Detects yawns using facial landmarks
* Triggers an alarm when drowsiness or yawning is detected
* Lightweight and simple interface

## Technologies Used

* Python 3
* OpenCV
* Dlib
* imutils
* Numpy

## Screenshots

### Eyes Open  
![Eyes Open](screenshots/open.png)

### Eyes Closed  
![Eyes Closed](screenshots/closed.png)

### Yawning  
![Yawning Detected](screenshots/yawn.png)

## Getting Started

1. Clone the repository:  
   `git clone https://github.com/YourUsername/Real-Time-Drowsiness-Detector.git`

2. Navigate into the folder:  
   `cd Real-Time-Drowsiness-Detector`

3. Install dependencies:  
   `pip install -r requirements.txt`

4. Run the application:  
   `python drowsiness_yawn.py`

> Make sure your webcam is connected.

## File Structure

* `drowsiness_yawn.py`: Main script to run the system  
* `shape_predictor_68_face_landmarks.dat`: Facial landmarks model  
* `Alert.wav`: Alarm sound  
* `requirements.txt`: Required Python libraries  
* `screenshots/`: Folder containing output snapshots

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Fork the repo and open a pull request.

## Author

**D. Shafiya Banu**

## Contact

For any questions or feedback, feel free to reach out via  
GitHub: [@ShafiyaBanu](https://github.com/ShafiyaBanu)
