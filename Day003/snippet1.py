#welcome to Day 3 of my 100 days of codes
#Today I will cotninue on decorators in python
#
#follow me on twitter @_drjimoh


#I a, copying all my existing codes from day 1 to this file
#defining global variables

#I will do a little bit of rearrangement
#but my global variables will still come first
dictionary_of_staff_in_department = {}
key_list = []

#defining decoration function
def add_salary(func):
	#lets define a wrapper function that modifies the employees list
	#and returnd yhe new list
	def wrapper(department, employees,  amount):
		#for loop to add salary string to each name in 
		#the employees list
		for employee in employees:
			employees[employees.index(employee)] = employee + ' to collect ' + str(amount)
		return func(department, employees)
	return wrapper


@add_salary
def stafflist(department, employees):
	'''this is a function for computing staff list
	'''
	#making sure a list of employees is passed in and
	#not string
	try:
		assert type(employees) == list, 'Employees is not a list'
	except AssertionError as e:
		print(e)
		return None
	#lets update our dictionary of staff list
	if len(dictionary_of_staff_in_department) == 0:
		dictionary_of_staff_in_department.update({department.upper():employees})
	else:
		for key, value in dictionary_of_staff_in_department.items():
			key_list.append(key)
		for key in key_list:
			if key.upper() != department.upper():
				dictionary_of_staff_in_department.update({department.upper():employees})

#calling the decorated stafflist function
stafflist('Security', ['Mamud Inec', 'Bakare Peters'], amount=1000)
stafflist('Admin', ['Jimoh Waliu', 'Ekwesi Mamoh', 'Amaka Inec'], amount=200000)

#lets check what we have
for key, values in dictionary_of_staff_in_department.items():
	print(key, values)

