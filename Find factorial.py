#Find factorial -for loop
x=(int(input('Enter a number: ')))
f=1
if x==0:
    print('The factorial of 0 is 1')
elif x<0:
    print('There is no factorial for negative numbers')
else:
    for i in range(1,x+1):
        print(i)
        f=f*i
    print('The factorial of',x,'is',f)