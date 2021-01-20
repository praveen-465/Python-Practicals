#Indexing in arrays
from array import*
x=array('i',[10,20,30,40])

#Find no.of elements in array
l=len(x)

print(x[0])#prints 1st element of array
print(x[1])#prints 2nd element of array

#display elements of array
print('Elements of array are:')
for i in range(l):
    print (x[i])