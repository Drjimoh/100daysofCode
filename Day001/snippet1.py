#welcome to Day 1 of my 100 days of codes
#Today I will be mastering how to use decorators in python
#
#follow me on twitter @_drjimoh


#defining global variables
list_of_departments = []
dictionary_of_staff_in_department = {}


def add_dept(*args):
	'''
		this function creates departments only if the 
		department doesnt exist as at the time of 
		creation
	'''
	for arg in args:
		if arg.upper() not in list_of_departments:
			#I had to put the string in Uppercase
			#to avoid multiple entries in mixedcase
			#for example Audit, AUdit, AuDIT
			list_of_departments.append(arg.upper())
		else:
			print('%s department already exists' %arg)
	return list_of_departments



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
	dictionary_of_staff_in_department.update({department.upper():employees})



if __name__ == '__main__':

	#calling our functions
	#adding departments
	add_dept('Finance', 'Admin', 'Hr')
	#adding stafflists
	stafflist('Finance', ['Labake James', 'Omoraigbe Solomon', 'Okobenson Peter'])
	stafflist('Admin', ['Jimoh Waliu', 'Ekwesi Mamoh', 'Amaka Inec'])
	stafflist('Hr', ['Buhari Mohammadu', 'Saraki Bukola', 'Oshiomole Adams'])

	#let us check if our codes work correctly
	for key, values in dictionary_of_staff_in_department.items():
		print(key, values)