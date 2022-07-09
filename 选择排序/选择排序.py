import random


def search_min(arr):
    min_num = arr[0]
    min_index = 0
    for i in range(1, len(arr)):
        if arr[i] < min_num:
            min_num = arr[i]
            min_index = i
    return min_index


def select_sort(arr):
    sort_list = []
    for _ in range(len(arr)):
        index = search_min(arr)
        sort_list.append(arr[index])
        del arr[index]
    return sort_list


if __name__ == '__main__':
    list_item = [i for i in range(1, 50)]
    random.shuffle(list_item)
    sort_lis = select_sort(list_item)
    print(sort_lis)

