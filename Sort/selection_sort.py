ls = [10,5,12,2,7,9]
l = len(ls)
for i in range(l):
    min = i
    for j in range(i+1,l):
        if ls[min]>ls[j]:
            min=j
    ls[i],ls[min]=ls[min],ls[i]

print(ls)