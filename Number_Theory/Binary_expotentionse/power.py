
base,power=map(int,input().split())
result=1

while(power):
    if power%2==1:
        result*=base
        power-=1
    else:
        base*=base
        power/=2
print(result)

