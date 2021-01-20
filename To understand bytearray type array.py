#program to understand bytearray type array
Elements =12,23,34,56,78,90
p =bytearray(Elements)
for i in p:print(i)

print(p[4])
#you cannot edit byte array type array
#but you can modify it
p[0]=88   #replace 0th element with 88
for i in p: print( 'after modifying' ,i)