from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):
	name = StringField("Name of puppies: ")
	submit = SubmitField('Submit')


class DelForm(FlaskForm):
	id = IntegerField("ID number of Puppy to Remove: ")
	submit = SubmitField('Remove')