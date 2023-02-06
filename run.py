# Create input for user's name to signify their board.

name_input = input("name:")
print_name = (name_input + "'s board!")
print(print_name)
         
   
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
        print(" ".join([x for x in values]), "\n")





#def place_ship(grid):
 #   board.append("S")
  #  print(grid)


# place_ship(grid)    

board = create_battleship_board()