import math
n = int(input())
if n > 2:
    gcd = math.gcd(n-1, math.gcd(n-2, (n-3)))
    x = (n*(n-1)*(n-2))//gcd
    print(x)
else:
    print(n)
