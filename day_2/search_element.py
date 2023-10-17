def search(a,x):
    sum=0
    for i in range(len(a)):
        if(a[i]==x):
            print("element is found")
            return i
a=[]
length=int(input())
for i in range(0,length):
    x=int(input())
    a.append(x)
x=int(input("enter the value"))
print("At The index",search(a,x))