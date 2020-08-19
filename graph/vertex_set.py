import numpy as np
from typing import List, Dict
from graph.attributes import Attributes


class VertexSet:
    def __init__(self, names: List[str]):
        # {index -> name}
        self.__idx: np.array = np.array(names)
        # {name -> index}
        self.__names: Dict[str, int] = {k: v for v, k in enumerate(names)}
        # {index -> attrs}
        self.__vertex_attrs: Dict[int, Attributes] = dict.fromkeys(range(len(names)), Attributes())

    def __getitem__(self, node) -> Attributes:
        """
        Get vertex :class:`Attribute` by vertex id or name
        :param node: Id or name of a selected vertex
        :return: The :class:`Attribute` of a selected vertex
        :raises KeyError: if the vertex id or name doesn't exist
        :raises TypeError: if ``node`` is not of type int (vertex id) or str (vertex name)
        """
        if isinstance(node, int):
            return self.__vertex_attrs[node]
        elif isinstance(node, str):
            return self.__vertex_attrs[self.__names[node]]
        else:
            raise TypeError('The `node` argument must be of type int or str, not {}'.format(type(node).__name__))

    def __setitem__(self, node, attributes: Attributes):
        """
        Set vertex :class:`Attribute` by vertex id or name
        :param node: Id or name of a selected vertex
        :param attributes: :class:`Attribute` to be set to the specified vertex
        :raises KeyError: if the vertex id or name do not exist
        :raises TypeError: if `node` is not of type int (vertex id) or str (vertex name)
        """
        if isinstance(node, int):
            self.__vertex_attrs[node] = attributes
        elif isinstance(node, str):
            self.__vertex_attrs[self.__names[node]] = attributes
        else:
            raise TypeError('The `node` argument must be of type int or str, not {}'.format(type(node).__name__))

    def get_names(self) -> List[str]:
        return list(self.__names.keys())

    def get_name(self, idx: int) -> str:
        return self.__idx[idx]

    def get_index(self, name: str) -> int:
        return self.__names[name]

    def __insert_vertex(self, name: str):
        self.__idx = np.append(self.__idx, name)
        self.__names[name] = self.__idx.size - 1
        self.__vertex_attrs[self.__idx.size - 1] = Attributes()

    def __remove_vertex(self, name: str):
        del_idx = self.__names[name]

        del self.__names[name]
        del self.__vertex_attrs[del_idx]
        del self.__idx[del_idx]

        #TODO: Need to update all indices, by rescaling them
