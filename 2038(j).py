l=int(input())
p=0
b=0
for i in range(l):
    t, n = input().split()
    if t=="P":
        p+=int(n)
    else:
        b+=int(n)
        if (b-p)>0:
            print("YES")
            p-=p
            b=0
        else:
            print("NO")
            p-=b
            b=0


    