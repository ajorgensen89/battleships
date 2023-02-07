HIDDEN = "."
BATTLESHIP = "S"
HIT = "X"

class Board:
    def __init__(self, name, size, type, board):
        self.name = name
        self.size = size
        self.type = type
        self.board = [[HIDDEN] for x in range(1,6) for _ in range(1,6)]
        self.guesses = []
        self.ships = []
board = [[HIDDEN] for x in range(1,6) for _ in range(1,6)]
print(board)        