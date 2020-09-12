__author__ = ["Tommaso Mazza"]
__copyright__ = u"Copyright 2020, The Pagral Project"
__credits__ = [u"Ferenc Jordan"]
__version__ = u"0.1.2"
__maintainer__ = u"Tommaso Mazza"
__email__ = "bioinformatics@css-mendel.it"
__status__ = u"Development"
__date__ = u"12/09/2020"
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


from typing import Dict, List
from abc import ABC, abstractmethod
import numpy as np
from graph.vertex_set import VertexSet
from graph.edge_attribute import EdgeAttr
from graph.attribute import Attribute
from graph.adjacency_matrix import AdjacencyMatrix


def check_names(func):
    def wrapper(adj_matrix: AdjacencyMatrix = None, names: List[str] = None,
                directed: bool = False, weighted: bool = False):
        if adj_matrix and names and adj_matrix.size() != len(names):
            raise ValueError("graph_data and names must have the same size")
        else:
            func(adj_matrix, names, directed, weighted)
    return wrapper


class BaseGraph(ABC):
    @check_names
    def __init__(self, adj_matrix: AdjacencyMatrix = None, names: List[str] = None,
                 directed: bool = False, weighted: bool = False):
        """
        Base graph constructor which initializes:
        - _weighted boolean variable to account for weighted edges
        - _graph_data that references an IGraphData , which holds the actual graph data structure
        - __vertex_set that holds vertex names and attributes
        - __graph_attrs that refers to the set of global graph attributes
        :param adj_matrix: An optional IGraphData object holding the internal graph data structure
        :param names: An optional list of node names
        :param directed: An optional flag that specifies whether the graph will be directed or not
        :param weighted: An optional flag that specifies whether the graph will be weighted or not
        """
        self._weighted: bool = weighted
        self._directed: bool = directed

        # Assign or create an adjacency matrix
        if adj_matrix:
            self._adj_matrix: AdjacencyMatrix = adj_matrix
        else:
            if self._weighted and names:
                self._adj_matrix: AdjacencyMatrix = AdjacencyMatrix(size=len(names), weighted=True)
            elif self._weighted and not names:
                self._adj_matrix: AdjacencyMatrix = AdjacencyMatrix(size=0, weighted=True)
            elif not self._weighted and names:
                self._adj_matrix: AdjacencyMatrix = AdjacencyMatrix(size=len(names), weighted=False)
            else:
                self._adj_matrix: AdjacencyMatrix = AdjacencyMatrix(size=0, weighted=False)

        # Make the node names list
        if not names:
            names: List[str] = [str(i) for i in range(self.vcount())]

        # Collection of vertices of the graph
        self.__vertex_set: VertexSet = VertexSet(names)

        # Edge attributes
        self.__edge_attrs: EdgeAttr = EdgeAttr()

        # Global attributes of the graph
        self.__graph_attrs: Dict[str, Attribute] = {}

    def __getitem__(self, attr_name: str) -> Attribute:
        if isinstance(attr_name, str):
            return self.__graph_attrs[attr_name]
        else:
            raise TypeError('Index must be str, not {}'.format(type(attr_name).__name__))

    def __setitem__(self, attr_name: str, attr_value: Attribute):
        if isinstance(attr_name, str):
            self.__graph_attrs[attr_name] = attr_value
        else:
            raise TypeError('Index must be str, not {}'.format(type(attr_name).__name__))

    # Properties of vertices and edges
    @property
    def V(self) -> VertexSet:
        """
        Get the vertex set
        """
        return self.__vertex_set

    @V.setter
    def V(self, names: List[str]):
        """
        Create and set the vertex set
        :param names: List of names of vertices
        """
        if len(names) == self.vcount():
            self.__vertex_set = VertexSet(names)
        else:
            raise ValueError("The length of the list of names is incompatible with the graph size")

    @property
    def E(self) -> np.ndarray:
        return self.adjacency_matrix.nonzero_idx()

    @property
    def Eattrs(self):
        return self.__edge_attrs

    @Eattrs.setter
    def Eattrs(self, attrs: EdgeAttr):
        self.__edge_attrs = attrs

    @property
    def adjacency_matrix(self):
        return self._adj_matrix

    @adjacency_matrix.setter
    def adjacency_matrix(self, adj_matrix: AdjacencyMatrix):
        self._adj_matrix = adj_matrix

    def vcount(self) -> int:
        return self._adj_matrix.size()

    @abstractmethod
    def ecount(self) -> int:
        pass

    def is_weighted(self) -> bool:
        return self._weighted

    def is_directed(self) -> bool:
        return self._directed

    # Insert/delete methods
    def add_vertex(self, name: str) -> int:
        """
        Add a new vertex
        :param name: Name of the new vertex
        :return: The index of the inserted vertex
        """
        self._adj_matrix.expand(1)
        self.__vertex_set.insert_vertex(name)
        return self.vcount()

    def delete_vertex(self, name):
        """
        Delete a vertex
        :param name: Name of the vertex to be deleted
        :return: The index of the deleted vertex
        """
        # TODO: elaborate more efficient strategy of node deletion as, e.g., nullify columns/rows instead of removing
        self._adj_matrix._remove(name)
        return self.__vertex_set.remove_vertex(name)

    @abstractmethod
    def add_edge(self, vertex_name1: str, vertex_name2: str):
        pass

    @abstractmethod
    def delete_edge(self, vertex_name1: str, vertex_name2: str):
        pass
