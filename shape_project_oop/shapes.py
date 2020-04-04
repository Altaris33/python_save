import math

class Shape():

    def __init__(self, color='black', filled=False):
        self.color = color
        self.filled = filled

    def get_color(self):
        return self.__color 

    def set_color(self, color):
        self.__color = color

    def get_filled(self):
        return self.__filled

    def set_filled(self,filled):
        self.__filled = filled
        
                       
        