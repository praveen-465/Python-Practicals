#searh for an element
lst=[1,2,3,4,5]
x=int(input('Enter element to search: '))
for i in lst:
    if x==i:
        print('Element found from list')
        break
else:
    print('Element not found from list')