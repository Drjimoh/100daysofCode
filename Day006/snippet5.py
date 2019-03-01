import pandas as pd 
import tempfile, os.path


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
#tmpdir = tempfile.gettempdir()
filename = "users.csv"
final_users_table.to_csv(filename, index=False)

df = pd.read_csv(filename)
print(df)