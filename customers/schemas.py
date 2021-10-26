from customers.models import Customer
from app import ma


class CustomerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Customer
        # fields = ('id','username','first_name','last_name','email','dob','date_created')
