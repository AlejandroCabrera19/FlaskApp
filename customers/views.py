import json
from flask import Blueprint, jsonify, request
from app import db
from customers.models import Customer
from sqlalchemy import exc
from customers.schemas import CustomerSchema

views = Blueprint("views", __name__, url_prefix="/customers")
customerSchema = CustomerSchema()


@views.route("/", methods=["POST"])
def create():
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
        newCustomer.save()
        return (customerSchema.jsonify(newCustomer)), 200
    except exc.IntegrityError:
        # Error Code 409, for resource already exists / duplicate resource / Conflict
        # Error that occurs when a customer already has a place in the database
        # Should occur when a customer enters a unique field such as email and username more than once
        return {"Message": "ERROR, Code: 409, Customer already exists"}, 409
    except KeyError:
        # Error that occurs when a user leaves fields empty
        return {"Message": "ERROR, Code: 422, left required fields empty"}, 422


@views.route("/", defaults={"customer_id": None}, methods=["GET"])
@views.route("/<int:customer_id>", methods=["GET"])
def retrieve(customer_id):
    try:
        if customer_id is None:
            customer_list = []
            for selected_customer in Customer.query.all():
                customer_list.append(selected_customer.to_dict())
            return json.dumps(customer_list), 200
        else:
            selected_customer = Customer.query.filter_by(id=customer_id).first()
            return json.dumps(selected_customer.to_dict()), 200
    except Exception as e:
        print(e)
        return {"Message": "ERROR, invalid id number entered"}, 404


@views.route("/<int:customer_id>", methods=["PATCH", "PUT"])
def update(customer_id):
    try:
        request_data = request.get_json()
        updated_customer = Customer.query.filter_by(id=customer_id).first()
        if request.method == "PUT":
            updated_customer.username = request_data["username"]
            updated_customer.first_name = request_data["first_name"]
            updated_customer.last_name = request_data["last_name"]
            updated_customer.email = request_data["email"]
            updated_customer.dob = request_data["dob"]
            updated_customer.save()
            return (customerSchema.jsonify(updated_customer)), 200
        elif request.method == "PATCH":
            if "username" in request_data:
                updated_customer.username = request_data["username"]
            if "first_name" in request_data:
                updated_customer.first_name = request_data["first_name"]
            if "last_name" in request_data:
                updated_customer.last_name = request_data["last_name"]
            if "email" in request_data:
                updated_customer.email = request_data["email"]
            if "dob" in request_data:
                updated_customer.dob = request_data["dob"]
            updated_customer.save()
            return (customerSchema.jsonify(updated_customer)), 200
    except KeyError:
        return {"Message": "ERROR, did not fill all required fields"}, 422
    except Exception:
        return {"Message": "ERROR, invalid id number entered"}, 404


@views.route("/<int:customer_id>", methods=["DELETE"])
def delete(customer_id):
    try:
        removed_customer = Customer.query.filter_by(id=customer_id).first()
        removed_customer.delete()
        return "", 204
    except:
        return {"Message": "ERROR, invalid id number entered"}, 404
