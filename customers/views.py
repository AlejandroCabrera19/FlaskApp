import customers
from flask import Blueprint, flash, render_template, request
from app import db
from customers.models import Customer
from sqlalchemy import exc

views = Blueprint("views", __name__, template_folder="templates")


@views.route("/", methods=["GET", "POST"])
def index():
    return render_template("register.html", title="Register")


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
<<<<<<< HEAD
        return {"Message": "Error 409, left required fields empty"}
=======
        return {"Message": "ERROR, Code: 422, left required fields empty"}


def retrieve(customer_id=-1):
    try:
        if customer_id == -1:
            customer_list = {}
            for i in range(1, Customer.query.count() + 1):
                selected_customer = Customer.query.filter_by(id=i).first()
                customer_list.update({f"Customer {i}": f"{selected_customer.username}"})
            return json.dumps(customer_list)
        else:
            selected_customer = Customer.query.filter_by(id=customer_id).first()
            returning_data = {
                "id": f"{selected_customer.id}",
                "username": f"{selected_customer.username}",
                "first_name": f"{selected_customer.first_name}",
                "last_name": f"{selected_customer.last_name}",
                "email": f"{selected_customer.email}",
                "dob": f"{selected_customer.dob}",
                "date_created": f"{selected_customer.date_created}",
            }
            return json.dumps(returning_data)
    except Exception:
        return "ERROR, Code: 404, invalid id number entered"


@views.route("/list", methods=["GET"])
def list():
    return retrieve()


@views.route("/detail/<int:customer_id>", methods=["GET"])
def detail(customer_id):
    return retrieve(customer_id)


@views.route("/update/<int:customer_id>", methods=["PATCH", "PUT"])
def update(customer_id):
    try:
        request_data = request.get_json()
        updated_customer = Customer.query.filter_by(id=customer_id).first()
        if request.method == "PUT":
            if (
                "username" and "first_name" and "last_name" and "email" and "dob"
            ) not in request_data:
                return "ERROR! Code: 422, did not fill all required fields"
            else:
                updated_customer.username = request_data["username"]
                updated_customer.first_name = request_data["first_name"]
                updated_customer.last_name = request_data["last_name"]
                updated_customer.email = request_data["email"]
                updated_customer.dob = request_data["dob"]
                db.session.commit()
                return {
                    "id": f"{updated_customer.id}",
                    "username": f"{updated_customer.username}",
                    "first_name": f"{updated_customer.first_name}",
                    "last_name": f"{updated_customer.last_name}",
                    "email": f"{updated_customer.email}",
                    "dob": f"{updated_customer.dob}",
                    "date_created": f"{updated_customer.date_created}",
                }
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
            return {
                "id": f"{updated_customer.id}",
                "username": f"{updated_customer.username}",
                "first_name": f"{updated_customer.first_name}",
                "last_name": f"{updated_customer.last_name}",
                "email": f"{updated_customer.email}",
                "dob": f"{updated_customer.dob}",
                "date_created": f"{updated_customer.date_created}",
            }
    except Exception:
        return "ERROR, Code: 404, invalid id number entered"


@views.route("/delete/<int:customer_id>", methods=["DELETE"])
def delete(customer_id):
    try:
        removed_customer = Customer.query.filter_by(id=customer_id).first()
        db.session.delete(removed_customer)
        db.session.commit()
        return "Code: 204"
    except:
        return "ERROR, Code: 404, No such customer to delete"
>>>>>>> fe6d54d... Another Quick Git Fix
