from random import randint


def name_input():
    """
    Create name for use's Battleship Board. Check for input and 
    raise an error if no 'name' has been added to input.
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
        if name:
            print_name = (name_input + "'s board!")
            print(print_name)
            break
            
    try:
        if not name:
            raise EOFError(
                "Not Valid... You need to enter a name."
            )              
    except EOFError as e:
        print(f"Your input caused an error: {e} Try again.")
        return False
     
    return True    
    
    
name_input() 


# Create empty list to store the game's board.
board = []
# Create a list of 5 lists, all 5 "o" characters long. Add in to
# the empty board variable above.
for x in range(5):
    board.append(["o"] * 5)

# Create a function that combines 5 lists into a 5x5 grid shape 
# and remove decoration.
# Join list with a 'space' between the "o" characters.


def board_game(board):  
    for row in board:
        print((" ").join(row))


board_game(board)

# Place one ship randomly on the grid
random_row = randint(0, len(board) - 1)
random_column = randint(0, len(board[0]) - 1)

# Place five shipd randomly on the grid.

# Prints ship loction. To be removed.
print(random_row, random_column)

# Input from the user for row and column choice.
guess_row = int(input("GUESS ROW:\n"))
guess_column = int(input("GUESS COLUMN:\n"))

if guess_row == random_row and guess_column == random_column:
    print("HIT. Marked with a '*' on the board")
    print(f"The Battleship sunk on Row:{guess_row} and Column:{guess_column}")
    board[guess_row][guess_column] = "*"
    print(board_game(board))
else:
    print("MISSED. Marked with an 'X' on the board")
    print(f"It was on Row:{random_row} and Column:{random_column}")
    print("The Battleship's position is marked with an 'S' on the board")

    board[random_row][random_column] = "S"
    board[guess_row][guess_column] = "X" 
    print(board_game(board)) 


# Place one ship randomly on the grid.
# ships = []


# def get_five_ships(ships) -> int:
# for ship in ships:    