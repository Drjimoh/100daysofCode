import numpy as np


a = np.array([[1,2,3,4], [2,3,4,5], [1,2,3,4], [2,3,4,5], [1,2,3,4]]).reshape(10,2)
print(a)
b = a.copy()
print(b)
#print(b+np.array([[1,2,4,5],]))
