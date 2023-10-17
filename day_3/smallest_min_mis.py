a=[3,-5,-6,0,5,7]
b=[]



for i in range(0,len(a)):
    if(a[i]>=0):
        b.append(a[i])

max=max(b)
n=len(b)
c=[]
store=[]
flag=0



for i in range (0,max):
    c.append(i)
    for j in range(n):
        if(c[i]==b[j]):
            flag=0
            break
        else:
            flag=1
    if(flag==1):
        store.append(c[i])
'''
for i in range(1,len(store)):
    minimum=store[0]
    if(store[i]<minimum):
        minimum=store[i]
print(minimum)
'''
print(min(store))