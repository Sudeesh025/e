b="2,5,3,4,1,2,7,8"
a=b.split(',')
for i in range(0,len(a)):
    a[i]=int(a[i])
sum2=''
sum=0
index=a.index(4)
index1=a.index(7)
for i in range(0,index):
    sum+=a[i]
for i in range(index1+1,len(a)):
    sum+=a[i]
for i in range(index,index1+1):
    sum2+=str(a[i])
print(sum+int(sum2))