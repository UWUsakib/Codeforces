user=input()
a,b=list(map(int, user.split()))
bros=[0,0,0]
bros[a-1]=1
bros[b-1]=1
for i in range(3):
    if bros[i]==0:
        print(i+1)
        break

