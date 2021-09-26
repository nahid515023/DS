def binary_search(data_list, first_index, lest_index, search_data):
    if lest_index >= first_index:
        mid = (first_index + lest_index)//2
        if data_list[mid] == search_data:
            return mid
        if data_list[mid] > search_data:
            lest_index = mid - 1
            return binary_search(data_list, first_index, lest_index, search_data)
        else:
            first_index = mid + 1
            return binary_search(data_list, first_index, lest_index, search_data)
    else:
        return -1


if __name__ == '__main__':
    data_list = [2, 3, 4, 10, 40]
    n = len(data_list)
    search_data = 2
    index = binary_search(data_list, 0, n, search_data)

    if index == -1:
        print('The value is not found.')
    else:
        print(f'Index of the value {data_list[index]} is :',index)

