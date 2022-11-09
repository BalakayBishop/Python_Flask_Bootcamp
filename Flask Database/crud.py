from app import *

# Create
my_puppy = Puppy('Rufus', 5)
db.session.add(my_puppy)
db.session.commit()

# Read
all_puppies = Puppy.query.all()  # list of puppy objects in table
print(all_puppies)

# Select by ID
puppy_1 = Puppy.query.get(1)
print(puppy_1.name)

# Filter
puppy_franky = Puppy.query.filter_by(name='Franky')
print(puppy_franky.all())

# Update
first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()

# Delete
second_puppy = Puppy.query.get(2)
db.session.delete(second_puppy)
db.session.commit()

all_puppies = Puppy.query.all()
print(all_puppies)

# Running this more than once will cause errors
