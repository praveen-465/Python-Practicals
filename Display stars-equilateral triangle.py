#to display stars in equilateral triangle-for loop
n=45
for i in range(1, 11):
    print(' '*n,end=' ')  #repeat spaces for n times and cusor don't go to next line
    print('*'*(i))  #repeat star for i times
    n=n-1
    
#for same output the source code can be make more smaller
n=40
for i in range(1,11):
    print(' '*(n-i) +'*'*(i))