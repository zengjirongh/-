##阶乘
def jiecheng(n, sum):
    try:
        sum *= n
        n -= 1
        if n == 0:
            return sum
        return jiecheng(n, sum)
    except:
        return "请输入正确的值"


if __name__ == '__main__':
    try:
        jiec = int(input("你想求的阶乘数："))
        s = jiecheng(jiec, 1)
        print(s)
    except:
        print("请输入正确的值")
