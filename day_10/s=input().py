s=input()
los=s.split(',')
num=[]
for i in los:
    nc=i.split(':')
    name=nc[0]
    code=nc[1]
    print(name,code)
    l=len(name)
    max=0
    for i in code:
        if int(i)>max and int(i)<=len(name):
            max=int(i)
    if(max==0):
        num+='X'
    else:
        num+=name[max-1]
print(num)