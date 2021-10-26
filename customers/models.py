from app import db
from core.mixins import BaseModelMixin

# Creating the customer model
class Customer(BaseModelMixin):
    username = db.Column(db.String, unique=True, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    dob = db.Column(db.String, nullable=False)
    # Nullable default is true, Unique default is False
    def __repr__(self):
        # Used to verify the customers data
        return f"<Customer {self.username}>"

    def save(self):
        # Used to save data
        super().save()

    def delete(self):
        # Used to delete data
        super().delete()

    def to_dict(self):
        custDict = {
            "username": f"{self.username}",
            "first_name": f"{self.first_name}",
            "last_name": f"{self.last_name}",
            "email": f"{self.email}",
            "dob": f"{self.dob}",
        }
        custDict.update(super().to_dict())
        return custDict
