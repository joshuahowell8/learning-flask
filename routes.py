from flask import Flask, render_template, request
from models import db #imports from models.py
from forms import SignupForm


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/learningflask'
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
		return "Great Success!!"
	elif request.method == 'GET':
		return render_template('signup.html', form=form)

if __name__ == "__main__":
	app.run(debug=True)