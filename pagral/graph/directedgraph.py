from graph.basegraph import BaseGraph


class DGraph(BaseGraph):
    def ecount(self):
        return self._adj_matrix.nonzero_count()

    def add_edge(self, source_vertex: str, target_vertex: str, weight=1):
        # TODO: check vertex names existing in graph
        src_idx = self.V.get_index(source_vertex)
        trg_idx = self.V.get_index(target_vertex)
        self._adj_matrix[src_idx, trg_idx] = weight

    def delete_edge(self, source_vertex: str, target_vertex: str):
        # TODO: check vertex names existing in graph
        src_idx = self.V.get_index(source_vertex)
        trg_idx = self.V.get_index(target_vertex)
        self._adj_matrix[src_idx, trg_idx] = 0
