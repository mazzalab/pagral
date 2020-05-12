import numpy as np
from typing import List, Dict
from graph.attribute import Attribute


class VertexSet:
    def __init__(self, names: List[str]):
        # {index -> name}
        self.__idx: np.array = np.array(names)
        # {name -> index}
        self.__names: Dict[str, int] = {k: v for v, k in enumerate(names)}
        # {index -> attrs }
        self.__vertex_attrs: Dict[int, Attribute] = dict.fromkeys(range(len(names)), Attribute())

    def __getitem__(self, attr_key) -> Attribute:
        """
        Get vertex :class:`Attribute` by vertex id or name
        :param attr_key: Id or name of a selected vertex
        :return: The :class:`Attribute` of a selected vertex
        :raises KeyError: if the vertex id or name doesn't exist
        :raises TypeError: if ``attr_key`` is not of type int (vertex id) or str (vertex name)
        """
        if isinstance(attr_key, int):
            return self.__vertex_attrs[attr_key]
        elif isinstance(attr_key, str):
            return self.__vertex_attrs[self.__names[attr_key]]
        else:
            raise TypeError('`attr_key` argument must be of type int or str, not {}'.format(type(attr_key).__name__))

    def __setitem__(self, attr_key, attr_value: Attribute):
        """
        Set vertex :class:`Attribute` by vertex id or name
        :param attr_key: Id or name of a selected vertex
        :param attr_value: :class:`Attribute` to be set to the specified vertex
        :raises KeyError: if the vertex id or name doesn't exist
        :raises TypeError: if `attr_key` is not of type int (vertex id) or str (vertex name)
        """
        if isinstance(attr_key, int):
            self.__vertex_attrs[attr_key] = attr_value
        elif isinstance(attr_key, str):
            self.__vertex_attrs[self.__names[attr_key]] = attr_value
        else:
            raise TypeError('`attr_key` argument must be of type int or str, not {}'.format(type(attr_key).__name__))

    def get_names(self) -> List[str]:
        return list(self.__names.keys())

    def get_name(self, idx: int) -> str:
        return self.__idx[idx]

    def get_index(self, name: str) -> int:
        return self.__names[name]

    def __insert_vertex(self, name: str):
        self.__idx = np.append(self.__idx, name)
        self.__names[name] = self.__idx.size - 1
        self.__vertex_attrs[self.__idx.size - 1] = Attribute()

    def __remove_vertex(self, name: str):
        del_idx = self.__names[name]

        del self.__names[name]
        del self.__vertex_attrs[del_idx]
        del self.__idx[del_idx]
