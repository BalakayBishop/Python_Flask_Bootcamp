from myproject import db, app
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, login_required, logout_user
from myproject.models import User
from myproject.forms import LoginForm, RegistrationForm
# from flask_bcrypt import Bcrypt
# from werkzeug.security import generate_password_hash, check_password_hash

# Bcrypt
# bcrypt = Bcrypt()
# password = 'password'
# hashed = bcrypt.generate_password_hash(password)
# print(hashed)
#
# # Werkzeug
# hashed_pass = generate_password_hash(password)
# print(hashed_pass)
# check = check_password_hash(hashed_pass, 'correct')
# print(check)


@app.route('/')
def index():  # put application's code here
	return render_template('index.html')

@app.route('/welcome')
@login_required
def welcome():
	return render_template('welcome_user.html')

@app.route('/logout')
@login_required
def logout():
	logout_user()
	flash("You've been logged out!")
	return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		
		if user.check_password(form.password.data) and user is not None:
			login_user(user)
			flash("Logged in successfully")
			next = request.args.get('next')
			
			if next is None or not next[0] == '/':
				next = url_for('welcome')
			return redirect(next)
		
	return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(email=form.email.data,
		            username=form.username.data,
		            password=form.password.data)
		
		db.session.add(user)
		db.session.commit()
		flash("Thank you for registering")
		return redirect(url_for('login'))
		
	return render_template('register.html', form=form)

@app.errorhandler(500)
def page_not_found(e):
	return render_template('500.html'), 500


if __name__ == '__main__':
	app.run()

# ----------------------------------------------------------------------------
# def check_email(self, field):
# 	if User.query.filter_by(email=field.data).first():
# 		raise ValidationError('Your email has been registered already!')
#
#
# def check_username(self, field):
# 	if User.query.filter_by(username=field.data).first():
# 		raise ValidationError('Your username has been registered already!')
# ----------------------------------------------------------------------------
# def validate_email(self, email):
#         if User.query.filter_by(email=self.email.data).first():
#             raise ValidationError('Email has been registered')
# def validate_username(self, username):
# 	if User.query.filter_by(username=self.username.data).first():
# 		raise ValidationError('Username has been registered')
# ----------------------------------------------------------------------------
# def validate_email(self, email):
# 	if email.data != current_user.email:
# 		if User.query.filter_by(email=email.data).first():
# 			raise ValidationError('Email has been registered')
#
# def validate_username(self, username):
# 	if username.data != current_user.username:
# 		if User.query.filter_by(username=username.data).first():
# 			raise ValidationError('Username has been registered')
# ----------------------------------------------------------------------------