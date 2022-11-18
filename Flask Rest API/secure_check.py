from user import User

users = [User(1, 'Jose', 'my_password'),
         User(2, 'Frank', 'secret_password')]

username_table = {u.username: u for u in users}
user_id_table = {u.id: u for u in users}

def authenticate(username, password):
	user = username_table.get(username, None)  # this will either return or None
	if user and password == user.password:
		return user
	
	
def identity(payload):
	user_id = payload['identity']
	return user_id_table.get(user_id, None)
