def merge_sort(a):
    if(len(a)<=1):
        return a
    else:
        mid=len(a)//2
        left=a[:mid]
        right=a[mid:]
        merge_sort(left)
        merge_sort(right)
        i=j=k=0
        left_lst = list(left)
        right_lst = list(right)
        while(i<len(left_lst) & j<len(right_lst)):
            if(left_lst[i]<right_lst[j]):
                a[k]=left_lst[i]
                i=i+1
                k=k+1
            else:
                a[k]=right_lst[j]
                j=j+1
                k=k+1
            while(i<len(left_lst)):
                a[k]=left_lst[i]
                i=i+1
                k=k+1
            while(j<len(right_lst)):
                a[k]=right_lst[j]
                j=j+1
                k=k+1

a=[2,3,4,5,6]
merge_sort(a)
print(a)