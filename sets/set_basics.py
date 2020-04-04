# set program
# 1 sets are a collection of unique elements

primes = {3,5,7,9,11,13,17,19,23,29}

print(type(primes))

print(f'The first prime numbers are {primes}')

# 2 Set using a constructor
# it will automatically remove all duplicates

unique=set("captainfalcon")

print(unique)
print(type(unique))

# 3 empty set creation

empty_set=set()
print(empty_set)
print(type(empty_set))


# 4 create a set from a list
prime_list = [3,5,7,11,13,17,19]
prime_set = set(prime_list)

print("Here are a set obtained from a cast from a list and the original list : \n")
print(type(prime_set))
print(type(prime_list))
print("\n\n")


# 5 Create Set from Tuple
my_tuple = (1,2,3,4,5,6,7,8,9,10,11,12,1,3,5,7,9,11)

num_set = set(my_tuple)

print("Here are a set obtained from a cast from a tuple and the original tuple : \n")
print(type(num_set))
print(f'{num_set}\n')

print(type(my_tuple))
print(f'{my_tuple}\n')
print("\n\n")


# 6 Access a specific value in a Set
# Set does not have indexes attached to it so we cannot access its elements like that.

# 7 Add items to a Set

new_set = {3,5,7,9}
print(new_set)
print('\n')
new_set.add(11)
new_set.add(13)
print(f'{new_set}\n')






