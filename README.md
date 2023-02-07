
Making a choice.
https://www.codecademy.com/courses/learn-python/lessons/battleship/exercises/welcome-to-battleship

Trial and Errors.<br>
Tried using Append() method to add a HIT or MISS to the Battleship Board but it was not working correctly as I had not identified the user's guess for row and column are in separate lists. It lead to it just being added to the list and not changing the current "o" character which makes the hidden board.<br>
![Append atempt](images/readme-images/Append.board.png)

# Create empty list to store the game's board.
board = []
computer = []

# Create a list of 5 lists, all 5 "o" characters long. Loop and add in to
# the empty board variable above.
for x in range(5):
    board.append(["o"] * 5)


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
    board[guess_row][guess_column] = "*"
    print(board_game(board))
else:
    print("MISSED. Marked with an 'X' on the board")
    print(f"It was on Row:{random_row} and Column:{random_column}")
    print("The Battleship's position is marked with an 'S' on the board")

    board[random_row][random_column] = "S"
    board[guess_row][guess_column] = "X" 
    print(board_game(board)) 