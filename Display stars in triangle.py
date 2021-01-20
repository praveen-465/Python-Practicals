#to display stars in right angled triangle-nested loop
for i in range(1,11):
    for j in range(1,i+1):
        print('*',end=' ')#end=' '.so that cursor will not go to next line
    print()#so that cursor will come to next line
print(' ')

#to display stars in right angled triangle-for loop
for i in range(1,11):
    print('*'*(i)) #repeat star for i times