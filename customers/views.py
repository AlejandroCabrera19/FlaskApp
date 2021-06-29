import customers
from flask import Blueprint, flash, render_template, request
from app import db
from customers.models import Customer
from sqlalchemy import exc
import json

views = Blueprint("views", __name__, template_folder="templates")


@views.route("/json-post", methods=["POST"])
def json_post():
    try:
        # The block of code that is supposed to execute if a new customer is to be placed in the database
        request_data = request.get_json()
        userName = request_data["username"]
        firstName = request_data["first_name"]
        lastName = request_data["last_name"]
        email = request_data["email"]
        dob = request_data["dob"]
        newCustomer = Customer(
            username=userName,
            first_name=firstName,
            last_name=lastName,
            email=email,
            dob=dob,
        )
        db.session.add(newCustomer)
        db.session.commit()
        return {
            "id": f"{newCustomer.id}",
            "username": f"{userName}",
            "first_name": f"{firstName}",
            "last_name": f"{lastName}",
            "email": f"{email}",
            "dob": f"{dob}",
            "date_created": f"{newCustomer.date_created}",
        }
    except exc.IntegrityError:
        # Error Code 409, for resource already exists / duplicate resource / Conflict
        # Error that occurs when a customer already has a place in the database
        return {"Message": "Error 409, Customer already exists"}
    except KeyError:
        # Error that occurs when a user leaves fields empty
        return {"Message": "ERROR, Code: 422, left required fields empty"}
