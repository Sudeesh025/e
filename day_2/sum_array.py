def sum(a):
    summ=0
    for i in range(len(a)):
        summ=summ+a[i]
    return summ
a=[]
for i in range(0,6):
    x=int(input())
    a.append(x)
print(sum(a))