from collections import deque


def bfs(graph, start):
    """Return the BFS traversal order from start."""
    if start not in graph.adjacency:
        raise ValueError(f"Unknown starting vertex: {start}")

    visited = {start}
    queue = deque([start])
    order = []

    while queue:
        vertex = queue.popleft()
        order.append(vertex)

        for neighbor in graph.neighbors(vertex):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


def dfs(graph, start):
    """Return the recursive DFS traversal order from start."""
    if start not in graph.adjacency:
        raise ValueError(f"Unknown starting vertex: {start}")

    visited = set()
    order = []

    def visit(vertex):
        visited.add(vertex)
        order.append(vertex)

        for neighbor in graph.neighbors(vertex):
            if neighbor not in visited:
                visit(neighbor)

    visit(start)
    return order