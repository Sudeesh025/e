n=int(input("Enter the size of matrix:"))
r=0
c=n//2
matrix = [[0] * n for _ in range(n)]
for i in range(1,n**2+1):
    if matrix[r][c]!=0:
        r=r+1
        c=c-1
    matrix[r][c]=i

    nr=(r-1)%n
    nc=(c+1)%n
    if matrix[nr][nc]!=0:
        r=(r+1)%n
    else:
        r,c=nr,nc
print("The Magical matrix:")
for i in range(n):
    for j in range(n):
        print(matrix[i][j],end=" ")
    print()

print("\n")
for i in range(2,-1,-1):
    for j in range(3):
        print(matrix[i][j],end=" ")
    print()
for i in range(2,-1,-1):
    for j in range(3):
        print(matrix[i][j],end=" ")
    print()