import os
# Create input for user's name to signify their board.  
 
  
def name_input():
    print("="*25)
    print("WELCOME TO BATTLESHIPS")
    print("Select a row: 0 to 4")
    print("and")
    print("Select a column: 0 to 4")
    print("=" * 25)

    name_input = input("Enter a name:")
    if not name_input:
        print("Not Valid...")
        os.system("run.py")
    else:
        print_name = (name_input + "'s board!")
        print(print_name)


name_input()        

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


create_battleship_board()

#Select "." on grid
