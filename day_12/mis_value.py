n=int(input())
arr=[0,1,8,4,3,5,2,6,10,9]
for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if(arr[j]>arr[j+1]):
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)
num=[]
i=1
for i in range(1,n):
    if(arr[i]!=i):
        num.append(i)
        i=i-1
print(num)  