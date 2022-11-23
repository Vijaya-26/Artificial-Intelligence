def bfs(graph, root_node):
    visited = []
    frontier =[]
    visited.append(root_node)
    frontier.append(root_node)
    # print(node)
    # print(frontier)
    # print(visited)
    while(frontier):
        node = frontier.pop(0)
        print(node,end=" ")
        # visited.append(node)
        for i in graph[node]:
            if i not in visited:
                visited.append(i)
                frontier.append(i)
    # print(visited)
    # print(frontier)

if __name__ == '__main__':
    graph = {1:[2,3,4],
    2:[5,6],
    3:[],
    4:[7,8],
    5:[9,10],
    6:[],
    7:[11,12],
    8:[],
    9:[],
    10:[],
    11:[],
    12:[]
    }
    bfs(graph,1)