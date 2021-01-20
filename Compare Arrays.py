#Comparing Arrays
from numpy import*
a=array([10,20,30,40,50])
print('Array a',a)
b=array ([30,20,40,10,50])
print('Array b',b)

c=a==b
print('Result of a==b:',c)
c=a>b
print('Result of a>b:',c)
c=a<b
print('Result of a<b:',c)