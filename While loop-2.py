#while loop-Displays odd numbers from user's choice
x=int(input('Enter the minimum range: '))
y=int(input('Enter the maximum range: '))

if x % 2==0:
    x=x+1

while  x<=y :
    print(x)
    x=x+2