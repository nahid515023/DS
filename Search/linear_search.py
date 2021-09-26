def search(data_list, search_data):
    for i in range(len(data_list)):
        if data_list[i] == search_data:
            return i
    print('The value is not found in the list.')


if __name__ == '__main__':
    list_data = [10, 20, 80, 30, 60, 50,
                 110, 100, 130, 170]
    search_data = 60
    index = search(list_data, search_data)
    print('The value is present at index :',index)
