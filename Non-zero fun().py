#Non-zero fun()
from numpy import*
a=array([11,22,0,33,-44])

#retrive indexing of non-zero elements of a
c=nonzero(a)
print(c)

#Display Indexes of non-zero elements
for i in c:
    print(i)

#Display Elements
print(a[c])