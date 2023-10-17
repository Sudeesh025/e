def check(str):
    ob,oc,co,cc,op,cp,flag=1,1,1,1,1,1,1
    l=[]
    for i in str:
        l.append(i)
        if(i=='['):
            ob=ob+1
        if(i==']'):
            oc=oc+1
        if(i=='{'):
            co=co+1
        if(i=='}'):
            cc=cc+1
    if(ob>oc):
        while(ob!=oc):
            l.append(']')
            oc=oc+1
        print("missing ']'",)
    if(ob<oc):
        while(ob!=oc):
            l.append('[')
            ob=ob+1
        print("missing '['",)
    if(co>cc):
        while(co!=cc):
            l.append('}')
            cc=cc+1
        print("missing '}'",)
    if(co<cc):
        while(co!=cc):
            l.append('{')
            co=co+1
        print("missing '{'",)
    if(op>cp):
        while(op!=cp):
            l.append(')')
            cp=cp+1
        print("missing ')'",)
    if(op<cp):
        while(op!=cp):
            l.append('(')
            op=op+1
        print("missing '('",)


    print(l)
    if(ob!=oc):
        flag=0
    return flag

str=input()
print(check(str))