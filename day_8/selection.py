a=[12,8,2,19,69]
for i in range(0,len(a)):
    min_index=i
    for j in range(i+1,len(a)):
        if(a[min_index]>a[j]):
            t=a[min_index]
            a[min_index]=a[j]
            a[j]=t
print(a)
