#welcome to Day 8 of my 100 days of codes
#Today I will be working with all the datasets that
#comes with sklearn package
#follow me on twitter @_drjimoh

from sklearn.svm import SVC
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split 
import sklearn.datasets as dts 
import pandas as pd 


df =  dts.load_diabetes()
#print(df['target'])
#print(df['DESCR'])
target = pd.DataFrame(df['target'])
df = pd.DataFrame(df['data'])
df.columns = ['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']
#print(df.describe(include='all'))

df_train, df_test, target_train, target_test = train_test_split(df, target, 
												test_size=0.33, 
												random_state=1)

clf = LinearRegression()
clf.fit(df_train, target_train)
predictions = clf.predict(df_test)

print(predictions)
print(target_test)