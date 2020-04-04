# Fibonacci sequence printing

# Author : Jérémie LAERA

number_of_terms = int(input("How many terms do you wish to see? "))

# first 2 terms
number1, number2 = 0, 1
count = 0

# check if the number of terms is valid
if number_of_terms <= 0:
    print("Please enter a positive integer")
elif number_of_terms == 1:
    print(f"Fibonacci sequence up to {number_of_terms} : ")
    print(number1)
else:
    print("Fibonacci sequence : ")
    while count < number_of_terms:
        print(number1)
        nth = number1 + number2

        # update values and increment count 
        number1 = number2
        number2 = nth
        count += 1

