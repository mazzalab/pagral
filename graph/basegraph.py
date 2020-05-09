__author__ = ["Tommaso Mazza"]
__copyright__ = u"Copyright 2020, The Pagral Project"
__credits__ = [u"Ferenc Jordan"]
__version__ = u"1 beta"
__maintainer__ = u"Tommaso Mazza"
__email__ = "bioinformatics@css-mendel.it"
__status__ = u"Development"
__date__ = u"06/05/2020"
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
from typing import Dict, List
from graph.vertex_set import VertexSet
from graph.attribute import Attribute


def mutex_args(func):
    def init_wrapper(self, size: int, adjmatrix: np.array, names: List[str], weighted):
        if size and adjmatrix:
            raise ValueError("size and adjmatrix arguments are mutually exclusive")
        func(self)

    return init_wrapper


class BaseGraph(ABC):
    @mutex_args
    def __init__(self, size: int = None, adjmatrix: np.array = None, names: List[str] = None, weighted: bool = False):
        self.__weighted: bool = weighted

        if size:
            self.__size = size
            if weighted:
                self.__adjmatrix: np.array = np.empty((size, size), dtype=np.float32)
            else:
                self.__adjmatrix: np.array = np.empty((size, size), dtype=np.bool)
        else:
            self.__size: int = adjmatrix.shape[0]
            self.__adjmatrix: np.array = adjmatrix

        if not names:
            names: List[str] = [str(i) for i in range(self.__size)]

        # Collection of vertices of the graph
        self.__vertex_set: VertexSet = VertexSet(names)

        # Global attributes of the graph
        self.__graph_attrs: Dict[str, Attribute] = {}

    def __getitem__(self, attr_key: str) -> Attribute:
        if isinstance(attr_key, str):
            return self.__graph_attrs[attr_key]
        else:
            raise TypeError('Index must be int, str or slice not {}'.format(type(attr_key).__name__))

    def __setitem__(self, attr_key: str, attr_value: Attribute):
        if isinstance(attr_key, str):
            self.__graph_attrs[attr_key] = attr_value
        else:
            raise TypeError('Index must be int, str or slice not {}'.format(type(attr_key).__name__))

    def size(self) -> int:
        return self.__size

    def vcount(self) -> int:
        return self.__adjmatrix[0] - 1

    @abstractmethod
    def ecount(self) -> int:
        pass

    def is_weighted(self) -> bool:
        return self.__weighted

    # Properties of vertices and edges
    @property
    def V(self):
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
        if len(names) == self.__size:
            self.__vertex_set = VertexSet(names)
        else:
            raise ValueError("The length of the list of names is incompatible with the graph size")

    # Insert/delete methods
    def add_vertex(self, name: str) -> int:
        """
        Add a new vertex
        :param name: Name of the new vertex
        :return: The index of the inserted vertex
        """
        temp_adjmatrix = np.zeros((self.__adjmatrix.shape[0] + 1, self.__adjmatrix.shape[1] + 1))
        self.__adjmatrix[:-1, :-1] = temp_adjmatrix
        self.__vertex_set._VertexSet__insert_vertex(name)
        return self.vcount()

    def delete_vertex(self, name):
        """
        Delete a vertex
        :param name: Name of the vertex to be deleted
        :return: The index of the deleted vertex
        """
        # TODO: elaborate more efficient strategy of node deletion as,e.g., nullify columns/rows instead of removing
        node_idx = self.V.get_index(name)
        self.__adjmatrix = np.delete(self.__adjmatrix, node_idx, 0)
        self.__adjmatrix = np.delete(self.__adjmatrix, node_idx, 1)
        self.__vertex_set._VertexSet__remove_vertex(name)
        return node_idx

    @abstractmethod
    def add_edge(self, vertex_name1: str, vertex_name2: str):
        pass

    @abstractmethod
    def delete_edge(self, vertex_name1: str, vertex_name2: str):
        pass
