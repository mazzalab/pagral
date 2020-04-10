__author__ = ["Tommaso Mazza"]
__copyright__ = u"Copyright 2020, The Pyntacle Project"
__credits__ = [u"Ferenc Jordan"]
__version__ = u"2 beta"
__maintainer__ = u"Tommaso Mazza"
__email__ = "bioinformatics@css-mendel.it"
__status__ = u"Development"
__date__ = u"27/03/2020"
__license__ = u"""
  Copyright (C) 2016-2020  Tommaso Mazza <t.mazza@css-mendel.it>
  Viale Regina Margherita 261, 00198 Rome, Italy

  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <https://www.gnu.org/licenses/>.
  """

import numpy as np
from abc import ABC, abstractmethod

class BaseGraph(ABC):
    def __init__(self, size:int, adjmatrix:np.array=None, weighted:bool=False):
        self._size = size

        # A structured array with a name of type string of length 10 abd an object containing node attributes
        self.V = np.empty(size, dtype={'names':('name', 'attrs'), 'formats':('U10', 'O')})
        self.nametoidx = {}

        # self.V[0] = ("tim", {})

        # self.vertices = {}
        # self.verticeslist = np.empty(size, np.object)
        if weighted:
            self.adjMatrix = -1 * np.ones((size, size), np.float)
        else:
            self.adjMatrix = np.zeros((size, size), np.bool)
        
    @property
    def size(self):
        return self._size
    
    def set_vertex(self, index, name):
        if 0 <= index < self.size:
            # self.V[]

            self.vertices[name] = index
            self.verticeslist[index] = name

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
        for i in range(self.size):
            for j in range(self.size):
                if (self.adjMatrix[i][j] != -1):
                    edges.append(
                        (self.verticeslist[i], self.verticeslist[j], self.adjMatrix[i][j]))
        return edges

    def get_matrix(self):
        return self.adjMatrix
