def check(str):
    ob,oc,co,cc,op,cp,flag=1,1,1,1,1,1,1
    l=[]
    for i in str:
        l.append(i)
        if(i=='('):
            op=op+1
        if(i==')'):
            cp=cp+1

    while(op!=cp):
        if(op>cp):
            l.append(')')
            cp=cp+1
        print("missing ')'",)
    while(op!=cp):
        if(op<cp):
            l.append('(')
            op=op+1
        print("missing '('",)
    
    print(l)
    if(ob!=oc):
        flag=0
    return flag

str=input()
print(check(str))