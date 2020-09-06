#cython: language_level=3
#distutils: language = c++

import numpy as np
cimport numpy as np
import cython

BTYPE = np.bool_
FTYPE = np.float32

cdef class AdjacencyMatrix:
    cdef np.ndarray adjmatrix
    cdef np.dtype adjtype
    cdef bint weighted

    def __init__(self):
        pass

    def __cinit__(self, int size = 0, bint weighted = False):
        self.weighted= weighted

        if self.weighted:
            self.adjmatrix = np.zeros((self.size, self.size), dtype=FTYPE)
            self.adjtype = np.dtype(FTYPE)
        else:
            self.adjmatrix = np.zeros((self.size, self.size), dtype=BTYPE)
            self.adjtype = np.dtype(BTYPE)

    def __str__(self):
        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in self.adjmatrix]))

    def __getitem__(self, tuple adjacent):
        return self.adjmatrix[adjacent[0], adjacent[1]]

    def __setitem__(self, tuple adjacent, int weight):  # : Tuple[int, int]
        self.adjmatrix[adjacent[0], adjacent[1]] = weight

    cpdef int size(self):
        return self.adjmatrix.shape[0]

    cpdef int nonzero_count(self):
        return np.count_nonzero(self.adjmatrix)

    cpdef tuple nonzero_idx(self):
        cdef tuple idx_tuple = np.nonzero(self.adjmatrix)
        return np.column_stack((idx_tuple[0], idx_tuple[1]))
        # or maybe it suffices to type: return np.transpose(np.nonzero(self.adjmatrix))  # TODO: test this statement

    cdef bint is_symmetric(self):
        if self.adjtype == np.dtype(BTYPE):
            return (self.adjmatrix.T == self.adjmatrix).all()
        else:
            return np.allclose(self.adjmatrix, self.adjmatrix.T, rtol=1e-05, atol=1e-08)

    cdef void symmetrize(self, bint upper=True):
        # Diagonal values are left untouched
        if upper:
            np.triu(self.adjmatrix) + np.tril(self.adjmatrix, -1).T
        else:
            np.tril(self.adjmatrix) + np.tril(self.adjmatrix, -1).T

    cpdef void expand(self, int n):
        cdef np.ndarray temp_adjmatrix = np.zeros((self.size() + n, self.size() + n), dtype=self.adjtype)
        if self.size() > 0:
            temp_adjmatrix[:-n, :-n] = self.adjmatrix
        self.adjmatrix = temp_adjmatrix

    @cython.boundscheck(False)
    @cython.wraparound(False)
    @cython.cdivision(False)
    cpdef void remove(self, list idx):
        idx.sort(reverse=True)
        cdef int i, val
        for i in range(len(idx)):
            val = idx[i]
            self.adjmatrix = np.delete(self.adjmatrix, val, 0)
            self.adjmatrix = np.delete(self.adjmatrix, val, 1)

