#Creating an array
#There are 3 ways to create an array

import array
x=array.array('i',[1,-5,6,-4])
for i in x:
    print(i)

import array as ar
a=ar.array('d',[0.12,-3.2,5.6,4])
for i in a:
    print(i)

from array import*
f=array('u',['a','f','s','y'])
for i in f:
    print (i)