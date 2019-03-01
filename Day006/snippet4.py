import pandas as pd 

path = 'pima-indians-diabetes.data.csv'

df = pd.read_csv(path)
df.columns=['pregnant', 'plasma gluc conc', 'Diastolic BP', 'Tricep skin ft',
'2hr serum insulin', 'BMI', 'Diabetes Pedigree', 'Age', 'Dstatus']

query = df[(df.pregnant > 1) & (df.Dstatus == 1) & (df.Age > 50)]
#print(query)
print(query.isnull().sum())
print(df.notnull().sum())
df = df.dropna()
print(df.describe())