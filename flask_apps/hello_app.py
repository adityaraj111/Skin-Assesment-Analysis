from flask import request
from flask import jsonify
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

CORS(app)
@app.route('/hello',methods=['POST'])
def hello():
    message = request.get_json(force=True)
    name = message['name']
    response = {
            'greeting':'Hello, '+name+ '!'
    }
    return jsonify(response)