from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'models.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.app_context().push()

# -----------------------------------------------------------------------------------------

class Puppy(db.Model):
	__tablename__ = "Puppies"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text)
	toys = db.relationship('Toy', backref='puppy', lazy='dynamic')  # creating a 1-N rel
	owner = db.relationship('Owner', backref='puppy', uselist=False)  # creating 1-1 rel by stating uselist=False
	
	def __init__(self, name):
		self.name = name
		
		
	def __repr__(self):
		if self.owner:
			return f"Puppy name is {self.name} and the owner is {self.owner.name}"
		else:
			return f"Puppy name is {self.name}, has no owner yet"
		
	
	def report_toys(self):
		print("Here are my toys:")
		for toy in self.toys:
			print(toy.item_name)
	
	
class Toy(db.Model):
	__tablename__ = "Toys"
	id = db.Column(db.Integer, primary_key=True)
	item_name = db.Column(db.Text)
	puppy_id = db.Column(db.Integer, db.ForeignKey('Puppies.id'))  # declaring FK to connect to Puppies table
	
	def __init__(self, item_name, puppy_id):
		self.item_name = item_name
		self.puppy_id = puppy_id


class Owner(db.Model):
	__tablename__ = "Owner"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text)
	puppy_id = db.Column(db.Integer, db.ForeignKey('Puppies.id'))
	
	def __init__(self, name, puppy_id):
		self.name = name
		self.puppy_id = puppy_id
