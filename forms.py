from flask_wtf import Form 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
	first_name = StringField('First name', validators=[DataRequired("We need your first name.")])
	last_name = StringField('Last name', validators=[DataRequired("If we need your first name, then we DEFINITELY need your last name.")])
	email = StringField('Email', validators=[DataRequired("I won't spam you. Nor do I care to."), Email("Tsk, tsk...This is not valid!")])
	password = PasswordField('Password', validators=[DataRequired("I won't know your pw...or will I? ;)"), Length(min=6, message="Make it more than 6 characters fool!")])
	submit = SubmitField('Sign up')

class LoginForm(Form):
	email = StringField('Email', validators=[DataRequired("Enter your email bruh!"), Email("Email bro!!")])
	password = PasswordField('Password', validators=[DataRequired("We need that password bro!")])
	submit = SubmitField("Sign in")

class AddressForm(Form):
	address = StringField('Address', validators=[DataRequired("Please enter the address.")])
	submit = SubmitField("Search")