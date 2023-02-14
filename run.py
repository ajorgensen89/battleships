from random import randint
# Import file above for random integer production.

# Created functions, with credit, from Love Sandwiches Walkthrough
# via the course.
# Adapted for use here. User must enter name into INPUT
# before continuing into the game.


def want_to_play_again():

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
        print("The AI(Computer) will be one step closer to winning..")
        print("Get GAME OVER and...")
        print("The Battleship's position is mark with an - 'S'")
        print("The players board will be the top board displayed.")
        print("The board underneathe, will belong to the Ai.")
        print("~" * 40)
        # Create input field for a user to create a name or use their own.
        while True:
            name_input = input("Enter a name: ")
            name = name_input
            # If a valid input is filled in, break from while loop and continue
            # with the Battleship game.
            if validate_input(name):
                name = name_input
                break
        # Return name value, to function, to be used to label the user's board.
        # Saved in variable - data.
        return name

    def validate_input(value):
        """
        Validates user input for name.
        Raises Error if user has not added a name.
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
                guess_r = int(input(integer))
            except ValueError:
                print("Not an integer! Try again.")
                continue
            else:
                return guess_r
            break

    def input_column(integer):
        """
        Check there is an entry for column that is an integer.
        Raises an error if the input is empty or not an integer, like a letter.
        """
        while True:
            try:
                guess_c = int(input(integer))
            except ValueError:
                print("Not an integer! Try again.")
                continue
            else:
                return guess_c
            break

    # Saved name input in 'data' variable.

    data = get_name_input()

    def place_ships_row(ship):
        """
        Check there is an entry for row that is an integer.
        Raises an error if the input is empty or not an integer, like a letter.
        """
        while True:
            try:
                ship_row = int(input(ship))
            except ValueError:
                print("Not an integer! Try again.")
                continue
            else:
                return ship_row
            break

    def place_ships_col(ship):
        """
        Check there is an entry for column that is an integer.
        Raises an error if the input is empty or not an integer, like a letter.
        """
        while True:
            try:
                ship_col = int(input(ship))
            except ValueError:
                print("Not an integer! Try again.")
                continue
            else:
                return ship_col
            break

    # Create empty list to store the game's board Redefine in function.
    board = []
    ai = []
    # Create a list of 5 lists, all 5 "o" characters long. Loop and add in to
    # the empty board variable above.
    for x in range(5):
        board.append(["o"] * 5)
        ai.append(["."] * 5)

    def battleship_game(board, ai):
        """
        Create a function that combines the above 5 lists into a 5x5 grid shape
        and remove decoration.
        Join list with a 'space' between the "o" characters.
        """
        for row in board:
            print((" ").join(row))

        for row in ai:
            print((" ").join(row))

    ai_s_row = randint(1, len(board)) - 1
    ai_s_col = randint(1, len(board[0])) - 1

    while True:
        print("\nFIRST...")
        print("Place your Battleship on the Computer's board for your enemy")
        print("to find!")
        print("Select 0-4 for the Row and same for the Column.")
        print("Example: Top left position would be ROW: 0 and COL: 0")
        ship_row = place_ships_row("ROW:\n")
        ship_col = place_ships_col("COLUMN:\n")
        if (ship_row < 0 or ship_col < 0) or (ship_row >= 5 or ship_col >= 5):
            print("YOUR LOCATION MUST BE IN THE OCEAN!")
            print("Place your Battleship on valid row and column between 0-4")
        else:
            print("....Battleship is in position....")
            break

    tally = 0
    while True:
        print("\nEnter your guess for the Computer's Battleship postion..")
        print("You must find it first to win!")
        validate_input("blah:")
        guess_r = input_row("GUESS ROW:\n")
        guess_c = input_column("GUESS COLUMN:\n")
        ai_guess_r = randint(1, len(board)) - 1
        ai_guess_c = randint(1, len(board[0])) - 1
        while True:
            if (guess_r < 0 or guess_c < 0) or (guess_r >= 5 or guess_c >= 5):
                print("Re enter a valid row and column number between 0-4")
                print("for the location of your ship on the Computer's board")
                guess_r = input_row("GUESS ROW:\n")
                guess_c = input_column("GUESS COLUMN:\n")
            else:
                break
        if guess_r == ai_s_row and guess_c == ai_s_col:
            print("HIT!")
            print("_" * 40)
            print("You sunk the Computer's Battleship first!")
            print(f"Row:{guess_r}")
            print(f"Column:{guess_c}\n")
            print(data, "'s Board!")
            ai[guess_r][guess_c] = "*"
            battleship_game(board, " ")
            battleship_game(" ", ai)
            print("AI's Board!")
            print("In", tally, "turns!")
            break
        if ai_guess_r == ship_row and ai_guess_c == ship_col:
            print("A! HIT your ship!")
            board[ai_guess_r][ai_guess_c] = "*"
            ai[guess_r][guess_c] = "X"
            battleship_game(board, " ")
            battleship_game(" ", ai)
            tally += 1
            print("AI has Won this time.. in", tally, "goes!")
            break
        elif ai[guess_r][guess_c] == "X":
            print("~" * 40)
            print("Nice try but you have guessed that already. Try again...")
        elif board[ai_guess_r][ai_guess_c] == "X":
            print("The AI already tried that")
            ai_guess_r = randint(1, len(board)) - 1
            ai_guess_c = randint(1, len(board[0])) - 1
            ai[guess_r][guess_c] = "X"
            board[ai_guess_r][ai_guess_c] = "X"
            battleship_game(board, " ")
            battleship_game(" ", ai)
            tally += 1
        else:
            print("MISSED... Try again...")
            print(f"Batttleship was on Row:{ai_s_row} Column:{ai_s_col}\n")
            print(data, "'s turn:", tally)
            print(data, "'s Board")
            ai[guess_r][guess_c] = "X"
            board[ai_guess_r][ai_guess_c] = "X"
            battleship_game(board, " ")
            battleship_game(" ", ai)
            print("AI's Board!")
            tally += 1


while True:
    want_to_play_again()
    print("Do you want to play Battleships again?")
    print("Hit the ENTER button to continue..")
    restart_battleships = input("Press 'y' for yes or 'n' for no: ")
    if restart_battleships == "y":
        continue
    elif restart_battleships == "n":
        print("Thanks for playing Battlehips..")
        print("Ill bring more Battleships next time!")
        print("You can bring your sinking skills!")
        break
    elif restart_battleships != "y" or "n":
        restart_battleships = input("Press 'y' for yes or 'n' for no: ")