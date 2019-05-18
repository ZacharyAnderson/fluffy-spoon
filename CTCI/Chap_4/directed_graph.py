class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = dict()
        self.initiliaze_graph()

    def __repr__(self):
        return repr(self.graph)

    def initiliaze_graph(self):
        for i in range(self.vertices):
            self.graph[i] = list()

    def add_edge(self, node, vertice):
        if node in self.graph.keys():
            self.graph[node].append(vertice)
        else:
            raise Exception("Node is not in graph.")

    def is_route(self, node1, node2):
        visited = [False] * self.vertices
        # queue for BFS
        queue = list()

        queue.append(node1)
        visited[node1] = True

        while queue:
            # dequeue vertex
            vertex = queue.pop(0)

            # check if node just visited is destination
            if vertex == node2:
                return True

            # check all nodes that are connected to vertex
            for i in self.graph[vertex]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

        return False


if __name__ == "__main__":
    graph = Graph(4)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(2, 0)
    graph.add_edge(2, 1)
    graph.add_edge(1, 3)
    print(graph)
    print(graph.is_route(0, 1))
    print(graph.is_route(3, 1))
