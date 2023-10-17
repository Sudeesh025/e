def linear(a,temp):
    for i in a:
        if(a[i]==temp):
            return i
a=[1,2,3,4,5,6]
s=int(input())
s=linear(a,s)
print(s)