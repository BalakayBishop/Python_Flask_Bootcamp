from flask import Blueprint, render_template, redirect, url_for, request
from myproject import db
from myproject.models import Owner, Puppy
from myproject.owners.forms import AddForm

owners_blueprints = Blueprint('owners', __name__, template_folder='templates/owners')

@owners_blueprints.route('/add_owner', methods=['GET', 'POST'])
def add():
	form = AddForm()
	all_puppies = Puppy.query.all()
	if form.validate_on_submit():
		owner_name = form.name.data
		pup_id = request.form.get('puppy_id')
		new_owner = Owner(owner_name, pup_id)
		db.session.add(new_owner)
		db.session.commit()
		
		return redirect(url_for('puppies.list_pup'))
	
	return render_template('add_owner.html', form=form, all_puppies=all_puppies)
