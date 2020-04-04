# python file on OOP
# Plant class




class Plant():

    def __init__(self, name, color, age, location):
        self.name = name
        self.color = color
        self.age = age
        self.location = location

    def lifestyle(self):
        return "I have a lifestyle of 100!"

    #print(f'\n\nThe first plant is a {daffodil.name} and is of {daffodil.color} color.')
    def plant_info(self):
        return f'\n\nThis plant is a {self.name}, is {self.age} years old and is of {self.color} color.'  

    def is_your_birthday(self):
        self.age += 1 

    def location(self):
        return f'\n\n\tI am generally found in {self.location}.'

# daffodil inherit the base class called Plant
class Daffodil(Plant):
 
    def lifestyle(self):
        return "I come back every new Spring!"    

class Rose(Plant):

    def lifestyle(self):
        return "I am everywhere!"      

class Valerian(Plant):

    def lifestyle(self):
        return "I am in full blomm on summer..."
    







