#Slicing a Numpy Array
from numpy import*

a=arange(10,16)
print('Original Array a',a)

#Retrive from 1-5 elements with stepsize 2
b=a[1:6:2]
print('Retrived Array:',b)

#Retrive all elements 
c=a[::]
print('Retrived Array:',c)

#Retrive from 6-2=4th to 1 element prior to 4th element (6-2=4)
#Decreasing 1 stepsize
d=a[-2:2:-1]
print('Retrived Array:',d)

#Retrive from 0-one element prior to 4(6-2=4th)
e=a[:-2:]
print('Retrived Array:',e)