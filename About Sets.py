'''
Sets are written in flower bracets
To show that that sets only store a number once even if give more no.of times in that set
as it doesn't store duplicate  elements
To show that sets doesn't maintain order
'''
p={10,20,30,10,40,50,10,60}
print(p)
# you can update set datatype but not frozen sets
# the above point is the only difference between set and frozenset data types
s=set(p)
s.update([70,80])
print('After updating: ' ,p)
s.remove(20)
print('After removing: ',p)