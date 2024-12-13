import itertools
user =int(input())
ucar=input()
arr=[]
for i in ucar:
    arr.append(i)
print(arr)
com=list(itertools.permutations(arr))
for i in com:
    print(i)