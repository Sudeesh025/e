n=13
if(n&1==0):
    print("Even")
else:
    print("Odd")
n=int(input())
n1=0
n2=1
for i in range(0,n-1):
    n3=n2+n1
    n1=n2
    n2=n3
    print(n2)