#!/usr/bin/python3
"""module that contains classes Node and SinglyLinkedList
"""



class Node:
    """class that defines a node of a singly linked list
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(data) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not value is None or type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """class that defines a singly linked list
    """
    def __init__(self):

    def head(self):
        return self.__head

    def sorted_insert(self, value):

