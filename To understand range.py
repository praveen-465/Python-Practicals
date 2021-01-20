#to understand range
r=range(15)  #this will create a range object starting with 0 and ending with 14
for i in r:print (i)   #this will display elements of r

g=range(30,50,4)
for i in g:print('elements of g: ',(i))
'''
         this will create a range object starting with 30 and step size is 4
          step size mean that range will increase by 4 each time that means
           after 30 it will not print 31 it will print 34 i.e,4 increasing
            that means in bracets: 1st number is starting one       
                                              2nd number succesor of last number
                                              3rd umber is step size
 '''
x=range(10,1,-1)
for j in x:
    print(j)