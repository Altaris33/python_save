#OOP programming
# class and objects methods(action) and attributes(characteristics)

#attributes can be common for certain objects of the class
# We will define them at class level
# we will create those attributes before the __init__ method.
class Dog():

    # CLASS OBJECT ATTRIBUTES -> same for any instance of the class
    # So we do not use the self keyword
    species = 'mammal'

    def __init__(self,breed,name):
        self.breed = breed
        self.name = name
        

    # Action -> METHODS (function inside a class)
    # Methods can take outside arguments which are not called using self because they are not provided in the constructor
    def bark(self,number):
        print("WOOF! My name is {}".format(self.name,number))

#calling objects and class attributes
my_dog = Dog('Huskie', 'Guetdon')
print(my_dog.species)
print(my_dog.name)


#calling an object's method, using parentheses
#Usually methods will play with objects attributes
#We use self to refer to an object's attributes or variable
my_dog.bark(10)


# Circle class
class Circle():

    # Class Object Attribute (true for all instances of the class)
    pi = 3.14

    # constructor with default value that can be overriden later on when an instance is called
    def __init__(self,radius=1):
        self.radius = radius
        self.area = radius*radius*self.pi    # possible to write self.area = radius*radius*Circle.pi because pi is a class attribute

    # Method
    def get_circumference(self):
        return self.radius self.pi * 2

# first instance of a circle
my_circle = Circle()   
# call off the pi attribute  -> 3.14
my_circle.pi
# call on the radius attribute -> 1 by default
my_circle.radius
# call on a second instance and overriding the radius parameter with 30 -> 30
my_circle2 = Circle(30)
# call on the method to calculate the circumference 
my_circle.get_circumference()   
# call on the area attribute passed in the constructor -> 
my_circle.area    

