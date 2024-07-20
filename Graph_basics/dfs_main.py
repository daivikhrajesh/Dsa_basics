def dfs(graph,start):
    stack = [start]

    visited = set()

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)

            print(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    stack.append(neighbour)
                    #print(stack)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

dfs(graph, 'A')
