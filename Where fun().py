#Where fun()
from numpy import*
a=array([1,2,3,4,5])
y=array([12,1,3,40,0])

#If a>b then take elemnt from a else from b
c=where(a>y,a,y)
print(c)