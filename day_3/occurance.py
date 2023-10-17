arr=[1,5,1,2,3,4,2,8,8]
res=arr[0]
for i in range(0,9):
    res=res^arr[i]
print(res)
