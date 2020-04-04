#This program is a tictactoe project
import random


#This function is responsible for displaying the board based on a numpad 

def display_board(board):
    """ DISPLAY THE BOARD """
    print('\n'*100)
    print(board[7]+' |'+board[8]+'  | '+board[9])
    print('--|---|--')
    print(board[4]+' |'+board[5]+'  |'+board[6])
    print('--|---|--')
    print(board[1]+' |'+board[2]+'  | '+board[3])


# TEST UNITAIRE -> display board
test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'O', 'X', 'O']
display_board(test_board)    

# Assigning Player 1 and Player 2
def player_input():
    """OUTPUT => tuple (Player 1 marker, Player 2 marker)"""
    marker = ''
    # Keep asking for player 1 to choose X or O
    # Assign player 2 with the remaining marker
    while marker != 'X' and marker != 'O':
        marker = input('Player1, Choose between an "X" or "O" as a marker: ').upper()
    
    if marker == 'O':
        return ('O', 'X')
    else:
        return ('X', 'O')
        
    return (player1, player2)  

# TEST UNITAIRES -> afficher valeurs pour joueurs
player1_marker , player2_marker = player_input()
player1_marker
player2_marker

# Assigning X and O to the board
def place_marker(board, marker, position):
    board[position] = marker
    return board

# Test of modification of board
place_marker(test_board,'@',6)
display_board(test_board)

# check if there is a win
def win_check(board, mark):

    #WIN TIC TAC TOE -> check all ROWS and see if they all share the same marker
    # ALL COLUMN, check the same
    # 2 diagonals to check the same
    # Use indexing and returning a boolean
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

# TEST UNITAIRE -> win_check
display_board(test_board)
win_check(test_board, 'X')    

# choose randomly between the 2 players
def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

#Function responsible for checking whether a space is available on the board by returning a Boolean 
def space_check(board, position):
    return board[position] == ' '

# check if the board is full by looping through it
def full_board_check(board):

    for i in range(1,10):
        if space_check(board,i):
            return False
    #If the board is not full by the end the loop we return True        
    return True    

#ask for a player's next position
def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position: (1-9)'))
    return position

#Ask the player if he wants to play again and returns a Boolean True if so
def replay():
    choice =input("Play again? Enter Yes or No")

    return choice == 'Yes'

#Main Game Logic

#WHILE LOOP to keep running the game     
print('Welcome to Tic Tac Toe')
while True:
    #reset the board
    theBoard = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower[0] == 'y':
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn == 'Player 1':
            #Player 1's turn to play
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations, you have won the game!')
                game_on = False
        else:
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Congratulation to player 2 who won!')
                game_on = False
            #last case where the game is a draw    
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else: 
                    turn = 'Player 1 '
    if not replay():
        break                


