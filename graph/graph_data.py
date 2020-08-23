import numpy as np
from typing import Tuple, List
from abc import ABC, abstractmethod


class IGraphData(ABC):
    @abstractmethod
    def __init__(self, size: int = 0, weighted: bool = False):
        if weighted:
            self._weight_type = np.float32
        else:
            self._weight_type = np.bool

    @abstractmethod
    def __getitem__(self, adjacents: Tuple) -> np.dtype:
        pass

    @abstractmethod
    def __setitem__(self, adjacents: Tuple, weight: int = 1) -> None:
        pass

    @abstractmethod
    def vcount(self) -> int:
        pass

    @abstractmethod
    def ecount(self) -> int:
        pass

    @abstractmethod
    def _add(self, n: int) -> None:
        pass

    @abstractmethod
    def _remove(self, idx: List[int]) -> None:
        pass


class AdjacencyMatrix(IGraphData):
    def __init__(self, size: int = 0, weighted: bool = False):
        super().__init__(size, weighted)
        self._adjmatrix: np.array = np.zeros((size, size), dtype=self._weight_type)

    def __getitem__(self, adjacents: Tuple[int, int]):
        return self._adjmatrix[adjacents[0], adjacents[1]]

    def __setitem__(self, adjacents: Tuple[int, int], weight: int = 1):
        self._adjmatrix[adjacents[0], adjacents[1]] = weight

    def vcount(self) -> int:
        return self._adjmatrix.shape[0]

    def ecount(self) -> int:
        return np.count_nonzero(self._adjmatrix)

    def _add(self, n: int) -> None:
        temp_adjmatrix = np.zeros((self.vcount() + n, self.vcount() + n), dtype=self._weight_type)
        if self.vcount() > 0:
            temp_adjmatrix[:-n, :-n] = self._adjmatrix
        self._adjmatrix = temp_adjmatrix

    def _remove(self, idx: List[int]) -> None:
        # TOdO: SORT IDX AND REMOVE FROM BIGGER TO SMALLER
        for i in idx:
            self._adjmatrix = np.delete(self._adjmatrix, i, 0)
            self._adjmatrix = np.delete(self._adjmatrix, i, 1)
