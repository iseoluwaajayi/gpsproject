from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  'postgres://postgres:password@localhost/sample2'
app.debug = True
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	area = db.Column(db.String(100), unique=True)
	latitude = db.Column(db.String(100), unique=True)
	longitude = db.Column(db.String(100), unique=True)
	message = db.Column(db.String(100), unique=True)

	def __init__(self, area, latitude, longitude, message):
		self.area = area
		self.latitude = latitude
		self.longitude = longitude
		self.message = message

	def __repr__(self):
		return '<User %r>' % self.area

@app.route('/')
def index():
	return render_template('add_user.html')

@app.route('/post_user', methods=['POST'])
def post_user():
	user = User(request.form['area'], request.form['latitude'], request.form['longitude'], request.form['message'])
	db.session.add(user)
	db.session.commit()
	return redirect(url_for('index'))

if __name__ == "__main__":
	app.run()