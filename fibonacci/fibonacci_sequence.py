# fibonacci sequence

# Author : Jérémie LAERA


def fib_seq(N):

    """ 
    Recrusively return the next term and the current term in the Fibonacci sequence
    """

    if N == 1:
        return [1, 0]
    else:
        terms = fib(N - 1)
        terms = [terms[0] + terms[1], terms[0]]
        return terms

def validate_positive_integer():
    """
    Asks the user for input and only return when a positive integer under 500 is given
    """

    while True:
        se = input("Which term in the Fibonacci sequence do you want to see? ")
        try:
            N = int(se)
            if N >= 500:
                print ("Enter a number smaller than 500.")
            elif N > 0:
                return N
            else:
                print("Entr a positive integer.")
        except ValueError:
            print("An error has occurred, please enter a positive integer.")

def main():
    N = validate_positive_integer()
    print (fib(N)[1])

if __name__ == "__main__":
    main()                        




