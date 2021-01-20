#Largest and smallest number finder
num1 = int(input('Enter First number : '))
num2 = int(input('Enter Second number : '))
num3 = int(input('Enter Third number : '))
if (num1 > num2) and (num1 > num3):
    largest_num = num1
elif (num2 > num1) and (num2 > num3):
    largest_num = num2
else:
    largest_num = num3
print("The largest of the 3 numbers is : ", largest_num)
if(num1>num2) and (num3>num2):
    smallest_num=num2
elif(num2>num1) and (num3>num1):
    smallest_num=num1
else:
    smallest_num=num3
print('There smallest of 3 numbers is: ',smallest_num)