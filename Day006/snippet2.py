import pandas as pd 

columns = ['name', 'age', 'gender', 'job']

users1 = pd.DataFrame([
					['skibi', '30', 'M', 'musician'], 
					['Burna', '33', 'M', 'singer'],
					['JCole', '36', 'M', 'rapper']
					], columns=columns)

users2 = pd.DataFrame([
					['Joeboy', '20', 'M', 'musician'], 
					['Asa', '33', 'F', 'singer'],
					['Wayne', '39', 'M', 'rapper']
					], columns=columns)

users3 = pd.DataFrame(dict(name=['peter', 'john', 'sam', 'james'],
							age=['40', '23', '19', '33' ],
							gender=['M', 'M', 'M', 'M'],
							job=['Java Developer', 'Software Engineer', 'Security', 'Lawyer']	
						))

total_users = pd.concat([users1, users2, users3])
total_users.index= list(range(1,11))

users_height = pd.DataFrame(dict(name=total_users['name'],
								height= [160, 155, 145, 135, 172, 125, 140, 141, 142, 133]))
salary = pd.DataFrame(dict(
name=['skibi', 'Burna', 'JCole', 'Joeboy', 'Asa', 'Wayne',  'john', 'sam'],
salary= [100000, 200000, 300000, 10000, 3000000, 90000000, 400000, 10000]
))

incomplete_table = pd.merge(total_users, salary, on="name", how='outer')
#print(incomplete_table)

final_users_table = pd.merge(total_users, users_height, on="name")

stacked_final_table =pd.melt(final_users_table, id_vars="name", var_name = "variable", value_name= "Value")

#print(stacked_final_table)
#print(stacked_final_table.pivot(index="name", columns="variable", values="Value"))
#print(final_users_table.info())

#print(final_users_table.height, type(final_users_table.height))
#print(final_users_table['height'], type(final_users_table['height']))

#print(final_users_table[['height', 'gender', 'name']])
df = final_users_table.copy()

for i in range(final_users_table.shape[0]):
	df.loc[i, 'age'] =int(df.loc[i, 'age'])+ 1

users_below_30 = df[df.age < 30][['name', 'gender', 'job']]
male_users_below_30 = df[(df.age < 35) & (df.gender=='M')] 
female_users_below_30 = df[(df.age < 35) & (df.gender=='F')]
#or
#female_users_below_30 = df[(df.age < 35) & (df.gender!='M')] 

#print(female_users_below_30)
#print(final_users_table)
df = df.sort_values(by='age', ascending=False)
#print(df)

df.sort_values(by=['job', 'age'], inplace=True)
print(df.describe(include='object'))