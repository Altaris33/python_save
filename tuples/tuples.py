# creating tuples

my_empty_tuple = ()
print(my_empty_tuple)

# first tuple containing number
# then we iterate through it and display its even numbers only 
my_first_tuple = (1,2,3,4,5,6,7,8,9)
print(my_first_tuple)
for even_number in my_first_tuple:
    if even_number % 2 == 0:
        print(even_number)

my_mixed_tuple = ("Captain", "Pico", 26, 28)
print(my_mixed_tuple)

my_nested_tuple = ("pilotes", ['captain',"pico","blackbite","didborn"], (26,28,30))
print(my_nested_tuple)