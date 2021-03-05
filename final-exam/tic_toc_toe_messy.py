# Tic Tac Toe
# Reference: With modification from http://inventwithpython.com/chapter10.html. 

# TODOs:  
# 1. Find all TODO items and see whether you can improve the code. 
#    In most cases (if not all), you can make them more readable/modular.
# 2. Add/fix function's docstrings (use """ instead of # for function's header
#    comments)

import random

def drawBoard(board):
    ''' This function prints out the board that it was passed.
     "board" is a list of 10 strings representing the board (ignore index 0)'''
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def inputPlayerLetter():
    ''' Function that lets the player type which letter they want to be.
    Returns a list with the player’s letter as the first item, and the computer's letter as the second. '''

    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # the first element in the list is the player’s letter, the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:                       
        return ['O', 'X']

def whoGoesFirst():
    ''' Function to determine who goes first in the game '''
    if random.randint(0, 1) == 0:
        return 'computer'
    else:                       
        return 'player'

def playAgain():
    ''' This function returns True if the player wants to play again, otherwise it returns False.'''
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    '''Allows the player make moves'''
    board[move] = letter

def isWinner(current_board, letter):
    ''' Given a board and a player’s letter, this function returns True if that player has won.
    We use bo instead of board and le instead of letter so we don’t have to type as much. '''
    return ((current_board[7] == letter and current_board[8] == letter and current_board[9] == letter) or # across the top
            (current_board[4] == letter and current_board[5] == letter and current_board[6] == letter) or # across the middle     
            (current_board[1] == letter and current_board[2] == letter and current_board[3] == letter) or # across the bottom
            (current_board[7] == letter and current_board[4] == letter and current_board[1] == letter) or # down the left side
            (current_board[8] == letter and current_board[5] == letter and current_board[2] == letter) or # down the middle
            (current_board[9] == letter and current_board[6] == letter and current_board[3] == letter) or # down the right side
            (current_board[7] == letter and current_board[5] == letter and current_board[3] == letter) or # diagonal
            (current_board[9] == letter and current_board[5] == letter and current_board[1] == letter)) # diagonal

def getBoardCopy(board):
    ''' Make a duplicate of the board list and return it the duplicate.'''
    return [dup for dup in board]

def isSpaceFree(board, move):
    ''' Return true if the passed move is free on the passed board. '''
    return board[move] == " "

def getPlayerMove(board):
    ''' Let the player type in their move. '''
    decision = None
    possibilities = [str(num) for num in range(1, len(board)+1)] 
    while decision not in possibilities or not isSpaceFree(board, int(decision)):
        print('What is your next move? (1-9)')
        decision = input()
    return int(decision)

def chooseRandomMoveFromList(board, movesList):
    ''' Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move. '''
    possibleMoves = []
    for move in movesList:
        if isSpaceFree(board, move):
            possibleMoves.append(move)

    if possibleMoves: 
        return random.choice(possibleMoves)
    return None

def getComputerMove(board, computerPiece):
    ''' Given a board and the computer's letter, determine where to move and return that move. '''
    if computerPiece == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerPiece, i)
            if isWinner(copy, computerPiece):
                return i

    # Check if the player could win on their next move, and block them.
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move is not None: 
        return move

    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    '''Function thats returns True if every space on the board has been taken. Otherwise return False.'''
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

def inGamePlayerOutcome(turn, theBoard, playerLetter):
    ''' Conveys the Player’s logic and adjust the board accordingly '''
    game_status = ''
    
    drawBoard(theBoard)
    move = getPlayerMove(theBoard)
    makeMove(theBoard, playerLetter, move)

    if isWinner(theBoard, playerLetter):
        drawBoard(theBoard)
        game_status = 'Hooray! You have won the game!'
        print(game_status)
        return game_status
    
    elif isBoardFull(theBoard):
        drawBoard(theBoard)
        game_status = 'The game is a tie!'
        print(game_status)
        return game_status
            
    game_status = 'computer'
    return game_status

def inGameComputerOutcome(turn, theBoard, computerLetter):
    ''' Conveys the Computer’s logical choices and adjust the board accordingly.'''
    game_status = ''
    move = getComputerMove(theBoard, computerLetter)
    makeMove(theBoard, computerLetter, move)

    if isWinner(theBoard, computerLetter):
        drawBoard(theBoard)
        print('The computer has beaten you! You lose.')
        game_status = 'The computer has beaten you! You lose.'
        return game_status
    
    elif isBoardFull(theBoard):
        drawBoard(theBoard)
        print('The game is a tie!')
        game_status = 'The game is a tie!'
        return game_status
        
    game_status = 'player'
    
    return game_status
    
    
def gameLogic():
    '''This function determines the game logic based on the users input and decision making.'''
    
    # Reset the board
    theBoard = [' '] * 10 # TODO: Refactor the magic number in this line (and all of the occurrences of 10 thare are conceptually the same.)
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')

    while True:
        if turn == 'player':  
            turn = inGamePlayerOutcome(turn, theBoard, playerLetter)
            
        if turn == 'computer':
            turn = inGameComputerOutcome(turn, theBoard, computerLetter)
        else:
            break 

if __name__ == '__main__':
        
    print('Welcome to Tic Tac Toe!')

    while True:
        
        gameLogic()
        
        if not playAgain():
            break
        
    print('Thanks For Playing!')