n=int(input('enter a number : '))
for i in range(1,n):
    for j in range(n-1,i,-1):
        print(' ',end=' ')
    for k in range(1,i):
        print(k,end=' ')
    print()