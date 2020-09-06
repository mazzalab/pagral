from pagral.graph.basegraph import BaseGraph


class UGraph(BaseGraph):
    def ecount(self):
        return self._adj_matrix.nonzero_count() / 2

    def add_edge(self, vertex1: str, vertex2: str, weight=1):
        # TODO: check vertex names existing in graph
        src_idx = self.V.get_index(vertex1)
        trg_idx = self.V.get_index(vertex2)
        self._adj_matrix[src_idx, trg_idx] = weight
        self._adj_matrix[trg_idx, src_idx] = weight

    def delete_edge(self, vertex1: str, vertex2: str):
        # TODO: check vertex names existing in graph
        src_idx = self.V.get_index(vertex1)
        trg_idx = self.V.get_index(vertex2)
        self._adj_matrix[src_idx, trg_idx] = 0
        self._adj_matrix[trg_idx, src_idx] = 0
