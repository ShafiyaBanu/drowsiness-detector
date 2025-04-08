from flask import Flask, render_template
import subprocess
import threading

app = Flask(__name__)

process = None  # Variable to store the process reference

def start_detection():
    global process
    # Run the drowsiness detection script
    process = subprocess.Popen(["python", "drowsiness_yawn.py"])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start', methods=['GET'])
def start():
    threading.Thread(target=start_detection).start()
    return 'Detection started'

@app.route('/stop', methods=['GET'])
def stop():
    global process
    if process:
        process.terminate()  # Stop the Python script
        process = None
    return 'Detection stopped'

if __name__ == '__main__':
    app.run(debug=True)
