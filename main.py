from flask import Flask, jsonify
from core.tle_encoder import TLE_encoder

app = Flask(__name__)

@app.route("/")
def index():
    tles = TLE_encoder.open_TLEfile("TLE/TLE_msu.txt")
    tles += TLE_encoder.open_TLEfile("TLE/TLE_astroportal.txt")
    return jsonify([tle.model_dump() for tle in tles]) # генератор

app.run(host="0.0.0.0", port = 5000)