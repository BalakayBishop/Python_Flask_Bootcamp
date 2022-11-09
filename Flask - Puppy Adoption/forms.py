from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):
	name = StringField("Name of puppy: ")
	submit = SubmitField('Submit')
	

class DelForm(FlaskForm):
	id = IntegerField("ID number of Puppy to Remove: ")
	submit = SubmitField('Remove')
	
	
class AddOwner(FlaskForm):
	name = StringField("Name of owner: ")
	submit = SubmitField('Add Owner')