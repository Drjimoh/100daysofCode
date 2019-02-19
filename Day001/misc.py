#I use this fi;e to test some piece of logic before adding it to the main code

staff = {}

dept_list = ['CBG', 'Chemistry', 'Physics']


for department in dept_list:	
	staff.update({department:None})

print(staff)