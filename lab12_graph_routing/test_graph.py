import math

from graph import Graph
from traversals import bfs, dfs
from dijkstra import dijkstra, shortest_path


def build_sample_graph():
    graph = Graph(directed=False)

    # Weighted campus-routing example
    edges = [
        ("A", "B", 4),
        ("A", "C", 2),
        ("B", "C", 1),
        ("B", "D", 5),
        ("C", "D", 8),
        ("C", "E", 10),
        ("D", "E", 2),
        ("D", "F", 6),
        ("E", "F", 3),
    ]

    for source, target, weight in edges:
        graph.add_edge(source, target, weight)

    # Isolated vertex
    graph.add_vertex("G")

    return graph


def run_tests():
    print("\nAUTOMATED TESTS")

    # Test 1: Isolated vertex
    graph = build_sample_graph()
    assert bfs(graph, "G") == ["G"]
    assert dfs(graph, "G") == ["G"]
    print("[PASS] Isolated vertex")

    # Test 2: Cycle
    cycle = Graph()
    cycle.add_edge("A", "B")
    cycle.add_edge("B", "C")
    cycle.add_edge("C", "A")
    assert bfs(cycle, "A") == ["A", "B", "C"]
    print("[PASS] Cycle")

    # Test 3: Equal-cost alternatives
    equal = Graph()
    equal.add_edge("A", "B", 1)
    equal.add_edge("A", "C", 1)
    equal.add_edge("B", "D", 1)
    equal.add_edge("C", "D", 1)

    distance, path = shortest_path(equal, "A", "D")
    assert distance == 2
    assert path in (["A", "B", "D"], ["A", "C", "D"])
    print("[PASS] Equal-cost alternatives")

    # Test 4: Unreachable target
    graph = build_sample_graph()
    distances, predecessors = dijkstra(graph, "A")
    assert math.isinf(distances["G"])
    assert shortest_path(graph, "A", "G") == (math.inf, [])
    print("[PASS] Unreachable target")

    # Test 5: Negative weights must be rejected
    negative = Graph(directed=True)
    negative.add_edge("A", "B", -1)

    try:
        dijkstra(negative, "A")
        raise AssertionError("Negative weight was not rejected.")
    except ValueError:
        print("[PASS] Negative weight rejection")

    # Test 6: Expected shortest route
    distance, path = shortest_path(graph, "A", "F")
    assert distance == 13
    assert path == ["A", "C", "B", "D", "E", "F"]
    print("[PASS] Shortest path verification")

    print("All 6 tests passed.")


def main():
    graph = build_sample_graph()

    print("LABORATORY ACTIVITY NO. 12")
    print("GRAPH TRAVERSALS AND SHORTEST-PATH ROUTING")
    print("=" * 48)

    print("\nGRAPH ADJACENCY LIST")
    graph.display()

    print("\nTRAVERSAL RESULTS")
    print("BFS from A:", " -> ".join(bfs(graph, "A")))
    print("DFS from A:", " -> ".join(dfs(graph, "A")))
    print("BFS from C:", " -> ".join(bfs(graph, "C")))
    print("DFS from C:", " -> ".join(dfs(graph, "C")))

    print("\nDIJKSTRA SHORTEST PATHS FROM A")
    distances, predecessors = dijkstra(graph, "A")

    for target in graph.vertices():
        distance, path = shortest_path(graph, "A", target)

        if math.isinf(distance):
            print(f"A -> {target}: Unreachable")
        else:
            route = " -> ".join(path)
            print(f"A -> {target}: distance = {distance}, path = {route}")

    print("\nROUTING ANALYSIS")
    print("BFS minimizes the number of edges in an unweighted graph.")
    print("Dijkstra minimizes total weight for nonnegative edge weights.")
    print("DFS explores a branch before backtracking.")

    run_tests()


if __name__ == "__main__":
    main()