xor=0
for i in range(1,9):
    xor=xor^i
print(xor)
def xor(n):
    
    xor=0
    if(n%4==0):
        return n
    elif(n%4==1):
        return 1
    elif(n%4==2):
        return n+1
    elif(n%4==3):
        return 0
n=int(input())
sum=xor(n)
a=int(input())
summ=xor(a)
print(sum^summ)