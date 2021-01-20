#Indexing of Numpy Arrays
#Indexing refers to Location of Elements
from numpy import*

a=arange(10,16)
print(a)

#Retrive from 1-one element prior to 6th element with stepsize 2
b=a[1:6:2]
print(b)

#Display Elements Using Indexing
i=0
while i<len(a):
    print(a[i])
    i+=1
