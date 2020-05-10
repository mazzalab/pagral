import unittest
from graph.directedgraph import DGraph


class TestDGraph(unittest.TestCase):
    def setUp(self):
        self.g = DGraph()
        self.g.add_vertex("A")
        self.g.add_vertex("B")
        self.g.add_vertex("C")
        self.g.add_vertex("D")
        self.g.add_vertex("E")

        verts = self.g.V.get_names()
        self.g._graph_data[0, 1] = 1
        self.g._graph_data[0, 2] = 1
        self.g._graph_data[0, 3] = 1
        self.g._graph_data[1, 3] = 1
        self.g._graph_data[1, 4] = 1

    def test_ecount(self):
        self.assertEqual(self.g.ecount(), 5)

    def test_add_edge(self):
        verts = self.g.V.get_names()

        self.g.add_edge(verts[2], verts[1])
        src = self.g.V.get_index(verts[2])
        trg = self.g.V.get_index(verts[1])
        self.assertEqual(self.g._graph_data[src, trg], 1)

        self.g.add_edge(verts[2], verts[3], 10)
        src = self.g.V.get_index(verts[2])
        trg = self.g.V.get_index(verts[3])
        self.assertEqual(self.g._graph_data[src, trg], 1)

    def test_delete_edge(self):
        verts = self.g.V.get_names()

        self.g.delete_edge(verts[2], verts[1])
        src = self.g.V.get_index(verts[2])
        trg = self.g.V.get_index(verts[1])
        self.assertEqual(self.g._graph_data[src, trg], 0)

        self.g.delete_edge(verts[2], verts[3])
        src = self.g.V.get_index(verts[2])
        trg = self.g.V.get_index(verts[3])
        self.assertEqual(self.g._graph_data[src, trg], 0)

#
# if __name__ == '__main__':
#     unittest.main()
