#Handling the AssertionError
x=int(input('enter a number greater than 0: '))
try:
    assert(x>0)
    print ('U entered',x)
except AssertionError:
    print('Wrong input')
    