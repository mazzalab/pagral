__author__ = ["Tommaso Mazza"]
__copyright__ = u"Copyright 2020, The Pagral Project"
__credits__ = [u"Ferenc Jordan"]
__version__ = u"1 beta"
__maintainer__ = u"Tommaso Mazza"
__email__ = "bioinformatics@css-mendel.it"
__status__ = u"Development"
__date__ = u"12/05/2020"
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

from abc import ABC, abstractmethod
from typing import Dict, List
from graph.vertex_set import VertexSet
from graph.attribute import Attribute
from graph.graph_data import IGraphData, GraphMatrix


def check_names(func):
    def wrapper(graph_data: IGraphData = None, names: List[str] = None, weighted: bool = False):
        if (graph_data and names and graph_data.elem() == len(names)) or \
                (graph_data and not names) or \
                (not graph_data and not names):
            func(graph_data, names, weighted)
        else:
            raise ValueError("graph_data and names must have the same size")

    return wrapper


class BaseGraph(ABC):
    @check_names
    def __init__(self, graph_data: IGraphData = None, names: List[str] = None, weighted: bool = False):
        """
        Base graph constructor which initializes:
        - _weighted boolean variable to account for weighted edges
        - _graph_data that references an IGraphData , which holds the actual graph data structure
        - __vertex_set that holds vertex names and attributes
        - __graph_attrs that refers to the set of global graph attributes
        :param graph_data: An optional IGraphData object holding the internal graph data structure
        :param names: An optional list of node names
        :param weighted: An optional flag that specifies whether the graph will be weighted or not
        """
        self._weighted: bool = weighted

        # Assign or create the proper internal IGraphData structure
        if graph_data:
            self._graph_data: IGraphData = graph_data
        else:
            if weighted:
                self._graph_data: IGraphData = GraphMatrix(weighted=True)
            else:
                self._graph_data: IGraphData = GraphMatrix(weighted=False)

        if not names:
            names: List[str] = [str(i) for i in range(self.vcount())]

        # Collection of vertices of the graph
        self.__vertex_set: VertexSet = VertexSet(names)

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
        if len(names) == self._size:
            self.__vertex_set = VertexSet(names)
        else:
            raise ValueError("The length of the list of names is incompatible with the graph size")

    @property
    def graph_data(self):
        return self._graph_data

    @graph_data.setter
    def graph_data(self, graph_data: IGraphData):
        self._graph_data = graph_data

    def vcount(self) -> int:
        return self._graph_data.elem()

    @abstractmethod
    def ecount(self) -> int:
        pass

    def is_weighted(self) -> bool:
        return self._weighted

    # Insert/delete methods
    def add_vertex(self, name: str) -> int:
        """
        Add a new vertex
        :param name: Name of the new vertex
        :return: The index of the inserted vertex
        """
        self._graph_data._add(name)
        self.__vertex_set._VertexSet__insert_vertex(name)
        return self.vcount()

    def delete_vertex(self, name):
        """
        Delete a vertex
        :param name: Name of the vertex to be deleted
        :return: The index of the deleted vertex
        """
        # TODO: elaborate more efficient strategy of node deletion as, e.g., nullify columns/rows instead of removing
        self._graph_data._delete(name)
        return self.__vertex_set._VertexSet__remove_vertex(name)

    @abstractmethod
    def add_edge(self, vertex_name1: str, vertex_name2: str):
        pass

    @abstractmethod
    def delete_edge(self, vertex_name1: str, vertex_name2: str):
        pass
