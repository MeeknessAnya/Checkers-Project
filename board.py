from colorama import Fore

BOARD = [
    [".", "x", ".", "x", ".", "x", ".", "x"],
    ["x", ".", "x", ".", "x", ".", "x", "."],
    [".", "x", ".", "x", ".", "x", ".", "x"],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    ["o", ".", "o", ".", "o", ".", "o", "."],
    [".", "o", ".", "o", ".", "o", ".", "o"],
    ["o", ".", "o", ".", "o", ".", "o", "."],
]

currBoard = BOARD.copy()


def new_board(): # Resetting the currBoard
    """Function prints a new board after a game has concluded.

    Args: 
        null
    
    Returns: 
        null
    """

    for row in BOARD:
        print(" ".join(row))


def print_board():  # Printing the current board with character location
    """Function prints the current board of each play during the game 

    Args: 
        null

    Returns: 
        null
    """

    indexes = [["0", "1", "2", "3", "4", "5", "6", "7"]]
    output = currBoard
    output = indexes + output
    output[0] = [" "] + output[0]
    output[1] = ["0"] + output[1]
    output[2] = ["1"] + output[2]
    output[3] = ["2"] + output[3]
    output[4] = ["3"] + output[4]
    output[5] = ["4"] + output[5]
    output[6] = ["5"] + output[6]
    output[7] = ["6"] + output[7]
    output[8] = ["7"] + output[8]
    
    for i in range(len(output)):
        #print(" ".join(output[i]))
        out = ""
        if i % 2 == 0:
            c = 0
            while c < len(output[i]):
                if output[i][c] == "x":
                    out = out + "   " + f"{Fore.RED}x"
                elif output[i][c] == "o":
                    out = out + "   " + f"{Fore.BLUE}o"
                elif output[i][c] in "1234567890":
                    out = out + "   " + f"{Fore.WHITE}{output[i][c]}"
                else:
                    if c % 2 == 0:
                        out = out + "   " + f"{Fore.WHITE}{output[i][c]}"
                    else:
                        out = out + "   " + f"{Fore.GREEN}{output[i][c]}"
                c += 1
        else:
            c = 0
            while c < len(output[i]):
                if output[i][c] == "x":
                    out = out + "   " + f"{Fore.RED}x"
                elif output[i][c] == "o":
                    out = out + "   " + f"{Fore.BLUE}o"
                elif output[i][c] in "1234567890":
                    out = out + "   " + f"{Fore.WHITE}{output[i][c]}"
                else:
                    if c % 2 == 1:
                        out = out + "   " + f"{Fore.WHITE}{output[i][c]}"
                    else:
                        out = out + "   " + f"{Fore.GREEN}{output[i][c]}"
                c += 1
        print(out)

def access_board():
    """Calling this function gives acces to the current board.
    
    Args: 
        null
    
    Returns: 
        The current board during play
    """

    return currBoard

def start_piece(startPoint):
    """This function gets the starting piece for a player    

    Args:
        startPoint: A string, representing a player's selected starting move

    Returns: 
        The selected starting point's peice. Thus is either "x", "o", or ".".

    Example:
        start_peice("2,1") --> "x"
        start_peice("5,0") --> "o"
        start_peice("2,4") --> "."
    """

    start_row = int(startPoint[0])
    start_col = int(startPoint[2])
    return currBoard[start_row][start_col]

def move_piece(startPoint, endPoint):
    """Function reassigns a character to the position the player chooses thus moving the piece
       
    Args:
        startPoint: A string, representing a player's selected starting move 
        endPoint: A string, representing a player's selected ending move 
    
    Returns: 
        null
    
    """

    start_row = int(startPoint[0])
    start_col = int(startPoint[2])
    end_row = int(endPoint[0])
    end_col = int(endPoint[2])

    if currBoard[start_row][start_col] == "x":
        other = "o"
        two = 2
        one = 1
    else:
        other = "x"
        two = -2
        one = -1

    if end_row == start_row + one and (end_col == start_col + 1 or end_col == start_col - 1):
        # if the position is already occupied by your piece
        if currBoard[start_row][start_col] != currBoard[end_row][end_col]:
            currBoard[start_row][start_col],currBoard[end_row][end_col] = ".", currBoard[start_row][start_col]

    elif end_row == start_row + two and (end_col == start_col + 2 or end_col == start_col - 2):
        if end_col == start_col + 2:
            if currBoard[start_row + one][start_col + 1] == other and currBoard[start_row + two][start_col + 2] == ".":
                currBoard[start_row][start_col], currBoard[end_row][end_col] = ".", currBoard[start_row][start_col]
                currBoard[start_row + one][start_col +  1]  = "."
                
        if end_col == start_col - 2:
            if currBoard[start_row + one][start_col - 1] == other and currBoard[start_row + two][start_col - 2] == ".":
                currBoard[start_row][start_col], currBoard[end_row][end_col] = ".", currBoard[start_row][start_col]
                currBoard[start_row + one][start_col -  1]  = "."