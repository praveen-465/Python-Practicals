# Prime number generator
min = int(input("Enter minimum number: "))
max = int(input("Enter Maximum number: "))

for i in range(min, max+1):
    if i>1:
        for j in range(2, i):
            if i%j == 0:
                break
        else:
            print(i)
print('These are the prime numbers between',min,'and',max)