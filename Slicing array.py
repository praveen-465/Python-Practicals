#Slicing in arrays
#Indexing refers to Location of Elements
from array import*
x=array('i',[10,20,30,40,50,60,70,80])

#create an array y with elemnts from 1 to 3 elemts of x
y=x[1:4]
print(y)

 #create array y from 0th till last elemnt of x
y=x[0:]
print(y)

 #create array y with elements from 0-3 from x
y=x[:4]
print(y)

#create array y with last 4 elements of x
y=x[-4:]
print(y)

#create array starting with last 4 element,with 3 elements towards right  including 4th last
y=x[-4:-1]
print(y)

#create y with 0-7 elemnts with stepsize 2
y=x[0:8:2]
print(y)

#Display elements from 2-6 only
for i in x[2:7]:
    print(i)