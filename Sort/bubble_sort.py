ls = [10, 5, 4, 2, 14]
l = len(ls)

for i in range(l):
    for j in range(l-i-1):
        if ls[j+1] < ls[j]:
            ls[j+1], ls[j] = ls[j], ls[j+1]

print(ls)
