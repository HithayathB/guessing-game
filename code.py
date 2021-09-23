def check(n):
    if n==9:
        return 0;
    elif n==0:
        return 9;
    else:
        return(9-n);
    
a=input("Enter integer : ")
n=len(a)
a1=[]
for i in a:
    y=int(i)
    a1.append(y)
if a1[n-1]>0 and a1[n-1]!=1:
    c=a1[n-1]-2
    a1[n-1]=c
    a1.insert(0,2)
    print("This was the guessing answer :",end=" ")
    for i in a1: print(i,end="")
    print()
    print(a)
    s=2
    while(s>0):
        b=int(input())
        b2=rem=0
        while(b!=0):
            rem=b%10
            b2=b2*10+check(rem)
            b=b//10
            res=remainder=0
        while (b2 > 0):  
            remainder = b2 % 10  
            res = (res * 10) + remainder  
            b2 = b2 // 10 
        print("{:05d}".format(res))
        s-=1
    print("Answer is :",end=" ")
    for i in a1: print(i,end="")
else:
    print("Invalid number run again")

