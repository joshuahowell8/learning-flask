from flask import Flask, render_template, request, session, redirect, url_for
from models import db, User #imports from models.py
from forms import SignupForm


app = Flask(__name__)
										#postgresql://localhost/learningflask will NOT work
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///learningflask'
db.init_app(app)

#This is to prevent Cross-site forgery requests
app.secret_key = "development-key"

#Routes to the main page of the app
@app.route("/")
def index():
	return render_template("index.html")

#Routes to localhost:5000/about
@app.route("/about")
def about():
	return render_template("about.html")

#routes to localhost:5000/signup
@app.route("/signup", methods=['GET', 'POST'])
def signup():
	form = SignupForm()

	if request.method == 'POST':
		if form.validate() == False:
			return render_template('signup.html', form=form)
		else:
			newuser = User(form.first_name.data, form.last_name.data, form.email.data, form.password.data)
			db.session.add(newuser) #adds the new user from above to the database
			db.session.commit() #persistence to database

			session['email'] = newuser.email #Creates a session for a user
			return redirect(url_for('home')) #Redirects the user in a session to home page

	elif request.method == 'GET':
		return render_template('signup.html', form=form)

@app.route("/home")
def home():
	return render_template("home.html")

if __name__ == "__main__":
	app.run(debug=True)