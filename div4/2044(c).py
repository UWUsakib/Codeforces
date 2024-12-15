u=int(input())
for i in range(u):

    tm=0
    user=input()
    m,a,b,c=list(map(int, user.split()))
    ts=2*m
    if m>a:
        ts-=a
        tm+=a
    else:
        ts-=m
        tm+=m
    if ts>=b:
        ts-=b
        tm+=b
    elif ts!=0:
        ts-=m
        tm+=m
    if ts>=c:
        tm+=c
    elif ts!=0:
        tm+=ts
    print(tm)
    