ls = [12, 11, 13, 5, 1, 6]

l = len(ls)

for i in range(1, l):
    j = i
    while ls[j-1] > ls[j] and j > 0:

        ls[j], ls[j-1] = ls[j-1], ls[j]
        j -= 1

print(ls)
