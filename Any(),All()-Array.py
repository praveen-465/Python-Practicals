#Using any() and all() functions
from numpy import*
a=array([10,20,30,40])
b=array([20,10,12,30])

c=a=b
print('Result of a=b is',c)

print('Check if any one element is true:',any(c))
print('Check if all elements are true:',all(c))