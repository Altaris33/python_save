# additions en base 12
# exercice et mise en exergue avec Python

# base decimal -> les nombres entiers sont écrit à l'aide des chiffres : 0,1,2,3,4,5,6,7,8,9
    # exemple -> 156 = 1 * 10 * 10 + 5 * 10 + 6

# base douze -> les nombres entiers sont écrit à l'aide de douze 'chiffres' : 0,1,2,3,4,5,6,7,8,9,A,B
    # A = 10 et B = 11. 
    # exemple -> 12 = 1 * 12 + 0 donc 12 = 10 en base 12
    #            22 = 1 * 12 + 10 donc 22 = 1A en base 12
    #            145 = 144 + 1 = 1 * 12 * 12 + 0 * 12 + 1 donc 145 = 101 en base 12
    #            563 =  3 * 12 * 12 + 10 * 12 + 11 donc 563 = 3AB en base 12     

# The following python program will display the base 12 value for any base 10 number
    # a dictionary will store all 12 values
def base_12(number1, value_base_12, base12):

    number1 = 22
    
    value_base_12 = {0 : 0, 1 : 1, 2 : 2, 3 : 3, 4 : 4, 5 : 5, 6 : 6, 7 : 7, 8 : 8, 9 : 9, 'A' : 10, 'B' : 11}

    return base12