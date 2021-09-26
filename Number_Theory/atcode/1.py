n = int(input())
ls = list(map(int,input().split()))
#l=ls.copy()
l=ls
l.sort()
for i in range(n):
    if l[n-2]==ls[i]:
        print(i+1)
        break
