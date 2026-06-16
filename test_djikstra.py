import heapq
import unittest

class Graph:
    def __init__(self):
        self.content = {}

    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.content:
            self.content[from_node] = []

        if to_node not in self.content:
            self.content[to_node] = []

        self.content[from_node].append((to_node, weight))


class Dijkstra:
    def __init__(self):
        self.path = []
        self.shortest_distance = -1

    def find_shortest_path(self, start, finish, graph):

        distances = {node: float('inf') for node in graph.content}
        distances[start] = 0

        previous = {node: None for node in graph.content}

        pq = [(0, start)]

        while pq:

            current_distance, current_node = heapq.heappop(pq)

            if current_distance > distances[current_node]:
                continue

            if current_node == finish:
                self.shortest_distance = current_distance
                self.path = []

                while current_node is not None:
                    self.path.append(current_node)
                    current_node = previous[current_node]

                self.path.reverse()
                return


            for neighbor, weight in graph.content[current_node]:

                new_distance = current_distance + weight

                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = current_node

                    heapq.heappush(
                        pq,
                        (new_distance, neighbor)
                    )


        self.shortest_distance = -1
        self.path = []


class TestDijkstra(unittest.TestCase):

    def setUp(self):
        self.dijkstra = Dijkstra()


    def test_simple_path(self):

        g = Graph()
        g.add_edge('A', 'B', 1)
        g.add_edge('B', 'C', 2)
        g.add_edge('A', 'C', 4)

        self.dijkstra.find_shortest_path('A', 'C', g)

        self.assertEqual(
            self.dijkstra.shortest_distance,
            3
        )

        self.assertEqual(
            self.dijkstra.path,
            ['A', 'B', 'C']
        )

    def test_no_path(self):

        g = Graph()
        g.add_edge('A', 'B', 1)
        g.add_edge('C', 'D', 1)


        self.dijkstra.find_shortest_path('A', 'D', g)


        self.assertEqual(
            self.dijkstra.shortest_distance,
            -1
        )

        self.assertEqual(
            self.dijkstra.path,
            []
        )


    def test_start_is_finish(self):

        g = Graph()
        g.add_edge('A', 'B', 1)
        self.dijkstra.find_shortest_path('A', 'A', g)

        self.assertEqual(
            self.dijkstra.shortest_distance,
            0
        )

        self.assertEqual(
            self.dijkstra.path,
            ['A']
        )


    def test_complex_graph(self):

        g = Graph()

        g.add_edge('A', 'B', 10)
        g.add_edge('B', 'C', 10)
        g.add_edge('A', 'C', 100)

        self.dijkstra.find_shortest_path('A', 'C', g)
        self.assertEqual(
            self.dijkstra.shortest_distance,
            20
        )


if __name__ == "__main__":
    unittest.main()