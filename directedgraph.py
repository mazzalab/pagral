import numpy as np
from abc import ABC, abstractmethod

class DGraph(BaseGraph):
    def __init__(self, numvertex:int):
        super.__init__()
    
    def set_vertex(self, vtx, id):
        if 0 <= vtx <= self.numvertex:
            self.vertices[id] = vtx
            self.verticeslist[vtx] = id

    @abstractmethod
    def set_edge(self, frm, to, cost=0):
        frm = self.vertices[frm]
        to = self.vertices[to]
        self.adjMatrix[frm][to] = cost
        # for directed graph do not add this
        self.adjMatrix[to][frm] = cost

    def get_vertex(self):
        return self.verticeslist

    def get_edges(self):
        edges = []
        for i in range(self.numvertex):
            for j in range(self.numvertex):
                if (self.adjMatrix[i][j] != -1):
                    edges.append(
                        (self.verticeslist[i], self.verticeslist[j], self.adjMatrix[i][j]))
        return edges

    def get_matrix(self):
        return self.adjMatrix