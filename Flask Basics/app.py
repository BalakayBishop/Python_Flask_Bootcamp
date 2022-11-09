from flask import Flask, render_template, request

app = Flask(__name__)


# @app.route('/')  # this is a decorator for where the URL is going to go
# # this could also be route('/some_page') and then it would be 127.0.0.1:500/some_page
# def index():  # put application's code here
# 	return render_template('basic.html')  # connecting python/flask to HTML
#
# # this will now be 127.0.0.1:5000/info
# @app.route('/info')
# def info():
# 	return "<h1>Puppies are cute</h1>"
#
# # example of dynamic routing
# @app.route('/puppy/<name>')
# def other_page(name):
# 	return f'<h1>Puppy: {name}</h1>'
#
# # routing exercise
# @app.route('/puppy_latin/<name>')
# def puppy_latin(name):
# 	# My Solution
# 	pup_latin = list(name)
# 	if name[-1] != 'y':
# 		pup_latin.append("y")
# 		latin_name = ''.join(pup_latin)
# 		return f'<h1>Hi {name}! Your puppy latin name is {latin_name}'
# 	elif pup_latin[-1] == 'y':
# 		pup_latin.pop(-1)
# 		pup_latin.append("iful")
# 		latin_name = ''.join(pup_latin)
# 		return f'<h1>Hi {name}! Your puppy latin name is {latin_name}'

# Provided Solution
# pup_name = ''
# if name[-1] == 'y':
#   pup_name = name[:-1] + 'iful'
# else:
#   pup_name = name + 'y'
# return f'<h1>Your Puppy Latin name is {pup_name}</h1>'

# @app.route('/')
# def index():
# 	name = 'Jose'
# 	letters = list(name)
# 	pup_dict = {'pup_name': 'Sammy'}
# 	return render_template('basic.html', name=name, letters=letters, pup_dict=pup_dict)
# this is using Jinga and will pass my_var

# we can use control flow through using {% %} in the template
# @app.route('/')
# def index():
# 	# my_list = [1, 2, 3, 4, 5]
# 	puppies = ['Fluffy', 'Rufus', 'Spike']
# 	return render_template('control_flow.html', puppies=puppies)

# @app.route('/')
# def index():
# 	return render_template('home.html')
# # this now has url_for() in the base.html to link templates
#
# @app.route('/puppy/<name>')
# def pup_name(name):
# 	return render_template('puppy.html', name=name)

# @app.route('/')
# def index():
# 	return render_template('index.html')
# this now has url_for() in the base.html to link templates

# @app.route('/signup_form')
# def signup_form():
# 	return render_template('signup.html')
#
# @app.route('/thank_you')
# def thank_you():
# 	first = request.args.get('first')
# 	last = request.args.get('last')
#
# 	return render_template('thankyou.html', first=first, last=last)
#
# @app.errorhandler(404)
# def page_not_found(e):
# 	return render_template('404.html'), 404


@app.route('/')
def index():
	return render_template('index_project.html')


@app.route('/report')
def report():
	username = request.args.get('username')
	
	uppercase = False
	lowercase = False
	number = False
	
	for i in username:
		if i.isupper():
			uppercase = True
			break
	for j in username:
		if j.islower():
			lowercase = True
			break
	if username[-1].isdigit():
		number = True
	
	report_all = lowercase and uppercase and number
	
	return render_template('report.html', report_all=report_all, lowercase=lowercase, uppercase=uppercase,
	                       number=number)


if __name__ == '__main__':
	app.run()
