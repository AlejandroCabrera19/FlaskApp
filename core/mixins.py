from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app import db

# Creating the customer model
class BaseModelMixen(object):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    # Nullable default is true, Unique default is False

    def save(self):
        # Used to save data
        db.session.add(self)
        return db.session.commit()

    def delete(self):
        # Used to delete data
        db.session.delete(self)
        return db.session.commit()

    def to_dict(self):
        # Collects all values and returns a dictionary
        return {
            "id": f"{self.id}",
            "username": f"{self.username}",
            "first_name": f"{self.first_name}",
            "last_name": f"{self.last_name}",
            "email": f"{self.email}",
            "dob": f"{self.dob}",
            "date_created": f"{self.date_created}",
        }
