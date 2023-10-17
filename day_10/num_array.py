
def num_array(n):
    arr=[]
    arr_2=[]
    while(n!=0):
        rem=n%10
        arr.append(rem)
        n=n//10
    print(arr)
    len=0

    
    arr_2=arr[::-1]
    print(arr_2)
    arr_0=[]

    arr_0.append(arr_2[1::2])
    return arr_0

nums=int(input())
arr_0=num_array(nums)
print(arr_0)
for i in range(0,3):
    num=pow(arr_0[i],2)
    arr_0.append(num)
print(arr_0[0::4])