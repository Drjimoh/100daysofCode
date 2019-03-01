import pandas as pd 
from sklearn import linear_model, metrics , model_selection

path = r'C:\Users\USER\Documents\codes\100 days of code\Day006\pima-indians-diabetes.data.csv'

df = pd.read_csv(path)
df.columns=['pregnant', 'pglucconc', 'DiastolicBP', 'Tricepskinft',
'2hrseruminsulin', 'BMI', 'DiabetesPedigree', 'Age', 'Dstatus']
df = df.dropna()
#splitting data into features and label
labels = df['Dstatus'] #label
feautures = df.drop(['Dstatus'], axis=1) #feautures

feautures_train, feautures_test, labels_train, labels_test = model_selection.train_test_split(
															feautures, labels,
															test_size=0.33, random_state=42)
clf = linear_model.LogisticRegression()
clf.fit(feautures_train, labels_train)
labels_predict = clf.predict(feautures_test)

print(metrics.accuracy_score(labels_test, labels_predict))


'''for i in range(labels_predict.shape[0]):
	if labels_predict[i] > 0.5 and labels_test.iloc[i] == 0:
		print("unreliable")
	elif labels_predict[i] < 0.5 and labels_test.iloc[i] == 1:
		print("unreliable")
	else:
		print("somewhat reliable")'''
	#print(labels_predict[i], labels_test.iloc[i])