#Searching for the position of the element in array

from array import*
x=array('i',[])

print('How many elements?',end='')
j=int(input())

for i in range(j):
    print('Enter Element:',end='')
    f=int(input())
    x.append(f)
print('Original array: ',x)

print('Enter element to search: ',end='')
e=int(input())

for i in range(len(x)):
    if x[i]==e:
        print('The element',e,'is found at Position',i+1)
        break
else:
    print(e,'Not found in array')