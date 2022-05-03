import json
from flask import Flask
from flask.wrappers import Request
from flask_cors import CORS
from flask import request

app = Flask(__name__)
CORS(app)

@app.route('/test')
def test():
    return {'result': 'result'}

@app.route('/gateway')
def getGateway():
    result = request.json
    matrix = result["data"]

    return {'result': getDeterminant(matrix)}