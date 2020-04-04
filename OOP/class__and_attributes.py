# OOP programming

mylist = [1,2,3,4,5]

myset = set()

type(mylist)
type(myset)

# creating our own class Camel Casing
# classes are blueprint for objects
# objects are instances of a class and have their own methods
# and attributes (characteristics)
class Dog():
    
    # method called every time an instance of the class is created
    # Constructor of the class
    # Self = instance of the object itself
    def __init__(self,breed,name,spots):
        # Attributes 
        # Assign it using self.attribute_name = parameters passed
        self.breed = breed
        self.name = name
        self.spots = spots


# instance of classes 
my_dog = Dog(breed='Huskie',name='Sammy',spots=False)
#checking the type
type(my_dog)
my_dog.breed
my_dog.name
my_dog.spots

