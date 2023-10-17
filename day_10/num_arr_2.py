def check(str):
    max=0
    num_arr=[]
    res = [int(i) for i in str.split() if i.isdigit()]
    print(res)
    maxi=max(res)
    if(max<=len(str)):
        print(str[max])


s=input()
check(s)