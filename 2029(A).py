user=int(input())
for i in range(user):
    l,r,k=input().split()
    l=int(l)
    r=int(r)
    k=int(k)
    if l*k>r:
        print(0)
    else:
        print(((r//k)-l)+1)
