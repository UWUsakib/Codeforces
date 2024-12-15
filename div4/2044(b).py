u=int(input())
for i in range(u):
    x=input()
    siz=len(x)
    st=""
    for i in range(siz-1,-1,-1):
        if x[i]=="q":
            st+="p"
        elif x[i]=="p":
            st+="q"
        else:
            st+=x[i]
    print(st)
