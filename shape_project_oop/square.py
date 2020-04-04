import math
from shapes import Shape

class Square(Shapes):
    def __init__(self, length):
        self.__length = length

    def __str__(self):
        return f'This is a square with length of {self.__length} and of perimeter {self.get_perimeter}'

    def get_length(self):
        return self.__length

    def set_length(self):
        self.__length = length

    def get_perimeter(self):
        return self.__length**2 

