# Special Methods -> allow built-in methods on our objects
mylist = [4,5,6,7,8,9]
print(len(mylist))


class Sample():
    pass

my_sample = Sample()

# will return the script where the object is as well as its memory location
print(my_sample)

# Use built-in Python function on our own objects also called magic or dunder methods

class Book():

    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author} and has {self.pages}"  

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book object has been deleted")          

book1 = Book('Python rocks', 'Captain', 168)
print(book1)  
len(book1) 
del book1     

# Python displays the memory location as a string, therefore we can use special __str__ method to ask to return 
# a string representation of what is inside an object.
# 
# Same for length and delete to delete an object  
# str returns back the string representations of an object
# len returns back a length
# del allow to delete it from our memory
