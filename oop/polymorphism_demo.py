import math

class Shape:
    """Base class for different shapes."""
    
    def area(self):
        """Method to calculate area. To be overridden in derived classes."""
        raise NotImplementedError("Subclasses must implement this method.")

class Rectangle(Shape):
    """Class representing a rectangle."""
    
    def __init__(self, length, width):
        """Initialize rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of the rectangle."""
        return self.length * self.width

class Circle(Shape):
    """Class representing a circle."""
    
    def __init__(self, radius):
        """Initialize circle with radius."""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * (self.radius ** 2)
