import introduction
import game
import board
import boardgraphic
import player
import time
from colorama import Fore

def startGame(): # This function starts the game
    """This function starts the game and loads all other functions associated with the game.

    Args: 
        null

    Returns: 
        null
    """

    print(introduction.name())
    time.sleep(1)
    print(introduction.instructions())

    STARTPIECE = input(Fore.BLUE + "Player 1, please select your piece? x/o ") # To track what peice a player uses

    if STARTPIECE == "x": # To track what peice the other player uses
        OTHERPIECE = "o" 
        
    else:
        OTHERPIECE = "x"

    print("\n")
    board.print_board()
    currBoard = board.access_board()
    boardgraphic.graph(currBoard)
    print("\n")

    gameOn = True
    while gameOn: # While the game hasn't ended 
        
        # Player 1's turn
        print("Player 1's turn")
        turn = True
        
        while turn:
            turn = player.playerTurn(turn, STARTPIECE)
                
        currBoard = board.access_board()
        boardgraphic.graph(currBoard)

        gameOn = game.game_on(currBoard, STARTPIECE)
        if gameOn == False:
            break
        
        # Player 2's turn
        print("Player 2's turn") 
        turn = True
        
        while turn:
            turn = player.playerTurn(turn, OTHERPIECE)

        currBoard = board.access_board()
        boardgraphic.graph(currBoard)

        gameOn = game.game_on(currBoard, STARTPIECE) # Updates gameOn


if __name__ == "__main__":
    start = input(Fore.YELLOW + "Do you want to play? y/n ")
    print("\n")
    if start == "y":
        startGame()
    if start == "n":
        print(Fore.RED + "Hope you comeback later:)")  