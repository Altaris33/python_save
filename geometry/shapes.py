# shapes program using inheritance and polymorphism
import math

class Shape:

    def __init__(self, color='black', filled=False):
        self.__color = color
        self.__filled = filled

    def get_color(self):
        return self.__color

    def set_color(self, color):
        return self.__color = color

    def get_filled(self):
        return self.__filled

    def set_filled(self, filled):
        return self.__filled = filled

class Rectangle(Shape):

    def __init__(self, length, breadth):
        super().__init__()
        self.__length = length
        self.breadth = breadth

    def get_length(self):
        return self.__length

    def set_length(self,length):
        return self.__length = length

    def get_breadth(self):
        return self.__breadth

    def set_breadth(self,breadth):
        return self.__breadth = breadth

    def get_area(self):
        return self.__length * self.breadth

    def get_perimeter(self):
        return 2 * (self.__length + self.__breadth)            

# Circle implementation : calculate perimeter & circumference

class Circle(Shape):

    def __init__(self, radius):
        super().__init__()
        self.__radius = radius
        
    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        return self._radius = radius

    def get_area(self):
        return math.pi * self.__radius ** 2

    def get_perimeter(self):
        return 2 - math.pi * self.__radius


# Square implementation : calculate perimeter & area

class Square(Shape):

    def __init__(self, length):
        super().__init__()
        self.__length = length

    def get_length(self):
        return self.__length

    def set_length(self,length):
        return self.__length = length

    def get_perimeter(self):
        return self.__length * 4    

    def get_area(self):
        return self.__length ** 2    
