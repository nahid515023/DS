for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    c = 0
    for i in range(n):
        for j in range(a[i]-i-2, n,a[i]):
            if j>=0:
                if (a[i]*a[j]==i+j+2 and i<j):
                    c += 1
    print(c)
