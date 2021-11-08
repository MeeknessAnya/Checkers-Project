from colorama import Fore

def name():

    """Function retuns the name of the game, OH MY CHECKERS!!!
    
    Args: 
    
    Returns: 
        The name
    """

    return Fore.GREEN + "Welcome to 'OH MY CHECKERS!!'"

def instructions():

    """Function retuns the instructions of the game
    
    Args: 
    
    Returns: 
        The instructions
    """

    return Fore.WHITE + "All inputs should be in this form: row,col\n" + Fore.WHITE + "NOTE: row and col represent the indexes of the pieces.\n" + Fore.WHITE + "With row being the horizontal index and col being the vertical index."