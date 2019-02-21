#welcome to Day 2 of my 100 days of codes
#Today I will continue on how to use decorators in python
#
#follow me on twitter @_drjimoh


from sys import path 
#let's add path to yesterday's file to my window's path list
#so python can locate the file

path_of_file = 'C:\\WHEREVER' #use Actual absolutePath
path.append(r"C:\Users\USER\Documents\codes\100 days of code\Day001") #Replace thiswith path_of_file
#import all from the snipet.py file
from snippet1 import * 


#put the functions to call
#stafflist('Finance', ['Labake James', 'Omoraigbe Solomon', 'Okobenson Peter'])
#stafflist('Admin', ['Jimoh Waliu', 'Ekwesi Mamoh', 'Amaka Inec'])
#stafflist('Hr', ['Buhari Mohammadu', 'Saraki Bukola', 'Oshiomole Adams'])
#stafflist('Admin', ['Jimoh Wali Junior'])

#let us check if our codes work correctly




#lets create a basic decorator 
#what this decorator does is it adds salary to each staff in the staff list
def add_salary(func, amount):
	#lets define a wrapper function that modifies the employees list
	#and returnd yhe new list
	def wrapper(department, employees):
		#for loop to add salary string to each name in 
		#the employees list
		for employee in employees:
			employees[employees.index(employee)] = employee + ' to collect ' + str(amount)
		return func(department, employees)
	return wrapper


#lets decorate the stafflist function
new_stafflist = add_salary(stafflist, 10000)


#calling the decorated stafflist function
new_stafflist('Security', ['Mamud Inec', 'Bakare Peters'])


#lets check what we have
for key, values in dictionary_of_staff_in_department.items():
	print(key, values)