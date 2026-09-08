# BFS — Breadth-First Search

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node in visited:
            continue

        visited.add(node)
        print(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)


graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}

bfs(graph, "A")