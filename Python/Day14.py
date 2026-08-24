n= int(input())
i=1
c=0
for a in range(1,(n*2)):
    for k in range(n-i):
        print(" ",end="")
    for j in range(i):
        print("*",end=" ")
    if i==n or c==1:
        c=1
        i=i-1
    else:
        i+=1
    print()
n= int(input())
i=n
c=0
for a in range(1,(n*2)):
    for k in range(n-i):
        print(" ",end="")
    for j in range(i):
        print("*",end=" ")
    if i==1 or c==1:
        c=1
        i=i+1
    else:
        i-=1
    print()
n= int(input())
c=65
for i in range(1,n+1):
    for j in range(i):
        print(chr(c),end=" ")
        c=c+1
    print()