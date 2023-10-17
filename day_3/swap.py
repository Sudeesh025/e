a=100
b=200
a=a^b
b=b^a
a=a^b
print(a,b)
n=int(input())
k=int(input())
if(n&(1<<k-1)):
    print("set")
else:
    print("not set")