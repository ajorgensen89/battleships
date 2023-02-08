from random import randint
import random


def get_name_input():
    """
    Create name for user's Battleship Board.
    Run while loop to check user had entered a name for their boardgame.
    Break loop if valid 'input' has been added. Continue with the game.
    This can be numbers, letters or special characters.
    For example: Player1 or Bobby. Even @Bobby_BattleShip-game!
    """
    while True:
        # Welcoming message with a few instructions to play.
        print("="*25)
        print("WELCOME TO BATTLESHIPS")
        print("Select a row: 0 to 4")
        print("and")
        print("Select a column: 0 to 4")
        print("=" * 25)
        # Create input field for a user to create a name or use their own.
        name_input = input("Enter a name:")
        name = name_input
        # If a valid input is filled in, break from while loop and continue
        # with the Battleship game.
        if validate_input(name):
            print_name = name + "'s board!"
            print(print_name)
            break
    # Return name value, to function, to be used to label the user's board.
    # Saved in variable - data.
    return name


def validate_input(value):
    """
    Validates user input for name.
    Raises Error if user has not added a name for their Battleship board.
    Check for input in try:
    Uses except: To print out Error.
    """
    try:
        if not value:
            raise EOFError(
                "Not Valid... You need to enter a name."
            )
    except EOFError as e_err:
        print(f"Your input caused an error: {e_err} Try again.")
        return False

    return True

# Saved name input for players board to be named in data variable.


data = get_name_input()


# Storage variables for guesssing a row and column.
guess_row = int(input("GUESS ROW:\n"))
guess_column = int(input("GUESS COLUMN:\n"))


def player_guess():
    """
    To validate guess for row and column by user.
    """
    while True:
        # Input from the user for row and column choice.
        if validate_player_guess(guess_row):
            print("Working...")
            break
        if validate_player_guess(guess_column):
            print("working too..")
            break
        return guess_row, guess_column


def validate_player_guess(guessed):
    """
    Errors for grid ranges. Raise error if out of range of the board length.
    """
    try:
        if guessed >= 5:
            raise ValueError(
                "Out of grid range! Try again."
            )
    except ValueError as v_err:
        print(f"Oops. {v_err}")
        return False

    return True


decision = player_guess()
print("Incorrect Enteries:", decision)


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


# Prints one Battleship 'S', randomly on the board.
# Which is only revealed after a turn.
random_row = randint(0, len(board))
random_column = randint(0, len(board[0]))


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


board_game(board)
