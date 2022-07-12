from collections import deque

"""创建节点之间的联系"""
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

"""编写广度优先搜索函数"""


def manzutioajian(node):  ##满足条件
    if node[-1] == "m":
        return True


def search(name):
    search_queue = deque()  ##创建队列
    search_queue += graph[name]  # 向队列中添加节点
    search_list = []
    while search_queue:
        node = search_queue.popleft()
        if node not in search_list:
            if manzutioajian(node):
                return f"{node}符合条件"
            else:
                search_queue += graph[node]
                search_list.append(node)
    return "没有符合条件的结果"


if __name__ == '__main__':
    print(search("you"))