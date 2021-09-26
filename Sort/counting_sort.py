def count_sort(ls):
    m = max(ls)
    l=m+1
    new_list = [0]*l
    for i in ls:
        new_list[i] += 1

    return new_list


def max(ls):
    max = 0
    for i in ls:
        if max < i:
            max = i
    return max


if __name__ == '__main__':
    ls = [5, 8, 4, 4, 3, 7, 8, 1, 2, 15, 11, 12, 12]
    ls = count_sort(ls)

    l=len(ls)
    
    for i in range(l):
        for j in range(ls[i]):
            print(i,end=' ')
