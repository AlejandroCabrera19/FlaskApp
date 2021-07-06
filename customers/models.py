from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app import db

#Creating the customer model
class Customer(db.Model):
        id = db.Column(db.Integer, primary_key = True)
        username = db.Column(db.String, unique = True, nullable = False)
        first_name = db.Column(db.String, nullable = False)
        last_name = db.Column(db.String, nullable = False)
        email = db.Column(db.String, unique=True, nullable = False)
        dob = db.Column(db.String, nullable = False)
        date_created = db.Column(db.DateTime, default = datetime.utcnow)
        #Nullable default is true, Unique default is False
        def __repr__(self):
                #Used to verify the customers data
                return f'<Customer ({self.id},{self.username},{self.first_name},{self.last_name},{self.email},{self.dob},{self.date_created})>'

