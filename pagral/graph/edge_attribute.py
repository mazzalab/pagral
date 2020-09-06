from typing import Tuple
from pagral.graph.attribute import Attribute


class EdgeAttr:
    def __init__(self):
        pass

    def __getitem__(self, edge: Tuple) -> Attribute:
        pass

    def __setitem__(self, edge: Tuple, attributes: Attribute):
        pass
