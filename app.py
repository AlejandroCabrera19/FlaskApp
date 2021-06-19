"""
API Project
By: Alejandro Cabrera
Purpose: For now, just to test flask and JSON objects out
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from views import views

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)
app.register_blueprint(views)


class Customer(db.Model):
        username = db.Column(db.String, primary_key=True)
        first_name = db.Column(db.String, unique=False, nullable = False)
        last_name = db.Column(db.String, unique=False, nullable = False)
        email = db.Column(db.String, unique=True, nullable = False)
        dob = db.Column(db.DateTime, unique=False, nullable = False)

"""
@app.route('/')

def JSON():
    jsonObj = {
            "name":"Alejandro",
            "datetime":datetime.utcnow().isoformat()}
    return jsonObj"""
