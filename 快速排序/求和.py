def sum(list_item):
    if len(list_item) == 1:
        return list_item[0]
    return list_item[0] + sum(list_item[1:])


if __name__ == '__main__':
    sums = sum([2, 24, 56])
    print(sums)
