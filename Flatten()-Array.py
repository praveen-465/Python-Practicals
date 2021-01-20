#Using Flatten() Method
# Using Flatten method we can convert array of any dimensions to 1 dimensions array
from numpy import*

a=array([[1,2,3,4],[6,7,8,9]])
print('Original Array:',a)

b=a.flatten()
print('Flattend Array:',b)