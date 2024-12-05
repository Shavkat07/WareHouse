





def registration(first_name: str, last_name: str, username: str, email: str, password: str):
	user = {
		'id': 0,
		'username': "",
		'first_name': "",
		'last_name': "",
		'email': "",
		'password': "",
	}
	if len(first_name) <= 50:
		user['first_name'] = first_name
	else:
		print("Ism Xato!!!")
		return
	if len(last_name) <= 50:
		user['last_name'] = last_name
	else:
		print("Familiya Xato!!!")
		return
	if load_data_from_file(file_name='users', param_key='username', param_value=username) is None and username.islower():
		user['username'] = username
	else:
		print("Username already exists!!!")
		return
	if load_data_from_file(file_name='users', param_key='email', param_value=email) is None:
		if email.islower() and "@" in email:
			user['email'] = email
		else:
			print('Email format is invalid!!!')
			return
	else:
		print("Email already exists!!!")
		return
	if len(password) >= 8 and password.isalnum() and not password.isalpha():
		# Bu yerda passwordni hesh lash kerak
		user['password'] = password
	else:
		print("Password must contain at least 8 characters and must contain at least one letter or number!!!")
		return
	if load_data_from_file(file_name='users', param_key='id',) is not None:
		user['id'] = load_data_from_file(file_name='users', param_key='id',) + 1
	else:
		user['id'] = 1
	save_data_to_file(data=user, file_name='users')
	print("User created successfully!")
	return