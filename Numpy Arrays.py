#There are several ways to create array from numpy
from numpy import*
#creating array using linspace() function
a=linspace(0,10,5)
#divide 0 to 10 into 5 parts and take those points
print(a)

#creating array using logspace
x=logspace(1,4,5)
#divede the range: 10 power 1 to 10 power 4 into 5 equal parts and take those points
print(x)

#creating array using arrange() function
y=arange(2,11,2)
#take numbers starting from 2 to 11 with stepsize 2
print(y)

#Creating array using Zeros and ones function
a=zeros(5,int)
print(a)
b=ones(5) #default datatype is float
print(b)