from unittest import TestCase
from graph.directedgraph import DGraph


class TestBaseGraph(TestCase):
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
        self.g.add_edge(verts[1], verts[4], 1)

    def test_add_vertex(self) -> int:
        self.g.add_vertex("Z")
        pass

        #
        # self._graph_data._add(name)
        # self.__vertex_set._VertexSet__insert_vertex(name)
        # return self.vcount()
        # self.fail()
