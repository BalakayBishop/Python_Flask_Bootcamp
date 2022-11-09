# OOP -> creating objects that have methods and attributes
# Create personal methods with the . operator
# keyword class and class
class NameOfClass:
	def __init__(self, param1, param2):
		self.param1 = param1
		self.param2 = param2

# a totally empty class
class Sample:
	pass

# instance of class Sample, type = __main__.Sample
x = Sample()

class Dog():
	# class obj attributes: defined outside method, things that will be true no matter the instance
	# no need for self.
	species = 'mammal'
	
	# this is called right after instance is created
	# self will allow you to assign attributes
	def __init__(self, breed, name):
		self.breed = breed
		self.name = name
		
y = Dog('Golden', 'Sam')
print(y.breed)  # this will print the arg passed to the class instantiation
print(y.name)
print(y.species)

my_dog = Dog('Golden Retriever', 'Autumn')


class Circle():
	pi = 3.1415
	
	def __init__(self, radius=1):
		self.radius = radius
		
	def area(self):
		return self.pi * pow(self.radius, 2)
	
	def circumference(self):
		return 2 * self.pi * self.radius


my_circle = Circle()
print(my_circle.radius)  # this will print 1 since it has default
print(my_circle.area())  # this will use my_circle's given radius
print(my_circle.circumference())

# ---------------------------------------
# Inheritance
class Animal():
	def __init__(self, fur):
		self.fur = fur
		
	def report(self):
		print('Animal')

	def eat(self):
		print('Eating')
		
a = Animal('fuzzy')
a.eat()
a.report()

class Dog(Animal):
	def __init__(self, fur):
		Animal.__init__(self, fur)  # this will call the Animal init method
		print("Dog Created")
		
	def report(self):
		print('I am a dog')  # this is now an overwritten method
		
d = Dog('short')
d.eat()  # this .eat method is inherited from the Animal class
d.report()  # using the overwritten method
print(d.fur)  # this will print 'short'
