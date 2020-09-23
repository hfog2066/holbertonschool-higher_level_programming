#!/usr/bin/python3
"""
Singly linked list module!
Contains functions for creating a basic singly linked list.
"""


class Node:
    """
    Node class. Creates a node that holds data, and stores the location
    of the next node in the singly linked list.
    Init with an int and the next node in the list (optional)
    """
    def __init__(self, data, next_node=None):
        """
        Requires data (int), next_node optional
        """
        self.data = data
        self.next_node = next_node

        @property
        def data(self):
            """
            Data getter
            """
            return (self.__data)

        @data.setter
        def data(self, value):
            """
            Data setter
            """
            self.__check_data(value)
            self.__data = value

        @property
        def next_node(self):
            """
            Next_node getter
            """
            return (self.__next_node)

        @next_node.setter
        def next_node(self, next_node):
            """
            Next_node setter
            """
            self.__check_next(next_node)
            self.__next_node = next_node

        def __str__(self):
            """
            Returns data for str
            """
            return str(self.data)

    def __check_data(self, data):
        """
        Checks to ensure data type is int
        """
        if type(data) != int:
            raise TypeError("data must be an integer")

    def __check_next(self, next_node):
        """
        Ensure inputted next_node is a node or None
        """
        if next_node is not None and type(next_node) != Node:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """
    SLL class, for singly linked list. List is an ordered list of
    Node classes. Sorted_insert allows you to insert a new node
    in an ordered position.
    """
    def __init__(self):
        """
        SLL requires no init, starts empty
        """
        self.__head = None

    def __str__(self):
        """
        Returns list of Nodes
        """
        walk = self.__head
        ret = []
        while walk:
            ret.append(str(walk.data))
            walk = walk.next_node
        return ("\n".join(ret))

    def sorted_insert(self, value):
        """
        Inserts a new node in numerical order
        """
        walk = self.__head
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        if walk is None:
            self.__head = Node(value)
            return
        elif value < walk.data:
            self.__head = Node(value, walk)
            return
        while walk:
            if not walk.next_node:
                walk.next_node = Node(value)
                break
            if value < walk.next_node.data:
                walk.next_node = Node(value, walk.next_node)
                break
            walk = walk.next_node
