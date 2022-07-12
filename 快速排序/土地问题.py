def area(n, m):
    if n > m:
        t = n
        n = m  # n为宽
        m = t  # m为长
    if m % n == 0:
        return n
    c = n
    k = m % n
    return area(c, k)


if __name__ == '__main__':
    chang = int(input("请输入土地的长度: "))
    kuan = int(input("请输入土地的宽度: "))

    n = area(chang, kuan)
    print(n)
