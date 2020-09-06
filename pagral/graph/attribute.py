class Attribute:
    def __init__(self):
        self.__attr = {}

    def __getitem__(self, attr_key):
        return self.__attr[attr_key]

    def __setitem__(self, attr_key, attr_value):
        self.__attr[attr_key] = attr_value

    def get_attributes_names(self):
        self.__attr.keys()
