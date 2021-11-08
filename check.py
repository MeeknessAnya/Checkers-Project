import board

def is_input_valid(startPoint, endPoint):
    """Function returns False if any of the conditional statement is true

    Args: 
        startPoint: A string, representing a player's selected starting move 
        endPoint: A string, representing a player's selected ending move
    
    Returns: 
        False

    Example:
        is_input_valid("2,1", "2,t") --> False
        is_input_valid("u,m", "i,A") --> False
        is_input_valid("2,4", "3,5") -->
    """
    
    if type(startPoint) != str or len(startPoint) != 3 or len(endPoint) != 3 or len(endPoint) != 3:
        return False
    
    start_row = startPoint[0]
    start_col = startPoint[2]
    end_row = endPoint[0]
    end_col = endPoint[2]

    if start_row.isnumeric() == False or start_col.isnumeric() == False or end_row.isnumeric() == False or end_col.isnumeric() == False:
        return False
    
def is_move_valid(startPoint, endPoint):
    """Function returns False if any of the the conditional statement is true
    
    Args: 
        startPoint: A string, representing a player's selected starting move 
        endPoint: A string, representing a player's selected ending move

    Returns: 
        False
    
    Example:
        is_move_valid("2,4", "3,5") --> False
        is_move_valid("5,2", "4,3") -->
        is_move_valid("2,5", "3,4") --> 
    """

    currBoard = board.access_board()
    start_row = int(startPoint[0])
    start_col = int(startPoint[2])
    end_row = int(endPoint[0])
    end_col = int(endPoint[2])

    if abs(end_row - start_row) > 2 or abs(end_col - start_col) > 2 or start_row == end_row or start_col == end_col:
        return False

    if start_row > 7 or start_col > 7 or end_row > 7 or end_col > 7 or start_row < 0 or start_col < 0 or end_row < 0 or end_col < 0:
        return False

    if currBoard[start_row][start_col] == currBoard[end_row][end_col] or currBoard[start_row][start_col] == ".":
        return False

    if currBoard[start_row][start_col] == "x":
        if end_row < start_row:
            return False
        two = 2
        one = 1

    else:
        if end_row > start_row:
            return False
        two = -2
        one = -1

    if end_row == start_row + two:
        if end_col == start_col + 2:
            if currBoard[start_row + one][start_col + 1] == ".":
                return False

            if currBoard[start_row + two][start_col + 2] != ".":
                return False

        elif end_col == start_col - 2:
            if currBoard[start_row + one][start_col - 1] == ".":
                return False

            if currBoard[start_row + two][start_col - 2] != ".":
                return False

        else: 
            return False

    elif end_row == start_row + one:
        if currBoard[end_row][end_col] != ".":
            return False
            
        if abs(end_col - start_col) != 1:
            return False