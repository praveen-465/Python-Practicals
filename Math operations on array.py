# mathematical operations on array
# importing numpy
from numpy import*
a=array([10,20,30,40])

print('Original Array: ',a)
print('After adding 5',a+5)
print('After subtracting 5',a-5)
print('After multiplying with 5',a*5)
print('After dividing by 5',a/5)
print('After modulus with 4',a%4)
print('Expression value:',(a+5)**2)
a=a-3#By doing like this U can change the original array
print('Modified Array',a)


x=array([15,23,34])
y=array([10,12,23])
#While performing math operation on 2 arrays the no.of elements in both elements should be same
#Adding 2 arrays
print('Array x+Array y=',x+y)

#Subtracting 2 arrays
print('Array a-Array y=',x-y)

#Multiplying 2 arrays
print('Array x*Array y=',x*y)