loop=int(input())
for i in range(loop):
    total=0
    user1=input()
    n,k=list(map(int, user1.split()))
    arr=[0]*(k+1)
    for i in range(k):
        user2=input()
        p,t=list(map(int, user2.split()))
        arr[p]+=t
    arr.sort(reverse=True)
    for i in range(n):
        if i<k:
            total+=arr[i]
        else:
            break
    print(total)