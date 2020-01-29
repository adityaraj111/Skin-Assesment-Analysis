
import base64
import numpy as np
import io
from PIL import Image
from PIL import ImageFile
from tensorflow import keras
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from flask import request
from flask import jsonify
from flask import Flask
from flask_cors import CORS
import cv2

app = Flask(__name__)
CORS(app)

def preprocess_image(image, target_size):
    
    #image = cv2.resize(image,(70,70))
    image = image.resize(target_size)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    
    return image


@app.route("/predict", methods=["POST"])
def predict():
    probability = []
    print(" * Loading Keras model...")
    model = keras.models.load_model('new_model.h5')
    print(" * Model Loaded...")
    
    message = request.get_json(force=True)
    
    encoded = message['image']
    encoded_1=encoded[23:]
    #print(encoded[23:])
    #print("ck1")
    #print("\n")
    decoded = base64.b64decode(encoded_1)
    #print(decoded)
    image = Image.open(io.BytesIO(decoded))
   # image = Image.open(io.BytesIO(decoded))
   # jpg_as_np =  np.frombuffer(decoded,dtype=np.uint8)
   # image = cv2.imdecode(jpg_as_np,flags=1)
    
    #byteImgIO = io.BytesIO(decoded)
    #image = Image.open(byteImgIO.read())
    #print(image)
    img = preprocess_image(image, target_size=(70,70))
    #print('ck4')
    #print('\n')
    prob = model.predict_proba(img)
    p = np.argsort(model.predict_proba(img))
    for i in p:
        p = i
    for i in prob:
        prob = i
    for i in range(len(prob)):
        probability.append([prob[i],p[i]])
    probability.sort(reverse=True)   
        
    classes = {0 : 'actinic keratosis /Bowens disease (intraepithelial carcinoma) (AKIEC)',
               1 : 'basal cell carcinoma (BCC)',
               2 : "benign keratosis (BKL)",
               3 :  "dermatofibroma (DF)",
               4 :  "melanoma (MEL)",
               5 :  'melanocytic nevus (NV)',
               6 :  'vascular lesion (VASC)' }
    response = ''
    #print('ck5')
    for i in probability:
        response += "You can have disease : '{}' with probability = {} \n".format(classes[i[1]],i[0])
        response +="\n"
    print(response)
    return jsonify(response)
    
            