def partition(arr, l, h):
    pivot = arr[l]
    i = l
    j = h
    while (i < j):
        while pivot >= arr[i]:
            i += 1
        while pivot < arr[j]:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[j], arr[l] = arr[l], arr[j]
    return j


def quick_sort(arr, l, h):
    if l < h:
        pivot = partition(arr, l, h)
        quick_sort(arr, l, pivot-1)
        quick_sort(arr, pivot+1, h)
    return arr


if __name__ == '__main__':
    arr = [5, 4, 7,3, 2, 10, 7, 8, 9, 1, 5]
    arr1= quick_sort(arr, 0, len(arr)-1)
    print(arr1)
