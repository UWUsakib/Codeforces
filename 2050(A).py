us=int(input())
for i in range(us):
    user=input()
    n,m=list(map(int, user.split()))
    x=0
    for i in range(n):
        u1=input()
        m-=len(u1)
        if (m>=0):
            x+=1

    print(x)
