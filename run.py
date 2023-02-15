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
    print("=" * 50)
    print("        ***WELCOME TO BATTLESHIPS***")
    print("\n      Guess a ROW between: 0 to 4")
    print("ROW NUMBERS are left most row(0), to right(4)")
    print("\n      Guess a COLUMN between: 0 to 4")
    print("COLUMN NUMBERS are top column(0), to bottom(4)")
    print("\n     A MISS is marked with - 'X'")
    print("\n     HIT the Battleship - '*' - will appear")
    print("You get to place your Battleship on the board.")
    print("The Battleship is marked with 'S' on the starting board")
    print("and then hidden.")
    print("\nPlayer's board is shown 1st. AI's board is 2nd.")
    print("=" * 50)
    print("TO PLAY AGAIN - If you want to play again at the end:")
    print("'y' is for yes and 'n' is for no and the game will exit.")
    print("=" * 50)
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


def input_row(integer):
    """
    Check players entry for row, is an integer.
    Also checks entry is between a set range(0-4)
    """
    while True:
        try:
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
            s_col = int(input(ship))
            if s_col not in range(0, 5):
                raise ValueError()
        except ValueError:
            print("Invalid choice: Choose an integer between 0-4")
            continue
        else:
            return s_col
        break

# Starting the Battleship game inside a function so game can be
# played again after completing game.
# 'y' for yes, to continue.
# Exit game using this function 'n' for no.


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
    for _ in range(5):
        user_board.append(["."] * 5)
        ai_board.append(["."] * 5)

    def battleship_game(user_board, ai_board):
        """
        Create a function that combines the above 5 lists into a 5x5 grid shape
        and remove decoration.
        Join list with a 'space' between the "o" characters.
        """
        for row in user_board:
            print((" ").join(row))

        for row in ai_board:
            print((" ").join(row))

    ai_ship_row = randint(1, len(ai_board)) - 1
    ai_ship_col = randint(1, len(ai_board[0])) - 1

    while True:
        print("\n   Place Battleship on your board...")
        print("\n          ...for the enemy to find")
        battleship_game(user_board, " ")
        s_row = ships_row("\nSHIP ROW: ")
        s_col = ships_col("SHIP COLUMN: ")
        user_board[s_row][s_col] = "S"
        break

    print("... Battleship is moving into position...")

    tally = 0
    while True:
        print("\nEnter your guess...")
        guess_r = input_row("ROW: ")
        guess_c = input_col("COLUMN: ")
        ai_guess_r = randint(1, len(user_board)) - 1
        ai_guess_c = randint(1, len(user_board)) - 1
        if guess_r == ai_ship_row and guess_c == ai_ship_col:
            print(data, "'s Board!")
            ai_board[guess_r][guess_c] = "S"
            battleship_game(" ", ai_board)
            print("\nHIT! You sunk the Computer's Battleship first!")
            print("_" * 50)
            print("You had", tally, "misses, then sunk the Battleship!\n")
            break
        if ai_guess_r == s_row and ai_guess_c == s_col:
            print("\nAI HIT your ship!")
            user_board[ai_guess_r][ai_guess_c] = "S"
            ai_board[guess_r][guess_c] = "X"
            battleship_game(user_board, " ")
            print("AI has Won this time.. with", tally, "guesses!")
            break
        elif ai_board[guess_r][guess_c] == "X":
            print("~~~Nice try but you've guessed that before. Try again..~~~")
        elif user_board[ai_guess_r][ai_guess_c] == "X":
            ai_guess_r = randint(1, len(user_board)) - 1
            ai_guess_c = randint(1, len(user_board)) - 1
            tally -= 1
        else:
            print(f"ship IS on Row:{ai_ship_row} Column:{ai_ship_col}\n") 
            print("\nMISSED... Try again...")
            print(data, "'s Board")
            ai_board[guess_r][guess_c] = "X"
            user_board[ai_guess_r][ai_guess_c] = "X"
            battleship_game(user_board, " ")
            print("AI's Board!")
            battleship_game("", ai_board)
        tally += 1


while True:
    try:
        YES = "y"
        NO = "n"
        want_to_play_again()
        print("PLAY AGAIN? Select'y'- yes or 'n'- no.")
        restart_battleships = input("Then hit Enter: ")
        if restart_battleships == YES:
            continue
        if restart_battleships == NO:
            print("\nThanks for playing Battlehips..")
            print("Ill bring a bigger Fleet next time!")
            break
        if not YES or NO:
            raise ValueError()
    except ValueError:
        print("'y' for yes or 'n' for no. The Press Enter")
        restart_battleships = input("'y'- yes or 'n'- no. Then hit Enter: ")


