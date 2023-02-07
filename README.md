Making a grid.
https://stackoverflow.com/questions/23177075/printing-a-list-into-grid

# Create input for user's name to signify their board.    

name_input = input("name:")
if not name_input:
    print("Not Valid...")
else:
    print_name = (name_input + "'s board!")
    print(print_name)

# Create variables to set a 5x5 grid play Battleships.
empty_list = []
grid_row = "." * 5
empty_list.append(" ".join(grid_row))
grid = empty_list * 5

class Board:
    """
    Board
    """
    def create_battleship_board():
        """
        Define a function to create a 5x5 board to play the game Battleships.
        """
        for values in grid:
            board = " ".join([x for x in values])
            # return board + '\n'
            print(board + '\n')
 

create_battleship_board()

#Select "." on grid

# Create variables to set a 5x5 grid play Battleships.
empty_list = []
grid_row = "." * 5
empty_list.append(" ".join(grid_row))
grid = empty_list * 5


def create_battleship_board():
    """
    Define a function to create a 5x5 board to play the game Battleships.
    """
    for values in grid:
        board = " ".join([x for x in values])
        # return board + '\n'
        print(board + '\n')

def run_game:
 create_battleship_board()


# Select "." on grid
 