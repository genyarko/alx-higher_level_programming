"""

class Square:
    """
    A class used to represent a Square.
    
    Attributes
    ----------
    side : int
        The length of a side of the square.
    
    Methods
    -------
    area()
        Returns the area of the square.
    """
    def __init__(self, side):
        """
        Parameters
        ----------
        side : int
            The length of a side of the square.
        """
        self.side = side
    
    def area(self):
        """
        Returns the area of the square.
        """
        return self.side * self.side
