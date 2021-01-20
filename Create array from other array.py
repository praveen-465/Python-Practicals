#Creating an array from other array
from array import*
x=array('d',[1.5,-2.3,4.5,3])

#Use the same type code and multiply each elemnt with 3
arr2=array(x.typecode,(a*3 for a in x))
print('The elements of arrray 2 are:')
for i in arr2:
    print(i)

#here we are multiply by 3 ,U can multiply by any value ,to get same elements we can multiply by 1