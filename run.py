from random import randint


def get_name_input():
    """
    Create name for user's Battleship Board. 
    Run while loop to check user had entered a name for their boardgame.
    Break loop if valid 'input' has been added. Continue with the game.
    This can be numbers, letters or special characters.
    For example: Player1 or Bobby. Even @Bobby_BattleShip-game!
    """
    while True:
        print("="*25)
        print("WELCOME TO BATTLESHIPS")
        print("Select a row: 0 to 4")
        print("and")
        print("Select a column: 0 to 4")
        print("=" * 25)

        name_input = input("Enter a name:")
        name = name_input
        if validate_input(name):
            print_name = (name + "'s board!")
            print(print_name)
            break
    return name        
   

def validate_input(value):    
    """
    Validates user input for name. 
    Raises Error if User had not added a name for their Battleship board.
    Check for input in try:
    Uses except: To print out Error.
    """  
    try:
        if not value:
            raise EOFError(
                "Not Valid... You need to enter a name."
            )              
    except EOFError as e:
        print(f"Your input caused an error: {e} Try again.")
        return False

    return True 


data = get_name_input() 
print(data, "gagaga")

# Create empty list to store the game's board.
board = []

# Create a list of 5 lists, all 5 "o" characters long. Loop and add in to
# the empty board variable above.
for x in range(5):
    board.append(["o"] * 5)

# Define a Battleship Board function in board_game


def board_game(board):
    """
    Create a function that combines the above 5 lists into a 5x5 grid shape 
    and remove decoration.
    Join list with a 'space' between the "o" characters.
    """  
    for row in board:
        print((" ").join(row))

# Place one ship randomly on the grid


board_game(board)

# Prints one Battleship 'S', randomly on the board
random_row = randint(0, len(board))
random_column = randint(0, len(board[0]))

# Prints ship loction. To be removed.
print(random_row, random_column)

# Input from the user for row and column choice.
guess_row = int(input("GUESS ROW:\n"))
guess_column = int(input("GUESS COLUMN:\n"))

if guess_row == random_row and guess_column == random_column:
    print("HIT. Marked with a '*' on the board")
    print(f"The Battleship sunk on Row:{guess_row} and Column:{guess_column}")
    print(data, "'s Board")
    board[guess_row][guess_column] = "*"
    print(board_game(board))
else:
    print("MISSED. Marked with an 'X' on the board")
    print(f"It was on Row:{random_row} and Column:{random_column}")
    print("The Battleship's position is marked with an 'S' on the board")
    print(data, "'s Board")
    board[random_row][random_column] = "S"
    board[guess_row][guess_column] = "X" 
    print(board_game(board)) 


# def get_five_ships(ships) -> int:
# for ship in ships:    