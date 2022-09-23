n=int(input())
for i in range(1,n+1):
    for sp in range(0,i-1):
        print(" ",end='')
    for j in range(i,n+1):
        print("*",end='')
    print()
