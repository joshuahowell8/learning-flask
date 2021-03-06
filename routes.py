from flask import Flask, render_template, request, session, redirect, url_for
from models import db, User #imports from models.py
from forms import SignupForm, LoginForm, AddressForm #imports from forms.py


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
	if 'email' in session:
		return redirect(url_for('home'))

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

#Routes to localhost:5000/login
@app.route("/login", methods=["GET","POST"])
def login():
	if 'email' in session:
		return redirect(url_for('home'))
	form = LoginForm()

	if request.method == "POST":
		if form.validate() == False:
			return render_template("login.html", form=form)
		else:
			email = form.email.data
			password = form.password.data

			user = User.query.filter_by(email=email).first()
			if user is not None and user.check_password(password):
				session['email'] = form.email.data
				return redirect(url_for('home'))
			else:
				return redirect(url_for('login'))

	elif request.method == 'GET':
		return render_template('login.html',form=form)

#logs the user out of their session
@app.route("/logout")
def logout():
	session.pop('email', None)
	return redirect(url_for('index'))

#Routes users to a home page localhost:5000/home
@app.route("/home")
def home():
	if 'email' not in session:
		return redirect(url_for('login'))

	form = AddressForm()
	if request.method == 'POST':
		if form.validate() == False:
			return render_template('home.html', form=form)
		else:
			#handle the form submission
			pass
	elif request.method == 'GET':
		return render_template("home.html", form=form)

if __name__ == "__main__":
	app.run(debug=True)