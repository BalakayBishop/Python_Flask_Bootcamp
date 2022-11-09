from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class AddForm(FlaskForm):
	name = StringField("Name of owner: ")
	submit = SubmitField('Add Owner')