#Copying array
from numpy import*

a=arange(1,7)
b=a.copy()

print('Original Array:',a)
print('New Array:',b)

b[1]=60
#In copying Modifing one array will not effect other array

print('After Modifing')
print('Original Array:',a)
print('New Array:',b)