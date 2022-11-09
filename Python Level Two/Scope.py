# Scope and Nested Statements
# Scope - where you can see or access a variable

x = 'outside'

def report():
	x = 'inside'
	return x

print(x)  # this prints outside

print(report())  # prints inside
print(x)  # prints outside

# 1. name assignments will change local names
# 2. name reference search 4 scopes
# LEGB -> Local, Enclosing, Global, Built-in
# Python will search in this order for the variable

# Local
def report2():
	x = 'local'
	print(x)  # local scope
	
# Enclosing -> function in function
x = 'GLOBAL'

def enclosing():
	x = 'enclosing'
	
	def inside():
		print(x)
		
	inside()
	
enclosing()

# Global
x = 'GLOBAL'


def enclosing():
	
	def inside():
		print(x)
	
	inside()


enclosing()

# Built in
# = len(), sum(), etc.

# changing global variables in functions
# Global keyword -> should be avoided and is not generally used
# it is much safer to pass the variable to the function and then return it, not change it globally
y = "Outside"

def def_global():
	global y
	y = 'inside'
	return y

print(def_global())
print(y)