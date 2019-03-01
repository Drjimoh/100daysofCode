import pandas as pd 


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

df = pd.read_csv(url)

print(df.columns)

print(df.describe(include='all'))