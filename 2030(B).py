l=int(input())
for i in range(l):
    user=int(input())
    ft=1
    gt=user
    com=[0]
    p1=abs(ft-gt)-1
    if p1!=-1:
        com=[0]*gt
        com[p1]=1
    com= ''.join(map(str, com))
    print(com)