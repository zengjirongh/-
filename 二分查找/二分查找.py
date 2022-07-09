def binary_search(list_item, item):
    low = 0
    hight = len(list_item) - 1  ##索引从0开始，所以要减1
    i = 1
    while low <= hight:
        mid = (low + hight) // 2  ##取索引的中间值,向下取整
        guess = list_item[mid]  # 根据索引取值
        if guess == item:  # 如果跟item相等，则返回索引
            return mid, f"循找次数{i}"
        if guess > item:
            hight = mid - 1  # 如果索引对应的值比item大，
            i += 1
        else:
            low = mid + 1
            i += 1
    return "你想查找的值不在列表里面", f"循找次数{i}"


if __name__ == '__main__':
    items = int(input("请输入你想查找的值: "))
    max_value = int(input("请输入范围最大值: "))
    list_items = [i for i in range(0, max_value)]
    mid_index, i = binary_search(list_items, items)
    print(mid_index, i)
