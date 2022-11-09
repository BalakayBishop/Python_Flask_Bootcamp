# Decorators -> keeping the original stuff but adding more
# @ operator
# @ some_decorator
# def simple_func()

def hello(name='Jose'):

	print('The hello function has been called')

	def greet():
		return "   This is inside greet()"

	def welcome():
		return "   This is inside welcome()"

	if name == "Jose":
		return greet()
	else:
		return welcome()

x = hello(name='Sam')  # prints hello
print(x)

# function as arg
def hello_again():
	return "Hi, there"

def other(func):
	print("Some other code")
	print(func)

other(hello())


def new_dec(func):
	
	def wrap_func():
		print("some code before executing func")
		func()
		print("code after executing func")
		
	return wrap_func

@new_dec
def func_needs_dec():
	print("please decorate")
	
func_needs_dec()

# Note to self return the wrapper func itself not the function call -> causes "TypeError" none not callable

# func_needs_dec() -> new_dec() -> returns/executes the wrapper
# -> transfers/executes func() or whatever func is has @new_dec
# -> returns control back after initial func call