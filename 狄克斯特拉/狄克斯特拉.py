graph = {}
"""a节点"""
graph["a"] = {}
graph["a"]["c"] = 5
graph["a"]["b"] = 2

"""b节点"""
graph["b"] = {}
graph["b"]["c"] = 8
graph["b"]["d"] = 7

"""c节点"""
graph["c"] = {}
graph["c"]["d"] = 2
graph["c"]["e"] = 4

"""d节点"""
graph["d"] = {}
graph["d"]["f"] = 1

"""e节点"""
graph["e"] = {}
graph["e"]["f"] = 3
graph["e"]["d"] = 6

"""f节点"""
graph["f"] = {}

"""节点权重"""
costs = {}
costs["b"] = 2
costs["c"] = 5
costs["e"] = float("inf")
costs["d"] = float("inf")
costs["f"] = float("inf")

"""父子节点"""
parents = {}
parents["b"] = 'a'
parents["c"] = "a"
parents["e"] = None
parents["d"] = None
parents["f"] = None

processed = []


def find_lowest_coast_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def find_min_node():
    node = find_lowest_coast_node(costs)
    while node is not None:
        cost = costs[node]  ##找出节点的权重
        neighbors = graph[node]  ##寻找邻居节点
        for n in neighbors.keys():  ##循环邻居节点
            new_cost = cost + neighbors[n]  ##到达邻居节点的权重
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_coast_node(costs)
    return costs, parents


if __name__ == '__main__':
    print(find_min_node())
