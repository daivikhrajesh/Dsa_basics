from collections import deque

def bfs(graph,start):
    
    queue = deque([start])

    visited = set()

    
    while queue:
        node = queue.pop()

        if node not in visited:
            visited.add(node)

            print(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

bfs(graph, 'A')
