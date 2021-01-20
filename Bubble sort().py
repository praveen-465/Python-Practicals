#Sorting an array using bubblesort technique
from array import*
#create an empty array to stote integers
x=array('i',[])

#store elements into array x
print('How many elements? ', end='')
n=int(input())

for i in range(n):
    print('Enter element: ',end='')
    x.append(int(input())) #add element to x

print('Original array: ',x)

#Bubble sort
for i in range(n-1):
    for j in range(n-1-i):
        if x[j] >x[j+1]:
            t=x[j]
            x[j]=x[j+1]
            x[j+1]=t

print('Sorted array: ',x)