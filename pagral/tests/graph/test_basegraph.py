import unittest
from graph.directedgraph import DGraph


class TestBaseGraph(unittest.TestCase):
    def setUp(self):
        self.g = DGraph()
        self.g.add_vertex("A")
        self.g.add_vertex("B")
        self.g.add_vertex("C")
        self.g.add_vertex("D")
        self.g.add_vertex("E")

        verts = self.g.V.get_names()
        self.g.add_edge(verts[0], verts[1], 1)
        self.g.add_edge(verts[0], verts[2], 1)
        self.g.add_edge(verts[0], verts[3], 1)
        self.g.add_edge(verts[1], verts[3], 1)
        self.g.add_edge(verts[1], verts[4], 2)

    def test_add_vertex(self):
        self.g.add_vertex("Z")
        self.assertTrue(self.g.V.exists_node("Z"))


if __name__ == '__main__':
    unittest.main()
