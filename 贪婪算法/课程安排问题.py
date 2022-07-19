carse_list = []


def search_min(graph):
    end = graph["英语"]["end"]
    for k, v in graph.items():
        ends = v["end"]
        if ends < end:
            end = ends
            carse_list.append(k)
            if len(carse_list) > 1:
                del carse_list[0]

    if len(carse_list) == 0:
        carse_list.append("英语")

    return end


def carse(graph):
    end = search_min(graph)
    for _ in range(len(graph)):
        for k, v in graph.items():
            if k not in carse_list:
                starts = v["start"]
                if starts == end:
                    carse_list.append(k)
                    end = v["end"]
                    break
    return carse_list


if __name__ == '__main__':
    graph = {'美术': {'start': 9, 'end': 10}, '英语': {'start': 9.3, 'end': 10.3}, '数学': {'start': 10, 'end': 11},
             '计算机': {'start': 10.3, 'end': 11.3}, '音乐': {'start': 11, 'end': 12}}
    anpai = carse(graph)
    print(anpai)
