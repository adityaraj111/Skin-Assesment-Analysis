from __future__ import absolute_import, division, print_function, unicode_literals
import base64
import numpy as np
import io
import keras
from PIL import Image
from keras import backend as K
from keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array
from flask import request
from flask import jsonify
from flask import Flask

app = Flask(__name__)

def get_model():
    global model
    model = load_model('new_model.h5')
    print(" * Model loaded!")

def preprocess_image(image, target_size):
    if image.mode!="RGB":
        image = image.convert("RGB")
    image = image.resize(target_size)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    
    return image

print(" * Loading Keras model...")
get_model()


@app.route("/predict", methods=["POST"])
def predict():
    message = request.get_json(force=True)
    encoded = message['image']
    decoded = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(decoded))
    processed_image = preprocess_image(image, target_size = (70,70))
    
    prediction = model.predict(processed_image).tolist()
    
    response = {
        'prediction' : {
            'akiec' : prediction[0][0],
            'bcc' : prediction[0][1],
            'bkl' : prediction[0][2],
            'df' : prediction[0][3],
            'mel' : prediction[0][4],
            'nv' : prediction[0][5],
            'vasc' : prediction[0][6]
        }
    }
    return jsonify(response)
            