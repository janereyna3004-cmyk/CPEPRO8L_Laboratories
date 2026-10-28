class Graph:
    """Adjacency-list graph for directed or undirected edges."""

    def __init__(self, directed=False):
        self.directed = directed
        self.adjacency = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency:
            self.adjacency[vertex] = {}

    def add_edge(self, source, target, weight=1):
        if not isinstance(weight, (int, float)) or isinstance(weight, bool):
            raise ValueError("Edge weight must be a number.")

        self.add_vertex(source)
        self.add_vertex(target)

        self.adjacency[source][target] = weight

        if not self.directed:
            self.adjacency[target][source] = weight

    def neighbors(self, vertex):
        return sorted(
            self.adjacency.get(vertex, {}).keys()
        )

    def vertices(self):
        return sorted(self.adjacency.keys())

    def display(self):
        for vertex in self.vertices():
            edges = [
                f"{neighbor}({self.adjacency[vertex][neighbor]})"
                for neighbor in self.neighbors(vertex)
            ]
            print(f"{vertex}: {', '.join(edges) if edges else 'No neighbors'}")