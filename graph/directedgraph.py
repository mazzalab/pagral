import numpy as np
from graph.basegraph import BaseGraph


class DGraph(BaseGraph):
    def ecount(self):
        return np.count_nonzero(self._graph_data)

    def add_edge(self, source_vertex: str, target_vertex: str, weight=1):
        # TODO: check vertex names existing in graph
        src_idx = self.V.get_index(source_vertex)
        trg_idx = self.V.get_index(target_vertex)
        self._graph_data[src_idx, trg_idx] = weight

    def delete_edge(self, source_vertex: str, target_vertex: str):
        # TODO: check vertex names existing in graph
        src_idx = self.V.get_index(source_vertex)
        trg_idx = self.V.get_index(target_vertex)
        self._graph_data[src_idx, trg_idx] = 0
