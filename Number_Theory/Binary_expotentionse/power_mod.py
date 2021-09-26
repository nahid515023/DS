m=10**9
base,power=map(int,input().split())
result=1

while(power):
    if power%2==1:
        result=(base*result)%m
        power-=1
    else:
        base=(base*base)%m
        power/=2
print(result)

