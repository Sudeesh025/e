

a=[6,0,3,5]
count=0
arr_2=[]
for i in range(4):
    for j in range(0,4-i-1):
        if(a[j]>a[j+1]):
            a[j],a[j+1]=a[j+1],a[j]
    count=count+1
    if(a==arr_2):
        break
    arr_2=a
print(count)
print(a)
