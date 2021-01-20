#Displaying numbers from 1-100 in proper format
for x in range (1,11):
    for y in range(1,11):
        print('{:8}'.format(x*y), end='')
    print()