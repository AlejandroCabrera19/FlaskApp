from os import error
import customers
from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from app import db
from forms import RegistrationForm
from customers.models import Customer
views = Blueprint('views',__name__,template_folder='templates')

@views.route('/', methods=['GET','POST'])
def index():
    form = RegistrationForm()
    if request.method == 'POST':#This makes it so the route detects if there was a post method used
        error = 'Error: You have not entered your: ' 
        if Customer.query.filter_by(username = form.username.data).first() is not None:
            flash('Customer '+form.username.data+' already created!') #This is to let the customer know if they already have an account
            return render_template('register.html', title = 'Register', form = form)
        else: #These Ifs are to test if the fields are empty
            if form.username.data == "":
                error = error + "Username," 
            if form.first_name.data == "":
                error = error + "First Name,"
            if form.last_name.data == "":
                error = error + "Last Name,"
            if form.email.data == "":
                error = error + "Email,"
            if form.dob.data == "":
                error = error + "Date of Birth"
            if error != 'Error: You have not entered your: ':
                #Flashes the number of fields left blank
                flash(error)
            
        if error == 'Error: You have not entered your: ':
            #block of code that executes if there are no errors
            newCustomer = Customer(username = form.username.data,first_name = form.first_name.data,last_name = form.last_name.data,email = form.email.data,dob = form.dob.data)
            db.session.add(newCustomer)
            db.session.commit()
            flash(f'Customer created with Username: {form.username.data}, First Name: {form.first_name.data}, Last Name: {form.last_name.data}, Email: {form.email.data}, Date of Birth: {form.dob.data}')
    return render_template('register.html', title = 'Register', form = form)
#newCust = Customer(username = userName,first_name = firstName,last_name = lastName,email = email,dob = dob)
    