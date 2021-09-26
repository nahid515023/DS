def multi(I, arr, n):
    r = [[None]*n]*n
    for i in range(n):
        for j in range(n):
            r[i][j] = 0
            for k in range(n):
                r[i][j] += I[i][k]*arr[k][j]

    return r


def power(arr, p, n):
    I = []
    for i in range(n):
        c = []
        for j in range(n):
            if i == j:
                c.append(1)
            else:
                c.append(0)
        I.append(c)

    while (p):
        if p % 2 == 1:
            arr = multi(I, arr, n)
            p -= 1
        else:
            arr = multi(arr, arr, n)
            p /= 2
    return arr


def main():
    arr = []
    n, p = map(int, input("Enter n & p: ").split())
    for i in range(n):
        c = []
        for j in range(n):
            c.append(int(input()))
        arr.append(c)

    m = power(arr, p, n)
    print(m)


if __name__ == '__main__':
    main()
