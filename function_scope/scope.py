#this file shows the scope notion
#variable are handled by Python who will guess the values regarding scope 
# This follow the LEGB rule
x = 22

def printer():
    x = 60
    return x

#that will print x first defined 22
print(x)
#that will print the x defined in the printer() function since the function is here printed
print(printer())

#local variable
lambda num:num**2

#enclosing function local and global -> name variable will be redefined inside the greet() function 
#global
name = 'This is a global string'
def greet():
    #enclosing
    name = 'Captain'

    def hello():
        print('This is ' + name)
    hello()

greet() 

#global

#built-in -> do not override them examples -> len, str...
help(len)

#local
y = 50

def func(y):
    print(f'Y is {y}')
    #local reassignment
    y = 200
    print(f'I just locally changed Y to {y}')

func(y)    




