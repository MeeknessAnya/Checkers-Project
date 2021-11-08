import turtle

def invertBoard(currBoard):
    """Function returns an inverted current board of each play since python turtle draws the board inverted.
    
    Args:
        currBoard: A 2D list, representing the current game board of each play

    Returns: 
        invBoard: The inverted board which is also a 2D list. 
    """
    
    invBoard = []
    l = len(currBoard)

    for i in range(l):
        a = []
        for j in range(8):
            a.append(currBoard[8-i-1][j])
        invBoard.append(a)

    return invBoard

def draw_board(row, col, color):
    """Function draws the current board using python turtle 

    Args: 
        row: An integer, representing the row to draw at
        col: An integer, representing the col to draw at
        
    Returns:
        null
    """
    
    turtle.sety(row * 50)
    turtle.setx(col * 50)
    turtle.begin_fill()
    turtle.down()
    turtle.color(color)
    for i in range(4):
        turtle.forward(50)
        turtle.left(90)
    turtle.up()
    turtle.end_fill()

def draw_piece(row, col, color):
    """Function draws the pieces using python turtle 

    Args: 
        row: An integer, representing the row to draw at
        col: An integer, representing the col to draw at
        
    Returns:
        null
    """
    
    turtle.sety(row * 50)
    turtle.setx((col + 0.50) * 50)
    turtle.begin_fill()  # Begin the fill process.
    turtle.down()
    turtle.color(color)
    turtle.circle(15)
    turtle.up()
    turtle.end_fill()
    
def graph(currBoard):
    """Function draws the current board using python turtle 

    Args: 
        currBoard: A 2D list, representing the current game board of each play
        
    Returns:
        null
    """
    
    turtle.speed(0)
    turtle.hideturtle()

    currBoard = invertBoard(currBoard)
    for row in range(len(currBoard)):
        for col in range(len(currBoard[row])):
            inverted = (row + col) % 2 == 0
            turtle.hideturtle()
            if currBoard[row][col] == "x":
                draw_board(row, col, "green" if inverted else "silver")
                draw_piece(row, col, "red")

            elif currBoard[row][col] == "o":
                draw_board(row, col, "green" if inverted else "silver")
                draw_piece(row, col, "blue")
                
            elif currBoard[row][col] == ".":
                draw_board(row, col, "green" if inverted else "silver")