#!/usr/bin/python3
""" class MyList that inherits from list """
class MyList(list):
    """
    A subclass of list that provides a print_sorted method to print the list in ascending order.
    """
    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
