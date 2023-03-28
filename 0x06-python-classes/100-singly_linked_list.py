#!/usr/bin/python3
class Node:
    """Class that defines a node of a singly linked list
    
    Attributes:
        data (int): data to store in the node
        next_node (Node): reference to the next node in the list
    """
    
    def __init__(self, data, next_node=None):
        """Initialize a Node object
        
        Args:
            data (int): data to store in the node
            next_node (Node): reference to the next node in the list
        """
        if not isinstance(data, int):
            raise TypeError('data must be an integer')
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError('next_node must be a Node object')

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data stored in the node"""
        return self._data

    @data.setter
    def data(self, value):
        """Set the data stored in the node"""
        if not isinstance(value, int):
            raise TypeError('data must be an integer')

        self._data = value

    @property
    def next_node(self):
        """Get the reference to the next node"""
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """Set the reference to the next node"""
        if value is not None and not isinstance(value, Node):
            raise TypeError('next_node must be a Node object')

        self._next_node = value


class SinglyLinkedList:
    """Class that defines a singly linked list
    
    Attributes:
        head (Node): reference to the head node of the list
    """
    
    def __init__(self):
        """Initialize a SinglyLinkedList object"""
        self.head = None

    def __str__(self):
        """Print the entire list in stdout
        
        Print one node number by line
        """
        node = self.head
        output = ''
        while node is not None:
            output += str(node.data) + '\n'
            node = node.next_node

        return output.rstrip()

    def sorted_insert(self, value):
        """Insert a new node into the correct sorted position in the list (increasing order)
        
        Args:
            value (int): value to insert
        """
        node = Node(value)

        if self.head is None:
            self.head = node
            return

        if node.data < self.head.data:
            node.next_node = self.head
            self.head = node
            return

        prev_node = self.head
        curr_node = self.head.next_node
        while curr_node is not None:
            if node.data < curr_node.data:
                node.next_node = curr_node
                prev_node.next_node = node
                return

            prev_node = curr_node
            curr_node = curr_node.next_node

        prev_node.next_node = node
