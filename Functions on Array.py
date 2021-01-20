#Operations on Array Class
from array import*

#Create an array with Unicode Characters
a=array('u',['a','e','h','p','w','y'])
print('Original Array: ',a)

#append i and z to array a
a.append('i')
a.append('z')
print('After apppending i,z ',a)

#Inserting j at position number 2 in array a
a.insert(2,'c')
print('After inserting c at 2nd position',a)

#Removing an element 
a.remove('e')
print('After removing element e',a)

#Remove last element using pop() method
n=a.pop()
print('After using pop(): ',a)
print('Popped element: ',n)

#findindg positon of element using Index() method
i=a.index('h')
print('First occurance of element h is at:',i)

#convert an array into list using tolist() method
l=a.tolist()
print('List: ',l)
print('Array: ',a)