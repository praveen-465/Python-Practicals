#Creating view() for an array
#Viewing is creating another array with same elements
#Viewing is called shallow copying
from numpy import*
a=arange(1,6)#Create an arra from 1-5 elements
b=a.view()

print('Original Array:',a)
print('New Array:',b)

b[1]=60

print('After Modifing')
print('Original Array:',a)
print('New Array:',b)