def search_value(high):
    low = 0
    high = high
    while True:
        mid, yu = divmod(high + low, 2)
        if yu != 0:
            mid += 1
        print(f"猜值{mid}")
        item = int(input("请说明你心中的值比猜值大还是小(小用0表示,大用1表示),如果猜对了，请随便输入2退出 : "))
        if item == 0:
            high = mid
        if item == 1:
            low = mid
        if item == 2:
            break


if __name__ == '__main__':
    high_value = int(input("最大范围值: "))
    search_value(high_value)
