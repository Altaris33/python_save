# program that will display prime numbers

print('Welcome to the prime numbers displayer! \n ')

my_primes = {"One": 2, "Two": 3}

start = 3
end = 100

for value in range(start, end + 1):

    # if the number is divisible by any number
    # between 2 and value, it is not prime
    if value > 1:
        for n in range(2, value):
            if (value % n) == 0:
                break
        else:
            print(value)



