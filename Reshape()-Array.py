#Reshape() Method 
#Reshape method can be used to change shape of array
from numpy import*

a=array([-10,-12,14,13,-15,-16,-15,8])
print('Original Array:',a)

b=a.reshape(2,4)
print('Array After Reshaping:',b)