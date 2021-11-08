import introduction
import check
import board
from colorama import Fore

def playerTurn(turn, STARTPIECE):
    
    """Function retuns the name of the game
    
    Args: 
        turn: A boolean, controlling the while loop for a player's turn
        STARTPIECE: A string which is constant, representing the starting peice
    
    Returns: 
        turn
    """

    startPoint = input(Fore.BLUE + "What piece are you moving? ")
    endPoint = input(Fore.CYAN + "What position are you moving to? ")
    print("\n")

    if check.is_input_valid(startPoint, endPoint) == False:
        print(Fore.RED + "Please follow instructions")
        print(introduction.instructions())
        print("\n")
        turn = True

    elif check.is_move_valid(startPoint, endPoint) == False:
        print(Fore.RED + "Enter a valid move")
        print("\n")
        turn = True

    elif board.start_piece(startPoint) != STARTPIECE:
        print(Fore.RED + "Please select your piece")
        print("\n")
        turn = True

    else:
        board.move_piece(startPoint, endPoint)
        board.print_board()
        print("\n")
        turn = False
        
    return turn