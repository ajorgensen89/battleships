from random import randint
# Import file above for random integer production.
global guess_row
global guess_column
global guessedRowColumn


def get_name_input():
    """
    Create name for user's Battleship Board.
    Run while loop to check user had entered a name for their boardgame.
    Break loop if valid 'input' has been added. Continue with the game.
    This can be numbers, letters or special characters.
    For example: Player1 or Bobby. Even @Bobby_BattleShip-game!
    """
    # Welcoming message with a few instructions to play.
    print("=" * 40)
    print("WELCOME TO BATTLESHIPS")
    print("Guess a ROW between: 0 to 4")
    print("ROWS are left most row(0), to right most row(4)")
    print("and")
    print("Guess a COLUMN between: 0 to 4")
    print("COLUMNS are top column(0), to bottom column(4)")
    print("=" * 40)
    print("A HIT is marked with - '*'")
    print("A MISS is marked with - 'X'")
    print("You have 5 turns to guess correct.\n")
    print("Keep track of your guesses as they count towards a turn..\n")
    print("The computer will be one step closer to winning..")
    print("Get GAME OVER and...")
    print("The Battleship's position is mark with an - 'S'")
    print("~" * 40)
    # Create input field for a user to create a name or use their own.
    while True:
        name_input = input("Enter a name:")
        name = name_input
        # If a valid input is filled in, break from while loop and continue
        # with the Battleship game.
        if validate_input(name):
            print("Good Luck " + name + "!")
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
                "It's empty... You need to enter a name."
            )
    except EOFError as e_err:
        print(f"Your input caused an error: {e_err}  Try again.")
        return False

    return True

# Saved name input in 'data' variable.


data = get_name_input()


def player_guess():
    """
    To validate guess for row and column by user.
    """
    while True:
        # Input from the user for row and column choice.
        guess_row = int(input("\nGUESS ROW:\n"))
        guess_column = int(input("GUESS COLUMN:\n"))
        row = guess_row
        column = guess_column
        if validate_player_guess(row, column):
            print(validate_player_guess(row, column))
            print("CORRECT INTEGER RANGE...")
            break

    return row, column


def validate_player_guess(guessed_row, guessed_column):
    """
    Errors for grid ranges. Raise error if out of range of the board length.
    """
    try:
        if guessed_row and guessed_column < 0 or guessed_row and guessed_column >= 5:
            raise ValueError(
                "Out of grid range! Try again."
            )
    except ValueError as v_err:
        print(f"Oops. {v_err}")
        return False

    return True


# Create empty list to store the game's board Redefine in function.
board = []
# ai = []
# guess_row, guess_column = [], []
# ai_rand_row, ai_rand_col = [], []
# Create a list of 5 lists, all 5 "o" characters long. Loop and add in to
# the empty board variable above.
for x in range(5):
    board.append(["o"] * 5)
    # ai.append(["."] * 5)
# Define a Battleship Board function in board_game.
# def computer_board(ai):
#    """
#    AI turn and Battleship board
#    """
# MISS = "X"


def board_game(board):
    """
    Create a function that combines the above 5 lists into a 5x5 grid shape
    and remove decoration.
    Join list with a 'space' between the "o" characters.
    """
    for row in board:
        print((" ").join(row))

    # for row in ai:
        # print((" ").join(row))


random_row = randint(1, len(board)) - 1
random_column = randint(1, len(board[0])) - 1

# For loop, to play the game on the grid created.

for battle in range(5):
    # guess_row = int(input("\nGUESS ROW:\n"))
    # guess_column = int(input("GUESS COLUMN:\n"))    
    guessedRowColumn = player_guess()    
    print(guessedRowColumn)
    
    if guessedRowColumn == random_row and random_column:
        print("HIT!")
        print("You found it!")
        print("The Battleship sunk on:")
        print(f"Co-ordinates: {guessedRowColumn}")
        print(data, "'s Board")
        guessedRowColumn = "X"
        board_game(board)
    elif guessedRowColumn == "X":
        print("You have guessed that already. Try again.")
    else:
        print("MISSED... Try again...")
        print(f"Battleship was on Row:{random_row} Column:{random_column}")
        print(data, "'s Board")
        board[guess_row][guess_column] = "X"
        board_game(board)
    if battle == 4:
        board[random_row][random_column] = "S"
        print("The Battleship was too well hidden.. GAME OVER.")
        board_game(board)

for battle in range(5):
    # guess_row = int(input("\nGUESS ROW:\n"))
    # guess_column = int(input("GUESS COLUMN:\n"))
    print(guessedRc)
    if guess_row or guess_column < 0 and guess_row or guess_column >= 5:
        print("Re enter a valid row and column number between 0-4")
        guess_row = int(input("GUESS ROW:\n"))
        guess_column = int(input("GUESS COLUMN:\n"))
    if guess_row == random_row and guess_column == random_column:
        print("HIT!")
        print("You found it!")
        print("The Battleship sunk on:")
        print(f"Row:{guess_row}")
        print(f"Column:{guess_column}")
        print(data, "'s Board")
        board[guess_row][guess_column] = "*"
        board_game(board)
        break
    elif board[guess_row][guess_column] == "X":
        print("You have guessed that already. Try again.")
    else:
        print("MISSED... Try again...")
        print(f"Battleship was on Row:{random_row} Column:{random_column}")
        print(data, "'s Board")
        board[guess_row][guess_column] = "X"
        board_game(board)
    if battle == 4:
        board[random_row][random_column] = "S"
        print("The Battleship was too well hidden.. GAME OVER.")
        board_game(board)        
