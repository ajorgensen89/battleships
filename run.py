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

# Saved name input in 'data' variable.


data = get_name_input()

# Create empty list to store the game's board.
board = []

# Create a list of 5 lists, all 5 "o" characters long. Loop and add in to
# the empty board variable above.
for x in range(5):
    board.append(["o"] * 5)
# Define a Battleship Board function in board_game.


def board_game(board):
    """
    Create a function that combines the above 5 lists into a 5x5 grid shape
    and remove decoration.
    Join list with a 'space' between the "o" characters.
    """
    for row in board:
        print((" ").join(row))


random_row = randint(1, len(board)) - 1
random_column = randint(1, len(board[0])) - 1

# For loop, to play the game on the grid created.

for battle in range(5):
    guess_row = int(input("GUESS ROW:\n"))
    guess_column = int(input("GUESS COLUMN:\n"))
    try:
        if guess_row and guess_column < 0 or guess_row and guess_column > 5:
            print("Re enter a valid row and column number between 0-4")
            guess_row = int(input("GUESS ROW:\n"))
            guess_column = int(input("GUESS COLUMN:\n"))
    except ValueError:
        print("error")
    if guess_row == random_row and guess_column == random_column:
        print("HIT. Marked with a '*' on the board")
        print(f"The Battleship sunk on Row:{guess_row}")
        print(f"Column:{guess_column}")
        print(data, "'s Board")
        board[guess_row][guess_column] = "*"
        print(board_game(board))
        break
    else:
        print("MISSED. Marked with an 'X' on the board")
        print(f"It was on Row:{random_row} and Column:{random_column}")
        print("Battleship is marked with an 'S'")
        print(data, "'s Board")
        board[guess_row][guess_column] = "X"
        print(f"Batttleship was on Row:{random_row}Column:{random_column}") 
        print(board_game(board))
    if guess_row and guess_column == str("X"):
        print("You have guessed that elready. Try again.")
        guess_row = int(input("GUESS ROW:\n"))
        guess_column = int(input("GUESS COLUMN:\n"))

print("This", battle)


def game_over(board):

    print("Game Over. You did not sink the Battleship")
     
    board[random_row][random_column] = "S"
    print(data, "'s Board")
    print(board_game(board))

    return board


gameOver = game_over(board)