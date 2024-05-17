import os, sys
from flask_cors import CORS
from flask import Flask, Response

path_this = os.path.abspath(os.path.dirname(__file__))
path_engine = os.path.join(path_this, "..")
sys.path.append(path_this)
sys.path.append(path_engine)

from src.detector import ObjectDetector

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return Response('Object Detector', mimetype='text/plain')

@app.route('/detect')
def detect():
    return Response(detector.detect_objects(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/get_queue')
def get_queue():
    return {"object": detector.q.get()}

if __name__ == '__main__':
    model_path = "yolov8m.pt"
    class_names = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
                   "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
                   "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
                   "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
                   "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
                   "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
                   "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
                   "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
                   "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
                   "teddy bear", "hair drier", "toothbrush"]

    detector = ObjectDetector(model_path, class_names)
    detector.detect_objects()
    app.run(port=1121)