from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import db
from core.mixins import BaseModelMixen

# Creating the customer model
class Customer(BaseModelMixen, db.Model):
    username = db.Column(db.String, unique=True, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    dob = db.Column(db.String, nullable=False)
    # Nullable default is true, Unique default is False
    def __repr__(self):
        # Used to verify the customers data
        return f"<Customer {self.username}>"
