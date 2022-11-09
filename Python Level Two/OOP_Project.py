# Bank account, class owner and balance, methods deposit and withdraw
#
# For this challenge, create a bank account class that has two attributes:
#
# * owner
# * balance
#
# and two methods:
#
# * deposit
# * withdraw
#
# As an added requirement, withdrawals may not exceed the available balance.
#
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class Account:
	def __init__(self, owner, balance=0):
		self.owner = owner
		self.balance = balance
		
	def __repr__(self):
		return f"Account Owner: {self.owner}, Balance: ${self.balance}"
		
	def deposit(self, amount):
		print(f"Depositing: {amount}")
		self.balance = self.balance + amount
		
	def withdraw(self, amount):
		if self.balance - amount >= 0:
			print(f"Withdrawing: {amount}")
			self.balance = self.balance - amount
		else:
			print(f"Insufficient funds: ${self.balance}")


# 1. Instantiate the class
acct1 = Account('Jose', 100)

# 2. Print the object
print(acct1)

# 3. Show the account owner attribute
print(f"Account Owner: {acct1.owner}")

# 4. Show the account balance attribute
print(f"Account Balance: ${acct1.balance}")

# 5. Make a series of deposits and withdrawals
acct1.deposit(50)
print(f"Balance: ${acct1.balance}")
acct1.withdraw(75)
print(f"Balance: ${acct1.balance}")
# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)
