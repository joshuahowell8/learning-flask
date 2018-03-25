from flask_wtf import Form 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class SignupForm(Form):
	first_name = StringField('First name', validators=[DataRequired("We need your first name.")])
	last_name = StringField('Last name', validators=[DataRequired("If we need your first name, then we DEFINITELY need your last name.")])
	email = StringField('Email', validators=[DataRequired("I won't spam you. Nor do I care to.")])
	password = PasswordField('Password', validators=[DataRequired("I won't know your pw...or will I? ;)")])
	submit = SubmitField('Sign up')