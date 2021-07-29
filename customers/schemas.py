from customers.models import Customer
from app import ma


class CustomerSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Customer
        # fields = ('id','username','first_name','last_name','email','dob','date_created')

    id = ma.auto_field()
    username = ma.auto_field()
    first_name = ma.auto_field()
    last_name = ma.auto_field()
    email = ma.auto_field()
    dob = ma.auto_field()
    date_created = ma.auto_field()
