def merge_inversion(lst):
    global c
    if len(lst)<=1:
        return lst
    else:
        mid=len(lst)//2
        left=lst[:mid]
        right=lst[mid:]
        merge_inversion(left)
        merge_inversion(right)
        i=j=k=0
        while i<len(left) and j< len(right):
            if left[i]<right[j]:
                left[k]=right[j]
                i=i+1
                k=k+1
            else:
                lst[k]=right[j]
                c=c+len(left)-i
                j=j+1
                k=k+1
            while(i<len(left)):
                lst[k]=lst[i]
                i=i+1
                k=k+1
            while(j<len(right)):
                lst[k]=right[j]
                j=j+1
                k=k+1
            return c
lst=[2,8,3,4,25,6,18,9]
c=0
print(merge_inversion(lst))
