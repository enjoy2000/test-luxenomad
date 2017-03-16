def test_sort(list):
    sorted_list = []
    while len(list):
        min = list[0]
        for value in list:
            if value <= min:
                min = value

        sorted_list.append(min)
        list.remove(min)

    return sorted_list


list = [1, 3, 4, 536, 13, 1234, 6, 31, 3, 5, 6]
print(test_sort(list))

