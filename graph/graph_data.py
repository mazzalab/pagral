import numpy as np
from typing import Tuple
from abc import ABC, abstractmethod


class IGraphData(ABC):
    @abstractmethod
    def __getitem__(self, coords: Tuple[int, int]):
        pass

    @abstractmethod
    def __setitem__(self, coords: Tuple[int, int], weight):
        pass

    @abstractmethod
    def elem(self) -> int:
        pass

    @abstractmethod
    def size(self) -> int:
        pass

    @abstractmethod
    def count_nonzero(self):
        pass

    @abstractmethod
    def _add(self, name: str):
        pass

    @abstractmethod
    def _delete(self, name: str):
        pass


class GraphMatrix(IGraphData):
    def __init__(self, weighted: bool = False):
        if weighted:
            self._weighted = True
            self._adjmatrix: np.array = np.zeros((0, 0), dtype=np.float32)
        else:
            self._weighted = False
            self._adjmatrix: np.array = np.zeros((0, 0), dtype=np.bool)

    def __getitem__(self, coords: Tuple[int, int]):
        return self._adjmatrix[coords[0], coords[1]]

    def __setitem__(self, coords: Tuple[int, int], weight):
        self._adjmatrix[coords[0], coords[1]] = weight

    def elem(self) -> int:
        return self._adjmatrix.shape[0]

    def size(self) -> int:
        return self._adjmatrix.size

    def count_nonzero(self) -> int:
        return np.count_nonzero(self._adjmatrix)

    def _add(self, name: str) -> None:
        if self.elem() == 0:
            if self._weighted:
                self._adjmatrix = np.zeros((1, 1), dtype=np.float32)
            else:
                self._adjmatrix = np.zeros((1, 1), dtype=np.bool)
        else:
            if self._weighted:
                temp_adjmatrix = np.zeros((self.elem() + 1, self.elem() + 1), dtype=np.float32)
            else:
                temp_adjmatrix = np.zeros((self.elem() + 1, self.elem() + 1), dtype=np.bool)
            temp_adjmatrix[:-1, :-1] = self._adjmatrix
            self._adjmatrix = temp_adjmatrix

    def _delete(self, name: str) -> int:
        node_idx = self.V.get_index(name)
        self._adjmatrix = np.delete(self._adjmatrix, node_idx, 0)
        self._adjmatrix = np.delete(self._adjmatrix, node_idx, 1)
        return node_idx
