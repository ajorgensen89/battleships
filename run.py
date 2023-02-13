from random import randint
# Import file above for random integer production.
global guess_row
global guess_col

# Created functions, with credit, from Love Sandwiches Walkthrough
# via the course.
# Adapted for use here. User must enter name into INPUT
# before continuing into the game.


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
        name_input = input("Enter a name: ")
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
                "It's empty... You need to enter something here."
            )
    except EOFError as e_err:
        print(f"Your input caused an error: {e_err} Try again.")
        return False

    return True

# Two functions created to help with validing input from the user.
# Credit for layout from - 101 computing.net. In Credit for README.md file
# Adaptations made to the code where necessary.


def input_row(integer):
    """
    Check there is an entry for row that is an integer.
    Raises an error if the input is empty or not an integer, like a letter.
    """
    while True:
        try:
            guess_row = int(input(integer))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return guess_row
        break


def input_column(integer):
    """
    Check there is an entry for column that is an integer.
    Raises an error if the input is empty or not an integer, like a letter.
    """
    while True:
        try:
            guess_col = int(input(integer))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return guess_col
        break


# Saved name input in 'data' variable.


data = get_name_input()

# Create empty list to store the game's board Redefine in function.
board = []
# ai = []
# guess_row, guess_col = [], []
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

guess_row = []
guess_col = []
# For loop, to play the game on the grid created.
# for battle in range(5):

tally = 0
while True:
    guess_row = input_row("GUESS ROW:\n")
    guess_col = input_column("GUESS COLUMN:\n")
    print("reaching here")
    while True:
        if (guess_row < 0 or guess_col < 0) or (guess_row >= 5 or guess_col >= 5):
            print("Re enter a valid row and column number between 0-4")
            guess_row = int(input("GUESS ROW:\n"))
            guess_col = int(input("GUESS COLUMN:\n"))
        else:
            break
    if guess_row == random_row and guess_col == random_column:
        print("HIT!")
        print("You sunk the Battleship sunk on")
        print("_" * 40)
        print(f"Row:{guess_row}")
        print(f"Column:{guess_col}")
        print(data, "'s Board")
        board[guess_row][guess_col] = "*"
        board_game(board)
        break
    elif board[guess_row][guess_col] == "X":
        print("Nice try but you have guessed that already. Try again...")
    else:
        print("MISSED... Try again...")
        print(f"Batttleship was on Row:{random_row} Column:{random_column}")
        print(data, "'s Board")
        board[guess_row][guess_col] = "X"
        board_game(board)
        tally += 1
    # if guess_row and guess_col == random_row and random_column:
    #    board[random_row][random_column] = "S"
    #    print("The Battleship was too well hidden.. GAME OVER.")
    #    board_game(board)
        
    print("Turn:", tally)
        
# def turn_count():
#    turn = 0
