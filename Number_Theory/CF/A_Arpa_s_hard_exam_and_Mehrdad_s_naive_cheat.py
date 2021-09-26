n = int(input())
r = 1
b = 8
while(n):
    if n % 2 == 1:
        r = (b*r)%10
        n -= 1
    else:
        b = (b*b)%10
        n /= 2
print(r)
