def check(str):
    ob=1
    oc=1
    co=1
    cc=1
    op=1
    cp=1
    flag=1
    for i in str:
        if(i=='['):
            ob=ob+1
        if(i==']'):
            oc=oc+1
        if(i=='{'):
            co=co+1
        if(i=='}'):
            cc=cc+1
        if(i=='('):
            op=op+1
        if(i==')'):
            cp=cp+1
    if(ob!=oc):
        flag=0
    if(co!=cc):
        flag=0
    if(op!=cp):
        flag=0
    return flag




str=input()
print(check(str))