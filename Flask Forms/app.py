from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, BooleanField, RadioField,
                     SelectField, TextAreaField)
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

# This was for the basic intro to Forms

# class InfoForm(FlaskForm):
#
#     breed = StringField("What breed are you?")
#     submit = SubmitField("Submit")
#
#
# @app.route('/', methods=['GET', 'POST'])
# def hello_world():  # put application's code here
#
#     breed = False
#     form = InfoForm()
#
#     if form.validate_on_submit():
#         breed = form.breed.data
#         form.breed.data = ''
#
#     return render_template('index.html', form=form, breed=breed)

# Form Fields part 1
# class InfoForm(FlaskForm):
#     breed = StringField('What breed are you?', validators=[DataRequired()])
#     neutered = BooleanField('Have you been neutered?')
#     mood = RadioField('Please choose you mood:',
#                       choices=[('mood_one', 'Happy'), ('mood_two', 'Excited')])
#     food_choice = SelectField('Pick your favorite food:',
#                               choices=[('chicken', 'Chicken'), ('beef', 'Beef'), ('fish', 'Fish')])
#     feedback = TextAreaField()
#     submit = SubmitField('Submit')
#
#
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     form = InfoForm()
#     if form.validate_on_submit():
#         session['breed'] = form.breed.data
#         session['neutered'] = form.neutered.data
#         session['mood'] = form.mood.data
#         session['food'] = form.food_choice.data
#         session['feedback'] = form.feedback.data
#
#         return redirect(url_for('thankyou'))
#
#     return render_template('Form_Fields_1/index.html', form=form)
#
#
# @app.route('/thankyou')
# def thankyou():
#     return render_template('Form_Fields_1/thankyou.html')


# Practicing Flash Messages
# class SimpleForm(FlaskForm):
#     submit = SubmitField('Click Me!')
#
#
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     form = SimpleForm()
#     if form.validate_on_submit():
#         flash('You clicked the button!')
#         return redirect(url_for('index'))
#
#     return render_template('Flash_Message/index.html', form=form)


# Code Along Forms and Flash Project
class SimpleForm(FlaskForm):
    submit = SubmitField('Submit')
    breed = StringField('What Breed are you?')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SimpleForm()
    if form.validate_on_submit():
        session['breed'] = form.breed.data
        flash(f"You just changed your breed to: {session['breed']}!")
        return redirect(url_for('index'))

    return render_template('CodeAlong_Project/index.html', form=form)
    

if __name__ == '__main__':
    app.run()
