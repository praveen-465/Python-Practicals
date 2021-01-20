#Attributes of an Array
from numpy import*

a=array([1,2,3,4,5])
b=array([[1,2,3],[4,5,6]])
c=array([1.1,2.1,3.5,4,5.0])
d=array([[1,2,3],
               [4,5,6],
               [7,8,9]])
e=array(['u','f','a','b'])

# The ndim Attribute-gives no.of dimensions
print('ndim of Array a:',a.ndim)
print('ndim of Array b:',b.ndim)

#shape Attribute-for 1d aay gives no.of elelemnts,for 2d or more dimensional array gives no.of rows and columns
#You can change shape of array
print('shape of Array a:',a.shape)
print('Shape of Arrray b',b.shape)
print('Shape of Array d:',d.shape)
b.shape=(3,2)
print('Array b with 3 rows and 2 columns',b)

#size Attribute-gives total no.of elements
print('Size of Array a:',a.size)
print('Size of Arrayb',b.size)

#itemsize Attribute-gives memory size of array
print('Itemsize of Array a:',a.itemsize)
print('Itemsize of Array c:',c.itemsize)

#Dtype Attribute-gives datatype of the elements in array
print('Dtype of Array c:',c.dtype)
print('Dtype of Array d:',d.dtype)
print('Dtype of Array e:',e.dtype)

#Nbytes Attribute-gives total no.of bytes occupied
print('Ntype of Array d:',d.nbytes)
print('Ntype of Array e:',e.nbytes)