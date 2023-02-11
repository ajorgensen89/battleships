from random import randint


def get_name_input():
    """
    Create name for user's Battleship Board.
    Run while loop to check user had entered a name for their boardgame.
    Break loop if valid 'input' has been added. Continue with the game.
    This can be numbers, letters or special characters.
    For example: Player1 or Bobby. Even @Bobby_BattleShip-game!
    """
    # Welcoming message with a few instructions to play.
    print("=" * 30)
    print("WELCOME TO BATTLESHIPS")
    print("Select a row: 0 to 4")
    print("and")
    print("Select a column: 0 to 4")
    print("=" * 30)
    print("A HIT is marked with - '*'")
    print("A MISS is marked with - 'X'")
    print("If you sink a Battleship, it will be marked with - 'S'")
    print("~" * 30)
    # Create input field for a user to create a name or use their own.
    while True:
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
                "It's empty... You need to enter a name."
            )
    except EOFError as e_err:
        print(f"Your input caused an error: {e_err} Try again.")
        return False
    
    return True

# Saved name input in 'data' variable.


data = get_name_input()

# Create empty list to store the game's board.
board = []
ai = []
guess_row, guess_column = [], []
ai_rand_row, ai_rand_col = [], []
# Create a list of 5 lists, all 5 "o" characters long. Loop and add in to
# the empty board variable above.
for x in range(5):
    board.append(["o"] * 5)
    ai.append(["."] * 5)
# Define a Battleship Board function in board_game.
# def computer_board(ai):
#    """
#    AI turn and Battleship board
#    """
MISS = "X"


def board_game(board, ai):
    """
    Create a function that combines the above 5 lists into a 5x5 grid shape
    and remove decoration.
    Join list with a 'space' between the "o" characters.
    """
    for row in board:
        print((" ").join(row))

    for row in ai:
        print((" ").join(row))


random_row, random_column = randint(1, len(board)) - 1, randint(1, len(board)) - 1
ai_rand_row, ai_rand_col = randint(1, len(ai)) - 1, randint(1, len(ai)) - 1

# For loop, to play the game on the grid created.


for battle in range(5):
    guess_row, guess_column = int(input("GUESS ROW:\n")), int(input("GUESS COLUMN:\n"))
    ai_guess_r, ai_guess_c = randint(1, len(ai)) - 1, randint(1, len(ai)) - 1
    if guess_row and guess_column == random_row and random_column:
        print("MISSED. Marked with an 'X' on the board")
        print("Battleship is marked with an 'S'")
        board[guess_row][guess_column] = MISS
        print("Batttleship was on:")
        print(f"Row:{random_row} Column:{random_column}")
        print("MISSED. Marked with an 'X' on the board")
        print(f"Ai Battleship was on Row:{ai_rand_row} and Column:{ai_rand_col}")
        print("Battleship is marked with an 'S'")
        print(data, "'s Board")
        print(board_game(board, ai))
    if ai_guess_r and ai_guess_c == ai_rand_row and ai_rand_col:
        print("MISSED. Marked with an 'X' on the board")
        print("Battleship is marked with an 'S'")
        board[guess_row][guess_column] = MISS
        print("Batttleship was on:")
        print(f"Row:{random_row} Column:{random_column}")
        print("MISSED. Marked with an 'X' on the board")
        print(f"Ai Battleship was on Row:{ai_rand_row} and Column:{ai_rand_col}")
        print("Battleship is marked with an 'S'")
        print(data, "'s Board")
        print(board_game(board, ai))   
    if ai_guess_r == ai_rand_row and ai_guess_c == ai_rand_col:
        print("HIT. Marked with a '*' on the board")
        print("The Battleship sunk on:")
        print(f"Row:{ai_guess_r} Column:{ai_guess_c}")
        ai[ai_guess_r][ai_guess_c] = "*"
        print(data, "'s Board")
        print(board_game(board, ai))
        break
    if guess_row == random_row and guess_column == random_column:
        print("Computer WINS!")
        print("HIT. Marked with a '*' on the board")
        print("The Battleship sunk:")
        print(f"Row:{guess_row}")
        print(f"Column:{guess_column}")
        board[guess_row][guess_column] = "*"
        print(data, "'s Board")
        print(board_game(board, ai))
        break
    elif guess_row and guess_column == MISS:
        print("You have guessed that elready. Try again.")
        guess_row, guess_column = int(input("GUESS ROW:\n")), int(input("GUESS COLUMN:\n"))
    elif ai_guess_r and ai_guess_c == MISS:
        print("You have guessed that elready. Try again.")
        ai_guess_r, ai_guess_c = randint(1, len(ai)) - 1, randint(1, len(ai)) - 1    
     


def game_over(board, ai):

    print("Game Over. You did not sink the Battleship")
    print(data, "'s Board")
    # print(board_game(data, board))
    print("Computer's Board")
    # print(board_game("Computer", ai))

    return board


game_over(board, ai)


def validate_grid(user, comp):
    """
    Validated input for Row and Column values
    """
    try:
        if not user and not comp:
            raise ValueError(
                "Incorrect co-ordinates."
            )
    except ValueError as v_err:
        print(f"Wrong. {v_err} Try again.")
        return False

    return True    