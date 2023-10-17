def binary(a,temp,s,h):
    mid=(s+h)//2
    if(a[mid]==temp):
        return mid
    elif(a[mid]>temp):
        return binary(a,temp,0,mid)
    elif(a[mid]<temp):
        return binary(a,temp,mid+1,len(a))
a=[1,2,3,4,5,6]
s=int(input())
s=binary(a,s,0,len(a))
print(s)