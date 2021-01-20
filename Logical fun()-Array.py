#Logical functions on array
#Using logical_and(),logical_or(),logical_not()
from numpy import*

a=array([10,20,3,0])
b=array([0,-20,30,10],)

c=logical_and(a>0,a<4)
print(c)

l=logical_or(b>=0,b==1)
print(l)

n=logical_not(a)
print(n)
