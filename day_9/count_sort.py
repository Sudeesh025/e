a=[2,1,1,0,2,5,4,0,2,8,7,7,9,2,0,1,9]




a_2=[]
for i in range(0,len(a)):
    a_2.append(0)
print(a_2)
for i in a:
    a_2[i]=a_2[i]+1
print("count_array",a_2)
print()
for i in range(1,len(a)):
    a_2[i]=a_2[i]+a_2[i-1]
a_0=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
print("sum - count array ",a_2)
print()
for i in range(len(a)-1,-1,-1):
    a_2[a[i]]=a_2[a[i]]-1
    curr=a_2[a[i]]
    a_0[curr]=a[i]
print(a_2)
print("updated count array ",a_2)
print()
print("result array",a_0)