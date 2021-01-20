#Aliasing array
#Aliasing is not Copying it's giving another name to it
from numpy import*

a=arange(1,6)#Arrange array with elements from 0-5
b=a#Another name to a is b

print('Original Array:',a)
print('Alias Array:',b)

b[1]=60#Modifing alias array will also modify Original Array

print('After Modifing')
print('Original Array:',b)
print('Alias Array:',b)
