#Continue statement
x=1
while x<10:
    x=x+1
    if x>5:
        continue#we use continue we skip the execution of that given type of value like which are greater than 5
    print(x)
print('Out of loop')

#here we print numbers from 1-30 but skip the execution of num in the loop which are divisible by 3 or 5
for i in range(1,30):
    if i%3==0 or i%5==0:
        continue
    print(i)