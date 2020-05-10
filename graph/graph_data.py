from abc import ABC, abstractmethod
import numpy as np
from typing import Tuple


class IGraphData(ABC):
    @abstractmethod
    def __getitem__(self, coords: Tuple[int, int]):
        pass

    @abstractmethod
    def __setitem__(self, coords: Tuple[int, int], weight):
        pass

    @abstractmethod
    def size(self) -> int:
        pass

    @abstractmethod
    def add(self, name: str):
        pass

    @abstractmethod
    def delete(self, name: str):
        pass


class WeightedMatrixData(IGraphData):
    def __init__(self):
        self._adjmatrix: np.array = np.zeros((0, 0), dtype=np.float32)

    def __getitem__(self, coords: Tuple[int, int]):
        return self._adjmatrix[coords[0], coords[1]]

    def __setitem__(self, coords: Tuple[int, int], weight):
        self._adjmatrix[coords[0], coords[1]] = weight

    def size(self) -> int:
        return self._adjmatrix.shape[0]

    def add(self, name: str) -> None:
        temp_adjmatrix = np.zeros((self.size() + 1, self.size() + 1), dtype=np.float32)
        self._adjmatrix[:-1, :-1] = temp_adjmatrix

    def delete(self, name: str) -> int:
        node_idx = self.V.get_index(name)
        self._adjmatrix = np.delete(self._adjmatrix, node_idx, 0)
        self._adjmatrix = np.delete(self._adjmatrix, node_idx, 1)
        return node_idx


class UnweightedMatrixData(IGraphData):
    def __init__(self):
        self._adjmatrix: np.array = np.zeros((0, 0), dtype=np.bool)

    def __getitem__(self, coords: Tuple[int, int]):
        return self._adjmatrix[coords[0], coords[1]]

    def __setitem__(self, coords: Tuple[int, int], weight):
        self._adjmatrix[coords[0], coords[1]] = weight

    def size(self) -> int:
        return self._adjmatrix.shape[0]

    def add(self, name: str) -> None:
        temp_adjmatrix = np.zeros((self.size() + 1, self.size() + 1), dtype=np.bool)
        self._adjmatrix[:-1, :-1] = temp_adjmatrix

    def delete(self, name: str) -> int:
        node_idx = self.V.get_index(name)
        self._adjmatrix = np.delete(self._adjmatrix, node_idx, 0)
        self._adjmatrix = np.delete(self._adjmatrix, node_idx, 1)
        return node_idx
