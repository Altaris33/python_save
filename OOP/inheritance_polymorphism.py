#base class Animal
class Animal():

    def __init__():
        print("Animal Created")

    def who_am_i(self):
        print("I am an animal")  

    def eat(self):
        print("I am eating")     

my_animal = Animal()        
my_animal.who_am_i()
my_animal.eat()

# Derived Dog Class Inheritance Animal Class Methods -> derived Class -> have access to the base class methods
class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    # Override who_i_am method
    def who_am_i(self):
        print("I am a dog.") 

    def eat(self):
        print("I am dog and eating")       

    # Dog's own method
    def bark(self):
        print("Woof!")
# Instance of Dog Class -> inherit Animal's methods        
my_dog = Dog()
my_dog.eat()
my_dog.who_am_i()
my_dog.bark()

#POLYMORPHISM
# Dog Class
class Dog():

    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + " says woof!"    

class Cat():

    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + " says meow!"          

niko = Dog()   
felix = Cat()

print(niko.speak())
print(felix.speak())

# demontrating polymorphism using for loops to display the types (dog type or cat type) iterating through a list
for pet_class in [niko,felix]:

    print(type(pet_class))
    print(type(pet_class.speak()))

# demonstrating using a function which happens to be the most common way
def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)
pet_speak(felix)

# ABSTRACT CLASSES -> MORE ADVANCED but COMMON PRACTISE to use POLYMORPHISM
# An abstract class is a class that never expects to be instantiated : you never expect to create an instance of this class 
# It is designed to only serve as a base class
class Animal():

    def __init__(self,name):
        self.name = name
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")    

class Dog(Animal):

    def speak(self):
        return self.name = " says woof!"

class Cat(Animal):

    def speak(self):
        return self.name = " says meow!"

guetguet = Dog("Guetguet")
hya = Cat("Hya") 

guetguet.speak()
hya.speak()


# Practical ways of using abtsract classes and polymorphism :
    # When reading different files
        # Create a base class Open (there are lots of types of files, pdf, doc, txt...)
        # Create derived class for each type of file and inherit the same method for the open class but adapted 
