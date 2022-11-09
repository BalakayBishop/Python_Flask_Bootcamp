from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
# __file__ -> C:\something\dir\app.py
# it is better to use the OS Lib to be OS independent

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

# username = "root"
# password = "password"
# host = "localhost", "127.0.0.1", "localhost:3306"
# db_name = "world"
# app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{username}:{password}@{host}/{db_name}"

db = SQLAlchemy(app)
app.app_context().push()  # very curious about what this is
migrate = Migrate(app, db)  # connecting app to db for migration

# -------------------------------------------------------
class Puppy(db.Model):
	__tablename__ = 'puppies'
	
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text)
	age = db.Column(db.Integer)
	breed = db.Column(db.Text)
	
	def __init__(self, name, age, breed):
		self.name = name
		self.age = age
		self.breed = breed
		
	def __repr__(self):
		return f"Puppy name: {self.name}, Age: {self.age}"
