from random import randint
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

print(random_row, random_column)

guess_row = int(input("GUESS ROW:\n"))
guess_column = int(input("GUESS COLUMN:\n"))

if guess_row == random_row and guess_column == random_column:
    print("HIT.")
    print(f"The Battleship sunk on Row:{guess_row} and Column:{guess_column}")
    board[guess_row][guess_column] = "*"
    print(board_game(board))
else:
    print("MISSED.")
    print(f"It was on Row:{random_row} and Column:{random_column}")
    board[guess_row][guess_column] = "X" 
    print(board_game(board)) 