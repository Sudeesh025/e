arr=[3,9,-2,8,7,6,5]
s_a=[1,]
m=max(s_a)
mini=min(s_a)-1
prefix_sum=[0,0,0,0,0,0,0]
for i in range(0,len(arr)):
    if(i==0):
        prefix_sum[i]=arr[i]
    else:
        prefix_sum[i]=arr[i]+prefix_sum[i-1]
print(prefix_sum)
total=prefix_sum[m]-prefix_sum[mini]
print(total)