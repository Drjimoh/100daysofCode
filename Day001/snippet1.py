#welcome to Day 1 of my 100 days of codes
#Today I will be mastering how to use decorators in python
#
#follow me on twitter @_drjimoh


#defining global variables
dictionary_of_staff_in_department = {}
key_list = []

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
		print(key_list)
		for key in key_list:
			if key.upper() != department.upper():
				dictionary_of_staff_in_department.update({department.upper():employees})





if __name__ == '__main__':

	#calling our functions
	#adding departments
	#add_dept('Finance', 'Admin', 'Hr')
	#adding stafflists
	stafflist('Finance', ['Labake James', 'Omoraigbe Solomon', 'Okobenson Peter'])
	stafflist('Admin', ['Jimoh Waliu', 'Ekwesi Mamoh', 'Amaka Inec'])
	stafflist('Hr', ['Buhari Mohammadu', 'Saraki Bukola', 'Oshiomole Adams'])
	#stafflist('Admin', ['Jimoh Wali Junior'])

	#let us check if our codes work correctly
	for key, values in dictionary_of_staff_in_department.items():
		print(key, values)