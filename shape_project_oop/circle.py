# circle class

from shapes import Shape
from math import pi

class Circle(Shape):
    def __init__(self,circumference,radius):
        self.__circumference = circumference
        self.__radius = radius

    def __str__(self):
        return f'This is a circle with radius of {self.__radius} and a circumference of {self.__circumference}.'    

     def __repr__(self):
         return 'Circle(radius={})'.format(self.__radius)

     def get_circumference(self):
         return self.__radius * self.__radius * pi

if __name__ == '__main__':
    user_input = input('Create a circle and add it a circumference : ')
    if user_input.isdecimal:
        try:
            

        
    else:
        print('You must enter a numeric value.')    
