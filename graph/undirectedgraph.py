import numpy as np
from typing import List
from abc import ABC, abstractmethod
from graph.basegraph import BaseGraph


class UGraph(BaseGraph):
    def __init__(self, size: int = None, adjmatrix: np.array = None, names: List[str] = None,  weighted: bool = False):
        super().__init__(size, adjmatrix, names, weighted)

    def ecount(self):
        pass

    def add_edge(self, vertex_name1: str, vertex_name2: str):
        pass

    def delete_edge(self, vertex_name1: str, vertex_name2: str):
        pass
