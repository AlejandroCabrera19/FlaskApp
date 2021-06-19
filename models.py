from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

class Customer(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        first_name = db.Column(db.String, unique=True, nullable = False)
        last_name = db.Column(db.String, unique=True, nullable = False)
        username = db.Column(db.String, unique=True, nullable = False)
        email = db.Column(db.String, unique=True, nullable = False)
        dob = db.Column(db.DateTime, default = datetime.now,unique=True, nullable = False)
