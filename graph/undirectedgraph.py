import numpy as np
from graph.basegraph import BaseGraph


class UGraph(BaseGraph):
    def ecount(self):
        return np.count_nonzero(self._graph_data) / 2

    def add_edge(self, vertex_name1: str, vertex_name2: str):
        pass

    def delete_edge(self, vertex_name1: str, vertex_name2: str):
        pass
