import numpy as np
from graph.basegraph import BaseGraph


class UGraph(BaseGraph):
    def ecount(self):
        return self._graph_data.ecount() / 2

    def add_edge(self, vertex1: str, vertex2: str, weight=1):
        # TODO: check vertex names existing in graph
        src_idx = self.V.get_index(vertex1)
        trg_idx = self.V.get_index(vertex2)
        self._graph_data[src_idx, trg_idx] = weight
        self._graph_data[trg_idx, src_idx] = weight

    def delete_edge(self, vertex1: str, vertex2: str):
        # TODO: check vertex names existing in graph
        src_idx = self.V.get_index(vertex1)
        trg_idx = self.V.get_index(vertex2)
        self._graph_data[src_idx, trg_idx] = 0
        self._graph_data[trg_idx, src_idx] = 0
