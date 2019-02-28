import numpy as np 

x =  np.array([[1,2], [3,4]])
y = x.transpose()
print(x)
print(y)
print('''The result of multiplying the x and y 
	matrixes is {} and the result of adding 
	the two matrixes is {}'''
	. format(y * y, y+x))


new = np.zeros(10).reshape(-1,1)
print(new)

print(x, x.mean(axis=0))