aa=int(input())
a=[]
rem=0
for i in range(5):
    x=int(input())
    if((x>10) & (x<aa)):
        a.append(x)

print(a)
for i in range(0,len(a)):
    if(a[i]%2==0):
        rem=a[i]
        while(rem!=1):
            rem=rem/2
            if(rem==1):
                print(a[i])