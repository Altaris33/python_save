# main file

import random

def choose_starter():
    '''Allow the user to choose their starter pokemon'''
    print('Please, choose your starter pokemon')
    print('Type 1 for Chimchar, 2 for Piplup or 3 for Turtwig : ')
    choice = input("Enter the number of the choice you wish to make : ")

    if choice == '1':
        print('You choose Chimchar')
        chimchar = { 'name' : 'Chimchar', 'hp' : 20, 'attack': 16, 'defense' : 12}
    if choice == '2':
        print('You choose Piplup')
    if choice == '3':
        print('You choose Turtwig')
