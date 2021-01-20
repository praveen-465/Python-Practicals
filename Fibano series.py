#To get Fibano series
x=int(input('How many Fibaniccis ?'))
f1=0
f2=1
c=2
if x==1:
    print(f1)
elif x==2:
    print(f1,'\n' ,f2 ,sep='')
else:
    print(f1, '\n' ,f2,sep='')
    while c<x:
        f=f1+f2
        print(f)
        f1,f2=f2,f
        c=c+1