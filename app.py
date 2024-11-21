from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import cv2
import json
from tensorflow.keras.models import load_model

with open('static/image_data.json', 'r', encoding='utf-8') as json_image:
    image_data = json.load(json_image)

app = Flask(__name__)

MODEL_IMAGE = load_model('models/79%.keras')

def preprocessing(file):
    file_bytes = np.frombuffer(file.read(), np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE)
    equalized_image = cv2.equalizeHist(image)
    resize_image = cv2.resize(equalized_image, (224, 224))
    resize_image = np.expand_dims(resize_image, axis=-1)
    resize_image = np.repeat(resize_image, 3, axis=-1)
    resize_image = np.expand_dims(resize_image, axis=0)
    return resize_image

@app.route('/')
def home():
    return 'Hello World!'

@app.route('/imagePrediction', methods=['PUT', 'POST'])
def predictFromImage():
    file = request.files['image']
    image = preprocessing(file)
    pred = MODEL_IMAGE.predict(image)
    pred = np.argmax(pred, axis=1)
    pred = int(pred)
    pred = image_data[pred]
    return jsonify(pred)

if __name__ == "__main__":
    app.run(debug=True)