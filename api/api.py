import json
from flask import Flask
from flask.wrappers import Request
from flask_cors import CORS
from flask import request
import functions as fn

app = Flask(__name__)
CORS(app)

@app.route('/test')
def test():
    return {'result': 'result'}

@app.route("/gateway", methods=["POST"])
def getGateway():
    result = request.json
    ip = result["data"]

    return {'result': fn.getGateway(ip)}

@app.route("/broadcast", methods=["POST"])
def getBroadcast():
    result = request.json
    ip = result["data"]

    return {'result': fn.getBroadcast(ip)}

@app.route("/comparison", methods=["POST"])
def getComparison():
    result = request.json
    ip = result["data"]
    ip2 = result["data2"]

    return {'result': fn.PerteneceARed(ip, ip2)}