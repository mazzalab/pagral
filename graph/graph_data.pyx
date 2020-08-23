import numpy as np
cimport numpy as np
import cython

BTYPE = np.bool_
FTYPE = np.float32

cdef class AdjacencyMatrixC:
    cdef np.ndarray adjmatrix
    cdef np.dtype atype
    cdef int size
    cdef bint weighted

    def __cinit__(self, int size = 0, bint weighted = False):
        self.size = size
        self.weighted= weighted

        if self.weighted:
            self.adjmatrix = np.zeros((self.size, self.size), dtype=FTYPE)
            self.atype = np.dtype(FTYPE)
        else:
            self.adjmatrix = np.zeros((self.size, self.size), dtype=BTYPE)
            self.atype = np.dtype(BTYPE)

    def __getitem__(self, tuple adjacents):
        return self.adjmatrix[adjacents[0], adjacents[1]]

    def __setitem__(self, tuple adjacents, int weight):  # : Tuple[int, int]
        self.adjmatrix[adjacents[0], adjacents[1]] = weight

    cpdef int vcount(self):
        return self.adjmatrix.shape[0]

    cpdef int ecount(self):
        return np.count_nonzero(self.adjmatrix)

    cpdef void add(self, int n):
        cdef np.ndarray temp_adjmatrix = np.zeros((self.vcount() + n, self.vcount() + n), dtype=self.atype)
        if self.vcount() > 0:
            temp_adjmatrix[:-n, :-n] = self.adjmatrix
        self.adjmatrix = temp_adjmatrix

    @cython.boundscheck(False)
    @cython.wraparound(False)
    @cython.cdivision(False)
    cpdef void remove(self, list idx):
        cdef local_idx = idx.sort(reverse=True)
        cdef int i, val
        for i in range(len(local_idx)):
            val = local_idx[i]
            self.adjmatrix = np.delete(self.adjmatrix, val, 0)
            self.adjmatrix = np.delete(self.adjmatrix, val, 1)
