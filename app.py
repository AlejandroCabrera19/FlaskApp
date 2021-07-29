"""
API Project
By: Alejandro Cabrera
Purpose: The purpose is to set up a database and get a stream of JSON in
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config["SECRET_KEY"] = "f52e426cb2bc827ee460520ef2e02ee6"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
# HINT: sqlite:///db.sqlite3
db = SQLAlchemy(app)
ma = Marshmallow(app)
from customers.models import Customer
from customers.views import views

app.register_blueprint(views)
