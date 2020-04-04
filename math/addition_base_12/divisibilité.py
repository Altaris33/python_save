# critère de divisibilité d'un nombre ou chiffre
    # 2 : un nombre est / par 2 lorsque le chiffre des unités est : 0,2,4,6 ou 8
import math

def check_divisibility_2(number,string_number,split_string,temp_number,result):

    number = int(input('Please enter a number to check if it is divisible by 2 : '))

    try:
        if number.isdecimal():
            string_number = str(number)
            split_string = string_number.split('')
            if split_string[-1] == '0' or split_string[-1] == '2' or split_string[-1] == '4' or split_string[-1] == '6' or \
               split_string[-1] == '8':
               temp_number = int(string_number.join())
               result = temp_number
               print(f'The number is divisibel by 2 and its result is {result}')

    except ValueError:
        print('Sorry the number passed was not correct in format or was not a number')
    else:
        print('Please provide a whole number')    

check_divisibility_2()        