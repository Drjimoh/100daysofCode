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


final_users_table = pd.merge(total_users, users_height, on="name")


for i in range(final_users_table.shape[0]):
	final_users_table.loc[i, 'age'] = int(final_users_table.loc[i, 'age'])
#print(final_users_table[(final_users_table.age > 30) & (final_users_table.job == 'singer')])

#print(final_users_table.groupby('job')['age'].mean())
#print(final_users_table.groupby('job').describe(include='all'))

#for grp, data in final_users_table.groupby('job'):
#	print(grp, data)

df = final_users_table.append(final_users_table.iloc[1], ignore_index=True)

print(df.drop_duplicates())