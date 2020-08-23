import numpy as np
cimport numpy as np


BTYPE = np.bool_
FTYPE = np.float_

cdef class AdjacencyMatrix:
    def __cinit__(self, int size = 0, bint weighted = False):
        cdef np.ndarray adjmatrix
        cdef np.dtype atype

        if weighted:
            self.adjmatrix = np.zeros((size, size), dtype=FTYPE)
            self.atype = FTYPE
        else:
            self.adjmatrix = np.zeros((size, size), dtype=BTYPE)
            self.atype = BTYPE

    def __getitem__(self, tuple adjacents):
        return self.adjmatrix[adjacents[0], adjacents[1]]

    def __setitem__(self, tuple adjacents, int weight):  # : Tuple[int, int]
        self.adjmatrix[adjacents[0], adjacents[1]] = weight

    cdef int vcount(self):
        return self.adjmatrix.shape[0]

    cdef int ecount(self):
        return np.count_nonzero(self.adjmatrix)

    cdef void _add(self, int n):
        cdef np.ndarray temp_adjmatrix = np.zeros((self.vcount() + n, self.vcount() + n), dtype=self.atype)
        if self.vcount() > 0:
            temp_adjmatrix[:-n, :-n] = self.adjmatrix
        self.adjmatrix = temp_adjmatrix

    def _remove(self, list idx) -> None:
        # TOdO: SORT IDX AND REMOVE FROM BIGGER TO SMALLER
        cdef int i
        for i in idx:
            self.adjmatrix = np.delete(self.adjmatrix, i, 0)
            self.adjmatrix = np.delete(self.adjmatrix, i, 1)
