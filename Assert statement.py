#To understand assert statement
x=int(input('Enter a number greater than 0: '))
assert x>0,'Wrong input entered'#statement after assert is not necessary
print('You entered',x)

x=int(input('Enter a even number: '))
assert x%2==0
'''The statement written after assert will be printed with
    assertion error if input give by user is not satisfying condition in assert'''