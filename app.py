"""
API Project
By: Alejandro Cabrera
Purpose: For now, just to test flask and JSON objects out
"""
from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/')

def JSON():
    jsonObj = {
            "name":"Alejandro",
            "datetime":datetime.utcnow().isoformat()}
    return jsonObj
