# Laboratory Activity No. 12: Graph Traversals and Shortest-Path Routing

**Student Name:** Mary Jane Y. Reyna  
**Course:** CPEPRO8L – Data Structures and Algorithms  
**Academic Year:** First Semester, AY 2026–2027  
**Date:** October 27, 2026

## 1. Objectives

1. Represent unweighted and weighted graphs using adjacency lists.
2. Implement and trace Breadth-First Search (BFS) and Depth-First Search (DFS).
3. Implement Dijkstra's shortest-path algorithm using a priority queue.
4. Verify traversal and shortest-path results through automated tests and manual tracing.

## 2. Environment and Tools

- Python 3.11 or later
- Visual Studio Code
- Python standard libraries: `collections`, `heapq`, and `math`
- Windows terminal or PowerShell

## 3. Files Submitted

- `graph.py` – Implements the graph structure using adjacency lists.
- `traversals.py` – Implements BFS and DFS.
- `dijkstra.py` – Calculates shortest distances and reconstructs paths.
- `test_graph.py` – Runs the graph demonstration and automated tests.
- `README.md` – Contains documentation, results, and analysis.

## 4. Graph Model and Edge Table

The program uses an undirected, weighted campus-routing graph. Vertex G is an isolated vertex used to test unreachable destinations.

| Source | Destination | Weight |
|---|---|---:|
| A | B | 4 |
| A | C | 2 |
| B | C | 1 |
| B | D | 5 |
| C | D | 8 |
| C | E | 10 |
| D | E | 2 |
| D | F | 6 |
| E | F | 3 |

Each edge can be traversed in both directions because the graph is undirected.

## 5. Execution Commands

Open the project folder in VS Code and run:

```bash
py test_graph.py
```

The program displays the adjacency list, BFS and DFS traversal orders, shortest paths from A, and automated test results.

## 6. Traversal and Shortest-Path Results

### Breadth-First Search

Starting from A:

`A → B → C → D → E → F`

BFS uses a queue and visits vertices in increasing number of edges from the starting vertex.

### Depth-First Search

Starting from A:

`A → B → C → D → E → F`

DFS follows one branch as far as possible before backtracking. The same order as BFS occurs for this particular graph and alphabetical neighbor order; this is not always the case for other graphs.

### Dijkstra's Algorithm

Shortest paths from A:

| Destination | Distance | Shortest Path |
|---|---:|---|
| A | 0 | A |
| B | 3 | A → C → B |
| C | 2 | A → C |
| D | 8 | A → C → B → D |
| E | 10 | A → C → B → D → E |
| F | 13 | A → C → B → D → E → F |
| G | Unreachable | No path |

The shortest route from A to F has a total weight of 13.

Manual verification:

- A to B: A → C → B = 2 + 1 = 3.
- A to F: A → C → B → D → E → F = 2 + 1 + 5 + 2 + 3 = 13.

## 7. Automated Test Results

| Test Case | Expected Result | Observed Result | Status |
|---|---|---|---|
| Isolated vertex | Only G is visited | Only G is visited | PASS |
| Cycle | Traversal terminates without revisiting vertices | Traversal terminates correctly | PASS |
| Equal-cost alternatives | Minimum distance is 2 | Distance is 2 | PASS |
| Unreachable target | G has infinite distance | G is unreachable | PASS |
| Negative edge weight | Dijkstra rejects the graph | ValueError is raised | PASS |
| Shortest path verification | A to F has distance 13 | Distance is 13 | PASS |

All six automated tests passed.

## 8. Overall Output

## 9. Complexity Analysis

Let V represent the number of vertices and E represent the number of edges.

| Algorithm | Time Complexity | Auxiliary Space |
|---|---|---|
| BFS | O(V + E) | O(V) |
| DFS | O(V + E) | O(V) |
| Dijkstra with a binary heap | O((V + E) log V) | O(V) |

The adjacency-list graph itself requires O(V + E) space. These complexities assume the usual adjacency-list representation and a binary heap for Dijkstra.

## 10. Guide Questions and Answers

### 1. How does the queue make BFS behavior different from DFS stack behavior?

BFS uses a first-in, first-out queue, allowing it to explore nearby vertices before farther vertices. DFS uses a stack or recursion, which allows it to follow one branch deeply before returning to other branches.

### 2. Why must neighbor order be defined before comparing traversal results?

A consistent neighbor order ensures that the program produces predictable traversal sequences. Without a defined order, two correct implementations might visit the same vertices in different orders, making comparisons difficult.

### 3. Under what condition can BFS produce a shortest path, and what does it minimize?

BFS finds a shortest path when all edges have equal cost, such as in an unweighted graph. It minimizes the number of edges between the starting vertex and the destination.

### 4. Why is Dijkstra's algorithm invalid for graphs with negative edge weights?

Dijkstra assumes that once a vertex has the smallest tentative distance, its distance will not improve through later exploration. Negative edges can violate this assumption and lead to incorrect shortest-path results.

### 5. What is the benefit of storing predecessor information with distances?

Predecessors record the previous vertex on the selected shortest route. This allows the program to reconstruct the complete path instead of displaying only the minimum distance.

### 6. How do adjacency lists affect the complexity of BFS, DFS, and Dijkstra?

Adjacency lists store only existing edges, making them efficient for sparse graphs. BFS and DFS run in O(V + E), while heap-based Dijkstra runs in O((V + E) log V) under the standard binary-heap implementation.

### 7. Which test case gave the strongest evidence that the routing implementation is correct?

The shortest-path verification from A to F provided strong evidence because the program returned a distance of 13, which matches the sum of the edge weights along the reconstructed route. The unreachable-target and negative-weight tests also verified important boundary conditions.

## 11. Conclusion

This laboratory activity demonstrated how graphs can represent connections between locations and how graph algorithms can be used for traversal and routing. BFS and DFS successfully visited reachable vertices using a consistent neighbor order. Dijkstra's algorithm calculated shortest weighted paths, reconstructed routes using predecessor information, and identified unreachable vertices. The automated tests also verified handling of cycles, equal-cost alternatives, isolated vertices, and negative edge weights.

The results show that selecting the appropriate graph algorithm depends on whether the task involves reachability, minimum-edge paths, or minimum-total-weight routing.

