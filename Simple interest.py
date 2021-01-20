p=int(input('Enter the prinicipal: '))
r=float(input('Enter the rate of interest: '))
t=int(input('Enter the time in Years: '))
I=p*r*t/100
print(f'Simple interest = Rs.',I)
A=p+I
print(f'Amount=Rs. ',A)