# Comparison and Logical Operators
# Comparison operators -> <, >, ==, !=
# Logical operators -> and, or

# logical operators allow us to chain comparison operators

print(1 > 2)  # False
print(3 > 2)  # True

print(3 >= 2)  # False

print(3 == 3)  # True
print(3 != 3)  # False

username = "Admin"
check = "Admin"
permission = True

print(username == check)  # -> do something

print(1 == 1 and 2 < 3)  # True
print(1 == 2 and 2 < 3)  # False, not all conditions are true

print(1 == 2 or 2 < 3)  # True, one of the conditions is true

print(username == check and permission)  # False b/c permission is False

has_permission = True
logged_in = True
print(has_permission and logged_in)  # True because the values are true

# if, elif, and else Statements
# the beginning or Control Flow
if 1 < 2:
	print('Yes')

if username == check:
	print("Access Granted")

if 1 == 2 and 1 < 2:
	print("Access Granted")
elif 1 == 1:
	print("Middle Condition True")
else:
	print("All conditions are not true")

if username == 'admin' and permission:
	print('Full Access')
elif (username == 'admin') and (permission == False):
	print('Admin access only')
else:
	print('No Access')
