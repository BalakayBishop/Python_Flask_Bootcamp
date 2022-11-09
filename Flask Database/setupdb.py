from app import *

# Creates all tables
db.create_all()

sam = Puppy('Sammy', 3)
frank = Puppy('Franky', 4)

print(sam.id)
print(frank.id)
# these two should print None because they were not added

db.session.add_all([sam, frank])  # or db.session.add(sam)

db.session.commit()  # save the db changes

print(sam.id)
print(frank.id)
