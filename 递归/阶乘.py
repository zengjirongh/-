def jiecheng(n):
    if n == 1:
        return 1
    else:
        return n * jiecheng(n - 1)


if __name__ == '__main__':
    value = jiecheng(6)
    print(value)
