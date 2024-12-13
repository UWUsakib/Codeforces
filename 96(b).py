import itertools
user=int(input())
p=[]
if user==1:
    p.append(4)
    p.append(7)
elif user==0:
    p.append(0)
else:
    l=len(str(user))
    
    pair=(l>>1)
    if l&(2-1)==0:
        for i in range(pair):
           p.append(4)
        for i in range(pair):
           p.append(7)
    else:
        pair+=1
        for i in range(pair):
           p.append(4)
        for i in range(pair):
           p.append(7)
allp=list(itertools.permutations(p))
allp=sorted(allp)
total=min(allp)
our=""
for i in total:
    our+=str(i)
print(int(our))