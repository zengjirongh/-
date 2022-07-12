def quicklysort(arr):
    if len(arr) < 2:  ##基线条件
        return arr
    first = arr[0]  ##选一个基准值
    maxarr = [i for i in arr[1:] if i >= first]
    minarr = [i for i in arr[1:] if i < first]
    return quicklysort(minarr) + [first] + quicklysort(maxarr)


if __name__ == '__main__':
    list_item = [23, 657, 68, 7, 56, 34, 23, 54]
    print(quicklysort(list_item))
