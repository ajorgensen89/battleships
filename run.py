# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
class Game:
    """
    Main board game. Set the size of the board, the number of ships, 
    the name of the player and the type 
    being computer player board or user player board.
    """
    def __init__(self, size, ships, name, type):
        self.size = size
        self.ships = [["." for x in range(size)] for y in range(size)]
        self.name = name
        self.type = type
        self.guess_list = []
        self.ships_list = []