l=int(input())
for i in range(l):
    f=input()
    s=input()
    fs=len(f)

    ss=len(s)

    flag= True
    x=0
    while flag:

        if f[x]!=s[x]:
            flag=False
            if x!=0:
                x-=1


        x+=1
        if (x==fs) or (x==ss):
            flag=False
        
        
    print( (fs-x)+ (ss-x) + x +1)

