def findPieces(currBoard, STARTPIECE):
    
    """Function checks to see if there's any piece left
    
    Args:
        currBoard: A 2D list, representing the current game board of each play
        STARTPIECE: A string which is constant, representing the starting peice
    
    Returns: 
        True or False
    """
    
    lst = []
    for row in range(len(currBoard)):
        for col in range(len(currBoard[row])):
            if currBoard[row][col] != ".":
                lst.append(currBoard[row][col])

    if "x" in lst and "o" in lst:
        return True

    elif STARTPIECE in lst:
        print("---------------------------")
        print("GAME OVER, PLAYER 1 WINS!!!")
        print("---------------------------")
        return False

    else:
        print("---------------------------")
        print("GAME OVER, PLAYER 2 WINS!!!")
        print("---------------------------")
        return False


def game_on(currBoard, STARTPIECE):

    """Function checks the current game state. If a player's piece gets to the other side, that player wins
    
    Args: 
        currBoard: A 2D list, representing the current game board of each play
        STARTPIECE: A string which is constant, representing the starting peice

    Returns: False 
    """

    #Checks for first to reach end
    if STARTPIECE == "x":
        if "x" in currBoard[7]:
            print("---------------------------")
            print("GAME OVER, PLAYER 1 WINS!!!")
            print("---------------------------")
            return False

        if "o" in currBoard[0]:
            print("---------------------------")
            print("GAME OVER, PLAYER 2 WINS!!!")
            print("---------------------------")
            return False

        return findPieces(currBoard, STARTPIECE)

    else:
        if "o" in currBoard[0]:
            print("---------------------------")
            print("GAME OVER, PLAYER 1 WINS!!!")
            print("---------------------------")
            return False

        if "x" in currBoard[7]:
            print("---------------------------")
            print("GAME OVER, PLAYER 2 WINS!!!")
            print("---------------------------")
            return False
            
        return findPieces(currBoard, STARTPIECE)
    