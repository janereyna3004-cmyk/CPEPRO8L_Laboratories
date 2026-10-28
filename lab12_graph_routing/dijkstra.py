import heapq
import math


def dijkstra(graph, start):
    """Return shortest distances and predecessors from start."""
    if start not in graph.adjacency:
        raise ValueError(f"Unknown starting vertex: {start}")

    # Dijkstra is only valid for nonnegative edge weights.
    for neighbors in graph.adjacency.values():
        for weight in neighbors.values():
            if weight < 0:
                raise ValueError(
                    "Dijkstra cannot process negative edge weights."
                )

    distances = {
        vertex: math.inf for vertex in graph.vertices()
    }
    predecessors = {
        vertex: None for vertex in graph.vertices()
    }

    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current = heapq.heappop(priority_queue)

        if current_distance > distances[current]:
            continue

        for neighbor in graph.neighbors(current):
            weight = graph.adjacency[current][neighbor]
            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                predecessors[neighbor] = current

                heapq.heappush(
                    priority_queue,
                    (new_distance, neighbor)
                )

    return distances, predecessors


def reconstruct_path(predecessors, start, target):
    """Reconstruct a shortest path, or return [] if unreachable."""
    if start not in predecessors or target not in predecessors:
        return []

    path = []
    current = target

    while current is not None:
        path.append(current)

        if current == start:
            path.reverse()
            return path

        current = predecessors[current]

    return []


def shortest_path(graph, start, target):
    """Return (distance, path) for a target."""
    distances, predecessors = dijkstra(graph, start)

    if math.isinf(distances[target]):
        return math.inf, []

    return distances[target], reconstruct_path(
        predecessors, start, target
    )