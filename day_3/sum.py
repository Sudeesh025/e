def sum(a,rem,N,l=[]):
    summ=40
    l=[]
    if(rem==0):
        return a
    if(rem>a[n-1]):
        return
    else:
        l=l+[a[N-1]]
        print(l)
        rem=rem-a[N]
        N=N-1
        if(len(a)>0):
            sum(a,rem,N,l)
arr=[6,8,9,5,4,3,26,2]
n=len(arr)
print(sum(arr,40,n))