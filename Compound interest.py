#Compound Interest
print('Finding Compound Interest')
print()
print('Componded Annually (1)')
print('Compounded Half Yearly (2)')
x=int(input('Your choice (1) or (2)'))
print()
p=int(input('Enter prinicipal:'))
r=int(input('Enter Rate of interest:'))
t=int(input('Enter time in Years: '))
print()
if x==1:
    a=p*(1+r/100)**t
else :
    a=p*(1+r/200)**t

print('Compound Interest=',a-p)
print('Amount=',a)