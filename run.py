'''
Import randint from Random Module
to use for random number generation.
'''
from random import randint

# Created function, with credit, from Love Sandwiches Walkthrough
# via the course.
# Adapted for use here. User must enter name into INPUT
# before continuing into the game.


def get_name_input():
    """
    Create name for user's Battleship Board.
    Run while loop to check user had entered a name for their boardgame.
    Break loop if valid 'input' has been added. Continue with the game.
    This can be numbers, letters or special characters.
    For example: Player1 , User1 or Bobby. Even @Bobby_BattleShip-game!
    """
    # Welcoming message with a few instructions to play.
    print("=" * 45)
    print("      ***WELCOME TO BATTLESHIPS***")
    print("\n   Guess a ROW between: 0 to 4")
    print("ROW NUMBERS are left most row(0),")
    print("to right(4)")
    print("\n      Guess a COLUMN between: 0 to 4")
    print("COLUMN NUMBERS are top column(0),")
    print("to bottom(4)")
    print("\n     A MISS is marked with - 'X'")
    print("\n     HIT the Battleship - '*' - will appear")
    print("Place your Battleship on the board.")
    print("It will be marked with 'S' on your board")
    print("\nPlayer's board is shown 1st.")
    print("AI's board is 2nd.")
    print("=" * 45)
    print("TO PLAY AGAIN AFTER: 'y' for yes to continue")
    print("And 'n' for no and the game will exit.")
    print("=" * 45)
    # Create input field for a user to create a name or use their own.
    while True:
        # Name input. Whitespace removed.
        name_input = input("Enter a name: ").strip()
        name = name_input
        # Valid input - break from while loop and continue
        # with the Battleship game.
        if validate_input(name):
            name = name_input
            break
    # Return name value, to function, to be used to label the user's board.
    # Saved in variable - data.
    return name

# Function below raises error for arguments. Such as 'name' above.


def validate_input(value):
    """
    Validates user input for name.
    Raises Error if user has not added a name.
    Check for input in try:
    Uses except: To print out Error.
    """
    try:
        # If an argument is returned False.
        # Error is raised until it returns True.
        if not value:
            raise EOFError(
                "It's empty... You need to enter something here."
            )
    except EOFError as e_err:
        print(f"Your input caused an error: {e_err} Try again.")
        return False

    return True


# Functions created to help with validing input from the user.
# Credit for layout from - 101 computing.net. In Credit for README.md file
# Adaptations made to the code where necessary.
# Functions check user input is an integer and within specified range(0-4).


def input_row(integer):
    """
    Check players entry for row, is an integer.
    Also checks entry is between a set range(0-4)
    """
    while True:
        try:
            # Validates the users row. Raises error if necessary.
            guess_r = int(input(integer))
            if guess_r not in range(0, 5):
                raise ValueError()
        except ValueError:
            print("Invalid choice: Choose an integer between 0-4")
            continue
        else:
            return guess_r
        break


def input_col(integer):
    """
    Check players entry for column, is an integer.
    Also checks entry is between a set range(0-4)
    """
    while True:
        try:
            # Validates the users column. Raises error if necessary.
            guess_c = int(input(integer))
            if guess_c not in range(0, 5):
                raise ValueError()
        except ValueError:
            print("Invalid choice: Choose an integer between 0-4")
            continue
        else:
            return guess_c
        break

# Saved name input in 'data' variable.


data = get_name_input()


def ships_row(ship):
    """
    Check there is an entry for row that is an integer.
    """
    while True:
        try:
            # Validates the users Battleship position. Raises error if not.
            # Validate the row entry.
            s_row = int(input(ship))
            if s_row not in range(0, 5):
                raise ValueError()
        except ValueError:
            print("Invalid choice: Choose an integer between 0-4")
            continue
        else:
            return s_row
        break


def ships_col(ship):
    """
    Check there is an entry for column that is an integer.
    """
    while True:
        try:
            # Validates the users Battleship position. Raises error if not.
            # Validates the column entry.
            s_col = int(input(ship))
            if s_col not in range(0, 5):
                raise ValueError()
        except ValueError:
            print("Invalid choice: Choose an integer between 0-4")
            continue
        else:
            return s_col
        break

# Function is called to restart the game at the end.
# Battleship game inside this function so game can be
# played again after completion.
# 'y' for yes, to continue.
# Exit game by entering 'n' for no. Hit Enter.


def want_to_play_again():
    """
    Function to restart game at the end. Called at the end inside
    a while loop to repeat the game depending on input of
    'y' for yes, to play again, and 'n' for no, to exit the program.
    """
    # Create empty list to store the game's board Redefine in function.
    user_board, ai_board = [], []
    # Create a list of 5 lists, all 5 "o" characters long. Loop and add in to
    # the empty user_board variable above.
    # "_" used for variable name as not unpacked or used in this instance.
    for _ in range(5):
        user_board.append(["."] * 5)
        ai_board.append(["."] * 5)

    # Main Battleship Game.

    def battleship_game(user_board, ai_board):
        """
        Main function to run the Battleship Game.
        Passing the player(user_board) and computer(ai_board) boards.
        """

        # These for loops combine the lists above from user_board and ai_board,
        # into a 5x5 grid shape. Creating the game board.
        # And removes decoration of a 'list'.
        # Join list with a 'space' between the "." characters.
        for row in user_board:
            print((" ").join(row))

        for row in ai_board:
            print((" ").join(row))

    # Generates random numbers which place a Battleship on the board
    # for the player to find.
    ai_ship_row = randint(1, len(ai_board)) - 1
    ai_ship_col = randint(1, len(ai_board[0])) - 1

    # While loop, loops until valid ship co-ordinates have been
    # presented by the player.
    while True:
        print("Place Battleship on your board...for the enemy to find")
        # Print users board.
        battleship_game(user_board, " ")
        # For row and column selected for Battlehip position by users.
        # Checked for errors.
        s_row, s_col = ships_row("\nSHIP ROW: "), ships_col("SHIP COLUMN: ")
        # Print the ships location, the AI is trying to find, on users board.
        user_board[s_row][s_col] = "S"
        break

    print("\n... Battleship is moving into position ...")

    tally = 0
    while True:
        print("\nTarget the AI's Board. Enter your guess...")
        # User can randomly keep guessing rows and columns. Checked for errors.
        guess_r, guess_c = input_row("ROW: "), input_col("COLUMN: ")
        # Generate AI's random guesses.
        ai_guess_r = randint(1, len(user_board)) - 1
        ai_guess_c = randint(1, len(user_board)) - 1
        # Tally up the turns taken.
        tally += 1
        # Checks incase the AI randomly generates the co-ordinates again.
        # Row and column get repeated.
        # List character, "." is changed to a "X".
        if user_board[ai_guess_r][ai_guess_c] == "X":
            ai_guess_r = randint(1, len(user_board)) - 1
            ai_guess_c = randint(1, len(user_board)) - 1
            # Prints a MISS 'X' on the board depending on the Ai's guess
            # of row and column.
            user_board[ai_guess_r][ai_guess_c] = "X"
        # If users guesses match the Ai's ship position -
        # HIT '*' is displayed. And the turns are tallyed up.
        # It changes the "." to a "*" on the board at specified points.
        if guess_r == ai_ship_row and guess_c == ai_ship_col:
            # Places both the users guess on the Ai's board by changing
            # the list character from "." to a "*".
            ai_board[guess_r][guess_c] = "*"
            # Prints the Ai's Board
            battleship_game(" ", ai_board)
            print("_" * 45)
            print("\nHIT! You sunk the AI's Battleship first!")
            print("It took", tally, "turns to sink the Battleship!\n")
            # Ends game loop.
            break
        # This compares the input to each other.
        # If the Ai's guess matches the Battleship place by the user, AI wins.
        # HIT '*' is placed on the users board. AI wins.
        if ai_guess_r == s_row and ai_guess_c == s_col:
            print("_" * 45)
            print("\nAI HIT your ship!")
            # Places the AI's guess on the users board.
            # Edits the boards "." and changes it to a "*"
            user_board[ai_guess_r][ai_guess_c] = "*"
            # Prints the users board with winning HIT.
            battleship_game(user_board, " ")
            print("AI Won this time.. with", tally, "guesses!")
            # Ends game loop.
            break
        # If a row and column has already been used and changed to an "X".
        # This can identify that and you try again.
        if ai_board[guess_r][guess_c] == "X":
            print("~" * 45)
            print("~~Nice try but you've guessed that before...")
            # Makes sure the tally does not increase when new
            # co-ordinates are re-selected (row and column).
            tally -= 1
        else:
            print("\nMISSED... Try again...\n")
            ai_board[guess_r][guess_c] = "X"
            # This edits this particular position of the board.
            # Changes the "." to a "X".
            user_board[ai_guess_r][ai_guess_c] = "X"
            # Prints user board with their name above it.
            print(data, "'s Board")
            battleship_game(user_board, " ")
            # Print AI's board and name for the board.
            print("AI's Board!")
            battleship_game("", ai_board)


# While loop to restart the game it True.
# If False, the game ends with a message of thanks.


while True:
    # Function to return to if returns True.
    want_to_play_again()
    print("\n", "=" * 45)
    print("   PRESS 'y'- yes to play again.")
    print("   PRESS 'n'- no to exit.")
    print("   THEN hit Enter: ")
    restart_battleships = input("PLAY AGAIN?: ")
    # Conintue playing if = "y"
    if restart_battleships == "y":
        continue
    # Continue playing if = "n"
    if restart_battleships == "n":
        print("\nThanks for playing Battleships..")
        # reaks loop and ends program after message of thanks.
        break
